import faiss
import numpy as np

# This allows semantic code search.

index = None
documents = []

def create_vector_store(embeddings, docs):

    global index, documents

    dimension = len(embeddings[0])

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    documents = docs


def search(query_embedding, k=3):

    distances, indices = index.search(query_embedding, k)

    results = []

    for i in indices[0]:
        results.append(documents[i])

    return results