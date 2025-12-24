from fastapi import FastAPI
from rag import ask_hcp

app = FastAPI(title="Pharma HCP RAG Chatbot")

@app.post("/chat")
def chat(query: str):
    answer = ask_hcp(query)
    return {"response": answer}
