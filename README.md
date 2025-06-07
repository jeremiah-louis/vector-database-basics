# Vector Database Basics

This project demonstrates the basics of using several vector (embedding) databases in Python, including [ChromaDB](https://www.trychroma.com/), [Pinecone](https://www.pinecone.io/), [Qdrant](https://qdrant.tech/), and [Milvus](https://milvus.io/).

## Features
- Create a collection (like a table) in a vector database
- Add documents (text) to the collection
- Query the collection for similar documents using embeddings

## Requirements
- Python 3.9 or higher

## Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/jeremiah-louis/vector-database-basics.git
   cd vector-database-basics
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   > **Note:** If you plan to use ChromaDB, you may need to install it separately:
   > ```bash
   > pip install chromadb
   > ```

## Environment Variables
Before running the scripts, create a `.env` file in the project root with the following variables (replace the example values with your actual API keys and endpoints):

```env
# Gemini API (Google Generative AI)
GEMINI_API_KEY=your-gemini-api-key-here

# Pinecone
PINECONE_API_KEY=your-pinecone-api-key-here

# Qdrant
QDRANT_URL=https://your-qdrant-instance-url
QDRANT_API_KEY=your-qdrant-api-key-here

# Milvus
MILVUS_URL=https://your-milvus-instance-url
MILVUS_TOKEN=your-milvus-token-here

# Firecrawl (if using batch scraping)
FIRECRAWL_API_KEY=your-firecrawl-api-key-here

# Wetrocloud (if using wetrocloud RAG)
WETRO_API_KEY=your-wetrocloud-api-key-here
```

## Usage
Each vector database has its own script located in `src/databases/`. Run the desired script as follows:

```bash
# ChromaDB
python src/databases/chroma-db.py

# Pinecone
python src/databases/pinecone-db.py

# Qdrant
python src/databases/qdrant-db.py

# Milvus
python src/databases/milvus-db.py
```

Each script will ingest data and perform a sample query, printing results to the console.

## File Overview
- `src/databases/chroma-db.py`: ChromaDB example
- `src/databases/pinecone-db.py`: Pinecone example
- `src/databases/qdrant-db.py`: Qdrant example
- `src/databases/milvus-db.py`: Milvus example
- `requirements.txt`: Python dependencies
- `.env`: Environment variables (not committed; see above for template)

## References
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Pinecone Docs](https://docs.pinecone.io/)
- [Qdrant Docs](https://qdrant.tech/documentation/)
- [Milvus Docs](https://milvus.io/docs/)

## License
This project is licensed under the Apache 2.0 License (see ChromaDB for details). 