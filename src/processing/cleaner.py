import re
import html


def clean_text(text: str):
    if not text:
        return ""

    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()
    
def clean_articles(articles: list):
    cleaned_articles = []

    for article in articles:
        cleaned_article = article.copy()

        cleaned_article["title"] = clean_text(article.get("title"))
        cleaned_article["summary"] = clean_text(article.get("summary"))

        cleaned_articles.append(cleaned_article)

    return cleaned_articles