from src.ingestion.rss_collector import fetch_all_news
from src.config.rss_sources import RSS_SOURCES
from src.processing.validator import validate_articles
from src.processing.cleaner import clean_articles
from src.processing.deduplicator import remove_duplicates
from src.storage.database import create_database, save_articles


# Step 1: Collect news
articles = fetch_all_news(RSS_SOURCES)

# Step 2: Validate articles
valid_articles, rejected_articles = validate_articles(articles)

# Step 3: Clean articles
cleaned_articles = clean_articles(valid_articles)

# Step 4: Remove duplicates
unique_articles = remove_duplicates(cleaned_articles)

# Step 5: Create database and save articles
create_database()
save_articles(unique_articles)

print("\nPipeline completed successfully!")
print("Total collected:", len(articles))
print("Valid articles:", len(valid_articles))
print("Rejected articles:", len(rejected_articles))
print("Cleaned articles:", len(cleaned_articles))
print("Unique articles:", len(unique_articles))