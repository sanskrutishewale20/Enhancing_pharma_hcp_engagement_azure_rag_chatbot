from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI is running"}


@app.post("/chat")
def chat(query: str):
    return {"response": f"You asked: {query}"}
