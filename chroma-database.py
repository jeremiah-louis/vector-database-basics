import chromadb
chroma_client = chromadb.Client()

# A collection is like a table in a database that stores text and metadata.
collection = chroma_client.create_collection(name="my_collection")

# Add documents to the collection.
# Documents are the text and metadata that you want to store in the collection.
# IDs are the unique identifiers for the documents.
# Chroma will embed the documents for you.
# Chroma will store the documents in the collection.
# Chroma will return the documents in the collection.
# Chroma will return the documents in the collection.

collection.add(
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"
    ],
    ids=["id1", "id2"]
)

# Query the collection.
# Query texts are the text that you want to search for in the collection.
# N results is the number of results to return.
# Chroma will embed the query texts for you.
# Chroma will search the collection for the query texts.
# Chroma will return the results.

results = collection.query(
    query_texts=["This is a query document about florida"], # Chroma will embed this for you
    n_results=2 # how many results to return
)

print(results)
