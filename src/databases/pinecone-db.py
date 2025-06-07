from time import perf_counter
from pinecone import Pinecone, ServerlessSpec
import google.generativeai as gemini_client
from decouple import config
from data.batch_scrape_records import batch_scrape_records
from data.records import pinecone_records

# Configure Gemini
GEMINI_API_KEY = config("GEMINI_API_KEY")
gemini_client.configure(api_key=GEMINI_API_KEY)

def get_embedding(text):
    response = gemini_client.embed_content(
        model="models/embedding-001",
        content=text,
        task_type="retrieval_document",
        title="Pinecone x Gemini",
    )
    return response['embedding']

# Pinecone setup
pc = Pinecone(api_key=config("PINECONE_API_KEY"))
index_name = "pinecone-search-index"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=768,  # Gemini embedding size
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)

# Prepare vectors for upsert
vectors = []
for idx, url in enumerate(batch_scrape_records):
    embedding = get_embedding(url)
    vectors.append({
        "id": str(idx),
        "values": embedding,
        "metadata": {"url": url}
    })

start_ingest = perf_counter()
# Upsert vectors
index.upsert(vectors=vectors)
ingest_time = perf_counter() - start_ingest
print(f"Inserted {len(vectors)} records into Pinecone index '{index_name}'")
print(f"Ingestion time: {ingest_time:.2f} seconds")

#### Query the db
# Your query
query_text = "Mendable pricing"
query_vector = get_embedding(query_text)

start_query = perf_counter()
# Query Pinecone
results = index.query(
    vector=query_vector,
    top_k=10,
    include_metadata=True
)
query_time = perf_counter() - start_query
print(f"Query time: {query_time:.2f} seconds")

for match in results['matches']:
    print(f"Score: {match['score']}, URL: {match['metadata']['url']}")