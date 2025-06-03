# Vector Database Basics

This project demonstrates the basics of using a vector (embedding) database in Python with [ChromaDB](https://www.trychroma.com/).

## Features
- Create a collection (like a table) in a vector database
- Add documents (text) to the collection
- Query the collection for similar documents using embeddings

## Requirements
- Python 3.9 or higher

## Installation
1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd vector-database-basics
   ```

2. **(Optional) Create and activate a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install chromadb
   ```
   > **Note:** `chromadb` is required but not listed in `requirements.txt`. Install it separately as shown above.

## Usage
Run the main script to see how to create a collection, add documents, and query for similar documents:

```bash
python chroma-database.py
```

You should see output similar to:
```
{'ids': [['id1', 'id2']], 'distances': [[...]], 'documents': [['This is a document about pineapple', 'This is a document about oranges']]}
```

## File Overview
- `chroma-database.py`: Main script demonstrating ChromaDB usage
- `requirements.txt`: Python dependencies (except `chromadb`)

## References
- [ChromaDB Documentation](https://docs.trychroma.com/)

## License
This project is licensed under the Apache 2.0 License (see ChromaDB for details). 