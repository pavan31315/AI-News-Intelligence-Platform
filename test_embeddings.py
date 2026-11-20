from src.storage.database import get_all_articles
from src.rag.chunker import chunk_articles
from src.rag.embedder import generate_embeddings


# Step 1: Load news articles
articles = get_all_articles()

# Step 2: Generate chunks
chunks = chunk_articles(
    articles,
    chunk_size=80,
    overlap=15
)

# Step 3: Extract chunk text
texts = [chunk["text"] for chunk in chunks]

print("Total chunks:", len(texts))

# Step 4: Generate embeddings
embeddings = generate_embeddings(texts)

# Step 5: Display results
print("\nEmbedding Results")
print("Total embeddings:", len(embeddings))
print("Embedding dimensions:", embeddings.shape[1])

print("\nFirst chunk:")
print(texts[0])

print("\nFirst embedding:")
print(embeddings[0][:10])