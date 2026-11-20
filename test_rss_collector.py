from src.ingestion.rss_collector import fetch_all_news
from src.config.rss_sources import RSS_SOURCES

articles = fetch_all_news(RSS_SOURCES)

print(f"Total articles collected: {len(articles)}")

for article in articles[:10]:
    print("\nSource:", article["source"])
    print("Title:", article["title"])
    print("Link:", article["link"])