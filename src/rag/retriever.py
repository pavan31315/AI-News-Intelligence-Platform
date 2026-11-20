
import numpy as np

from src.rag.embedder import generate_embeddings
from src.rag.vector_store import load_vector_store


def retrieve_relevant_news(query: str, top_k: int = 3):

    if not isinstance(query, str) or not query.strip():
        raise ValueError("Search query cannot be empty")

    if top_k <= 0:
        raise ValueError("top_k must be greater than zero")

    # Step 1: Load FAISS index and metadata
    index, chunks = load_vector_store()

    # Step 2: Convert user query into an embedding
    query_embedding = generate_embeddings([query])

    query_vector = np.asarray(
        query_embedding,
        dtype=np.float32
    )

    # Step 3: Search FAISS index
    scores, indices = index.search(
        query_vector,
        min(top_k, index.ntotal)
    )

    # Step 4: Collect matching articles
    results = []

    for score, index_position in zip(scores[0], indices[0]):

        if index_position == -1:
            continue

        article = chunks[index_position].copy()

        article["similarity_score"] = float(score)

        results.append(article)

    return results
