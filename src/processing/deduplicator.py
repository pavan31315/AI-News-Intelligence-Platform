def remove_duplicates(articles: list):
    unique_articles = []
    seen_links = set()

    for article in articles:
        link = article.get("link")

        if link and link not in seen_links:
            seen_links.add(link)
            unique_articles.append(article)

    return unique_articles