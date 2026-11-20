def validate_articles(articles: list):
    valid_articles = []
    rejected_articles = []

    for article in articles:
        title = article.get("title")
        link = article.get("link")

        if title and title.strip() and link and link.strip():
            valid_articles.append(article)
        else:
            rejected_articles.append(article)

    return valid_articles, rejected_articles