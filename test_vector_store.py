
from src.storage.database import get_all_articles
from src.rag.chunker import chunk_articles
from src.rag.embedder import generate_embeddings
from src.rag.vector_store import (
    build_vector_store,
    save_vector_store,
    load_vector_store
)


# Step 1: Load articles
articles = get_all_articles()

# Step 2: Generate chunks
chunks = chunk_articles(
    articles,
    chunk_size=80,
    overlap=15
)

# Step 3: Generate embeddings
texts = [chunk["text"] for chunk in chunks]
embeddings = generate_embeddings(texts)

# Step 4: Build FAISS index
index = build_vector_store(embeddings, chunks)

# Step 5: Save vector store
save_vector_store(index, chunks)

# Step 6: Load vector store
loaded_index, loaded_chunks = load_vector_store()

# Step 7: Verify results
print("\nVector Store Results")
print("Total vectors:", loaded_index.ntotal)
print("Total metadata records:", len(loaded_chunks))
print("Embedding dimensions:", loaded_index.d)
print("First article:", loaded_chunks[0]["title"])
