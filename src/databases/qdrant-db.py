from time import perf_counter
import os
from qdrant_client import QdrantClient
from qdrant_client.http import models as qdrant_models
import google.generativeai as gemini_client
from decouple import config
from data.batch_scrape_records import batch_scrape_records

# Set up Qdrant client
QDRANT_URL = config('QDRANT_URL')
QDRANT_API_KEY = config('QDRANT_API_KEY', default=None)
GEMINI_API_KEY = config('GEMINI_API_KEY')
gemini_client.configure(api_key=GEMINI_API_KEY)

qdrant = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

COLLECTION_NAME = 'batch_scrape_record'
VECTOR_SIZE = 768  # Gemini embedding-001 size

# Create collection if it doesn't exist
if COLLECTION_NAME not in [c.name for c in qdrant.get_collections().collections]:
    qdrant.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=qdrant_models.VectorParams(size=VECTOR_SIZE, distance=qdrant_models.Distance.COSINE)
    )

def get_embedding(text):
    response = gemini_client.embed_content(
        model="models/embedding-001",
        content=text,
        task_type="retrieval_document",
        title="Qdrant x Gemini",
    )
    return response['embedding']

points = []
for idx, url in enumerate(batch_scrape_records):
    embedding = get_embedding(url)
    points.append(qdrant_models.PointStruct(
        id=idx,  # integer ID
        vector=embedding,
        payload={
            "url": url
        }
    ))

# Upsert points in batches (Qdrant recommends batches for performance)
batch_size = 32
start_ingest = perf_counter()
for i in range(0, len(points), batch_size):
    qdrant.upsert(
        collection_name=COLLECTION_NAME,
        points=points[i:i+batch_size]
    )
ingest_time = perf_counter() - start_ingest
print(f"Ingested {len(points)} points into Qdrant collection '{COLLECTION_NAME}'")
print(f"Ingestion time: {ingest_time:.2f} seconds")

# Example query
query_text = "Firecrawl Pricing"
query_vector = get_embedding(query_text)

start_query = perf_counter()
search_result = qdrant.search(
    collection_name=COLLECTION_NAME,
    query_vector=query_vector,
    limit=10  # Number of results to return
)
query_time = perf_counter() - start_query
print(f"Query time: {query_time:.2f} seconds")

for hit in search_result:
    print(f"Score: {hit.score}, Payload: {hit.payload}")