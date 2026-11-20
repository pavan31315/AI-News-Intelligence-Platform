from src.storage.database import get_all_articles
from src.rag.chunker import chunk_articles

articles = get_all_articles()

articles_with_summaries = [
    article for article in articles
    if article.get("summary")
]

chunks = chunk_articles(
    articles_with_summaries,
    chunk_size=80,
    overlap=15
)

print("Total articles:", len(articles_with_summaries))
print("Total chunks generated:", len(chunks))

print("\nFirst 3 chunks:")

for chunk in chunks[:3]:
    print("\nArticle ID:", chunk["article_id"])
    print("Title:", chunk["title"])
    print("Chunk Index:", chunk["chunk_index"])
    print("Text:", chunk["text"])