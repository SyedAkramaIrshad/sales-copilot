# Conversational AI Sales Copilot

A command-line AI copilot that helps sales teams understand and summarize past sales calls.  
The system ingests call transcripts, embeds them using a **state-of-the-art embedding model**, stores them in a **FAISS vector store**, and uses a **Retrieval-Augmented Generation (RAG)** approach powered by **Groq’s GPT-OSS-120B** to answer user questions with supporting evidence.

---

## Project Structure

```
.
├── data
│   ├── 1_demo_call.txt
│   ├── 2_pricing_call.txt
│   ├── 3_objection_call.txt
│   └── 4_negotiation_call.txt
├── src
│   ├── chatbot.py       # Core SalesCopilot class (RAG logic with Groq LLM + FAISS)
│   ├── ingestion.py     # Reads transcripts, chunks, embeds with BGE, stores in FAISS
│   └── cli.py           # Command-line interface for interacting with the copilot
├── storage
│   └── faiss_index      # Persisted FAISS vector store
├── .env.example         # Example environment variables
├── README.md
└── requirements.txt     # Python dependencies
```

---

## Features

- 📂 **Transcript ingestion**: Load `.txt` sales call transcripts and embed them with `BAAI/bge-large-en-v1.5`.  
- 🔎 **Retrieval-Augmented QA**: Answer questions grounded in transcript context.  
- 📝 **Summarization**: Automatically summarize the most recent call.  
- 📋 **Call management**: List all ingested call IDs.  
- ⚡ **Powered by Groq**: Uses `openai/gpt-oss-120b` through `langchain_groq` for efficient, low-latency responses.  
- ✅ **Strict grounding**: The chatbot will say *“I don’t know”* if the answer isn’t in the transcripts.  

---

## Setup and Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SyedAkramaIrshad/sales-copilot.git
   cd sales-copilot
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Rename `.env.example` → `.env`
   - Add your Groq API key:
     ```env
     GROQ_API_KEY="your_groq_api_key"
     ```

5. **Ingest transcripts**
   ```bash
   python src/ingestion.py
   ```
   This will create a FAISS index in the `storage/` directory.

---

## How to Run the Copilot

Once data ingestion is complete, start the chatbot:

```bash
python -m src.cli
```

### Available Commands
- `list my call ids` → Shows all available transcript IDs.  
- `summarise the last call` → Summarizes the most recent transcript.  
- `exit` → Quits the copilot.  

### Example Queries
- *“What objections were raised in the pricing calls?”*  
- *“Summarize the demo call.”*  
- *“Give me all negative comments about the product.”*  

---

## Assumptions & Notes

- Transcripts are plain `.txt` files with consistent formatting (`[timestamp] Speaker: message`).  
- Embeddings use **BAAI/bge-large-en-v1.5**, optimized for semantic retrieval.  
- Vector store is **FAISS**, persisted locally (`storage/faiss_index`).  
- LLM is **Groq GPT-OSS-120B** via `langchain_groq`.  
- For production, consider scaling to a managed vector database (e.g., Pinecone, Weaviate, Milvus).  
