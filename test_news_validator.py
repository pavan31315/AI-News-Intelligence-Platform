from src.ingestion.rss_collector import fetch_all_news
from src.config.rss_sources import RSS_SOURCES
from src.processing.validator import validate_articles

articles = fetch_all_news(RSS_SOURCES)

valid_articles, rejected_articles = validate_articles(articles)

print("Total collected:", len(articles))
print("Valid articles:", len(valid_articles))
print("Rejected articles:", len(rejected_articles))