<<<<<<< HEAD
# Conversational AI Copilot

This project is a command-line chatbot that helps sales users understand and summarize their past sales calls. The bot ingests call transcripts, embeds them using a sentence-transformer model, stores them in a FAISS vector store, and uses a Retrieval-Augmented Generation (RAG) approach to answer user questions.

## Project Structure

```
.
├── data
│   ├── 1_demo_call.txt
│   ├── 2_pricing_call.txt
│   ├── 3_objection_call.txt
│   └── 4_negotiation_call.txt
├── src
│   ├── chatbot.py
│   ├── ingestion.py
│   └── cli.py
├── storage
│   └── faiss_index
├── .env.example
├── README.md
└── requirements.txt
```



- **data/**: Contains the raw call transcript files.
- **src/**: Contains the Python source code for the project.
  - `ingestion.py`: Handles reading, chunking, embedding, and storing the transcripts.
  - `chatbot.py`: Contains the core logic for the RAG-based chatbot.
  - `cli.py`: Provides a command-line interface for interacting with the chatbot.
- **storage/**: Stores the FAISS vector index.
- **.env.example**: Example environment file. You'll need to create a `.env` file with your Hugging Face API token and Groq token.
- **README.md**: This file.
- **requirements.txt**: A list of Python dependencies for the project.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    - Rename `.env.example` to `.env`.
    - Add your Hugging Face API token to the `.env` file:
      ```
      HUGGINGFACEHUB_API_TOKEN="your_hugging_face_api_token"
      ```

5.  **Ingest the data:**
    Before running the chatbot for the first time, you need to ingest the call transcripts.
    ```bash
    python src/ingestion.py
    ```
    This will create a FAISS index in the `storage/` directory.

## How to Run the Chatbot

Once the setup is complete and the data has been ingested, you can run the CLI chatbot:

```bash
python src/cli.py
```

You will be prompted to enter your questions. Here are some example commands you can use:

-   `list my call ids`
-   `summarise the last call`
-   `What were the main objections raised in the calls?`
-   `Give me all negative comments when pricing was mentioned in the calls`
-   `ingest a new call transcript from <path>`

To exit the chatbot, type `exit`.

## Assumptions

-   The call transcripts are in a consistent format, with each line starting with a timestamp and speaker information (e.g., `[00:00] AE (Jordan):`).
-   The user has a Hugging Face account and an API token with the necessary permissions.
-   The `sentence-transformers/all-MiniLM-L6-v2` model is used for embeddings, and `mistralai/Mistral-7B-Instruct-v0.2` is used for generation. These can be changed in the `chatbot.py` file.
-   The FAISS index is stored locally. For a production environment, a more robust and scalable vector database would be recommended.
=======
# sales-copilot
>>>>>>> 4e2c774024192efca8e7dc4da28321756a6b7278
