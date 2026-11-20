from src.storage.database import get_all_articles
from src.llm.categorizer import categorize_articles

# Retrieve articles from SQLite
articles = get_all_articles()

# Start with only 3 articles
test_articles = articles[:3]

print("Articles selected:", len(test_articles))

# Categorize articles using Gemini
categorized, failed = categorize_articles(test_articles)

print("\nCategorization Results:")

for article in categorized:
    print("\nTitle:", article["title"])
    print("Category:", article["category"])
    print("Confidence:", article["confidence"])
    print("Reason:", article["reason"])

print("\nBatch Summary")
print("Successfully categorized:", len(categorized))
print("Failed:", len(failed))

for article in failed:
    print("Failed article:", article["title"])
    print("Error:", article["error"])