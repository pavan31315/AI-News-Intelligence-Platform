from src.storage.database import get_latest_articles

articles = get_latest_articles(10)

print("Latest articles:", len(articles))

for article in articles:
    print("\nID:", article["id"])
    print("Source:", article["source"])
    print("Title:", article["title"])