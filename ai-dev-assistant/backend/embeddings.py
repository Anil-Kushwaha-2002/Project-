from sentence_transformers import SentenceTransformer

# Embeddings convert code → numerical vectors.

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(texts):

    return model.encode(texts)