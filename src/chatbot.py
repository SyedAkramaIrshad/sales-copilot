import os
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

load_dotenv()
class SalesCopilot:
    def __init__(self):
        # Ensure the Groq API key is available
        if not os.getenv("GROQ_API_KEY"):
            raise ValueError("GROQ_API_KEY not found in .env file")

        self.vector_store_path = "storage/faiss_index"
        self.embeddings = HuggingFaceEmbeddings(
            model_name="BAAI/bge-large-en-v1.5",
            model_kwargs={"device": "cpu"},
        )
        self.db = FAISS.load_local(self.vector_store_path, self.embeddings, allow_dangerous_deserialization=True)
        
        # Initialize the Groq Chat LLM
        self.llm = ChatGroq(
            temperature=0.1,
            model_name="openai/gpt-oss-120b",
            groq_api_key=os.getenv("GROQ_API_KEY")
        )
        self.qa_chain = self._create_qa_chain()

    def _create_qa_chain(self):
        prompt_template = """
            You are a helpful assistant that answers questions about past sales call transcripts. 
            Follow these rules strictly:

            1. Only use the provided context to answer the question. Do not use outside knowledge.  
            2. If the answer is explicitly present, extract it directly and state it clearly.  
            3. Always include the supporting snippet(s) from the context as **Source**.  
            4. If the answer cannot be found in the context, say exactly: "I don't know."  
            5. Be concise and factual. Do not add speculation or extra commentary.

            ---
            Context:
            {context}

            Question:
            {question}

            ---
            Answer:
            """

        PROMPT = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.db.as_retriever(search_kwargs={"k": 5}),
            return_source_documents=True,
            chain_type_kwargs={"prompt": PROMPT},
        )
        return qa_chain

    def ask_question(self, query):
        result = self.qa_chain.invoke({"query": query})
        return result

    def list_call_ids(self):
        data_path = "data/"
        files = [f for f in os.listdir(data_path) if f.endswith(".txt")]
        return files

    def summarize_last_call(self):
        data_path = "data/"
        files = [f for f in os.listdir(data_path) if f.endswith(".txt")]
        if not files:
            return "No calls found to summarize."
        last_call = sorted(files)[-1]
        query = f"Summarize the call transcript from the file named '{last_call}'"
        return self.ask_question(query)