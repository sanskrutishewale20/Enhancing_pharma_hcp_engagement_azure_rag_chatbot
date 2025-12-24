from openai import AzureOpenAI
import os
from search import retrieve_docs
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def ask_hcp(question):
    embedding = client.embeddings.create(
        model=os.getenv("AZURE_OPENAI_EMBEDDING"),
        input=question
    ).data[0].embedding

    context = retrieve_docs(embedding)

    prompt = f"""
You are a pharma medical assistant.
Answer ONLY using the context below.
If unsure, say "Information not available in approved documents."

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content
