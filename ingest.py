from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import *
from openai import AzureOpenAI
import os, uuid
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def embed(text):
    return client.embeddings.create(
        model=os.getenv("AZURE_OPENAI_EMBEDDING"),
        input=text
    ).data[0].embedding

documents = [
    {
        "id": str(uuid.uuid4()),
        "content": "Drug X is indicated for Type 2 Diabetes...",
        "vector": embed("Drug X is indicated for Type 2 Diabetes...")
    }
]

search_client = SearchClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    index_name=os.getenv("AZURE_SEARCH_INDEX"),
    credential=os.getenv("AZURE_SEARCH_KEY")
)

search_client.upload_documents(documents)
print("Indexed pharma documents")
