from time import perf_counter
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from data.batch_scrape_records import batch_scrape_records

chroma_client = chromadb.Client()

# A collection is like a table in a database that stores text and metadata.
embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

collection = chroma_client.create_collection(
    name="batch_scrape_record",
    embedding_function=embedding_function
)

# Use batch_scrape_records for indexing, assign string IDs
ids = [f"id{idx}" for idx in range(len(batch_scrape_records))]

start_ingest = perf_counter()
collection.add(
    documents=batch_scrape_records,
    ids=ids
)
ingest_time = perf_counter() - start_ingest
print(f"Ingestion time: {ingest_time:.2f} seconds")

start_query = perf_counter()
results = collection.query(
    query_texts=["Firecrawl pricing"], # Chroma will embed this for you
    n_results=10 # how many results to return
)
query_time = perf_counter() - start_query
print(f"Query time: {query_time:.2f} seconds")

for i, doc in enumerate(results["documents"][0]):
    score = results["distances"][0][i]
    doc_id = results["ids"][0][i]
    print(f"ID: {doc_id} | Score: {score:.4f} | Document: {doc}")
