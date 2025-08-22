import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def ingest_data():
    """
    Reads call transcripts, splits them into chunks, creates high-quality embeddings,
    and stores them in a FAISS vector store for powerful retrieval.
    """
    data_path = "data/"
    vector_store_path = "storage/faiss_index"

    # Get a list of all .txt files in the data directory
    files = [f for f in os.listdir(data_path) if f.endswith(".txt")]

    if not files:
        print("No .txt files found in the data directory.")
        return

    print("Loading documents...")
    documents = []
    for file in files:
        loader = TextLoader(os.path.join(data_path, file), encoding="utf-8")
        documents.extend(loader.load())

    # Use a text splitter with a larger overlap to preserve context between chunks
    print("Splitting documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=400)
    docs = text_splitter.split_documents(documents)

    # Use a more powerful, state-of-the-art embedding model for better retrieval accuracy.
    # BAAI/bge-large-en-v1.5 is a top-performing open-source model.
    print("Creating high-quality embeddings with BAAI/bge-large-en-v1.5...")
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-large-en-v1.5",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}, # Recommended for BGE models
    )

    print("Storing embeddings in FAISS vector store...")
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(vector_store_path)
    print(f"Data ingestion complete. FAISS index created at: {vector_store_path}")

if __name__ == "__main__":
    ingest_data()
