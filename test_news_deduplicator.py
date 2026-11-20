from src.ingestion.rss_collector import fetch_all_news
from src.config.rss_sources import RSS_SOURCES
from src.processing.validator import validate_articles
from src.processing.cleaner import clean_articles
from src.processing.deduplicator import remove_duplicates

articles = fetch_all_news(RSS_SOURCES)

valid_articles, rejected_articles = validate_articles(articles)

cleaned_articles = clean_articles(valid_articles)

unique_articles = remove_duplicates(cleaned_articles)

print("Total collected:", len(articles))
print("Valid articles:", len(valid_articles))
print("Rejected articles:", len(rejected_articles))
print("Cleaned articles:", len(cleaned_articles))
print("Unique articles:", len(unique_articles))
print("Duplicates removed:", len(cleaned_articles) - len(unique_articles))