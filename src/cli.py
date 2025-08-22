from src.chatbot import SalesCopilot
from src.ingestion import ingest_data

def main():
    """
    Main function to run the CLI chatbot.
    """
    print("Welcome to the Sales AI Copilot!")
    print("You can ask questions about your sales calls, or use the following commands:")
    print("  - list my call ids")
    print("  - summarise the last call")
    print("  - exit")

    # This assumes you have already run ingestion.py separately
    copilot = SalesCopilot()

    while True:
        query = input("\nEnter your question or command: ").strip()

        if query.lower() == "exit":
            break
        elif query.lower() == "list my call ids":
            call_ids = copilot.list_call_ids()
            print("\nAvailable call IDs:")
            for call_id in call_ids:
                print(f"- {call_id}")
        elif query.lower() == "summarise the last call":
            summary = copilot.summarize_last_call()
            print("\nSummary of the last call:")
            print(summary["result"])
            print("\nSource Documents:")
            for doc in summary["source_documents"]:
                print(f"- {doc.metadata['source']}:")
                print(f"  {doc.page_content}")
        else:
            result = copilot.ask_question(query)
            print("\nAnswer:")
            print(result["result"])
            print("\nSource Documents:")
            for doc in result["source_documents"]:
                print(f"- {doc.metadata['source']}:")
                print(f"  {doc.page_content}")

if __name__ == "__main__":
    main()