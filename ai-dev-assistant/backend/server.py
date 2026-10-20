from fastapi import FastAPI
from pydantic import BaseModel
import ollama

from code_loader import load_code_files
from embeddings import create_embeddings
from vector_store import create_vector_store, search

app = FastAPI()

class Query(BaseModel):
    question: str

# Load codebase
docs = load_code_files("../codebase")

texts = [d["content"] for d in docs]

embeddings = create_embeddings(texts)

create_vector_store(embeddings, docs)


@app.post("/ask")
def ask_codebase(q: Query):

    query_embed = create_embeddings([q.question])

    results = search(query_embed)

    context = ""

    for r in results:
        context += r["content"] + "\n\n"

    prompt = f"""
You are an AI coding assistant.

Project code:

{context}

User question:
{q.question}
"""

    response = ollama.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"answer": response["message"]["content"]}