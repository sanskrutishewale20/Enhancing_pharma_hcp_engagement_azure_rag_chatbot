from azure.search.documents import SearchClient
import os
from dotenv import load_dotenv

load_dotenv()

def retrieve_docs(query_vector):
    client = SearchClient(
        endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
        index_name=os.getenv("AZURE_SEARCH_INDEX"),
        credential=os.getenv("AZURE_SEARCH_KEY")
    )

    results = client.search(
        search_text="",
        vector_queries=[{
            "vector": query_vector,
            "k": 3,
            "fields": "vector"
        }]
    )

    return [doc["content"] for doc in results]
