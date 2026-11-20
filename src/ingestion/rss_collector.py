import feedparser


def fetch_rss_feed(feed_url: str):
    feed = feedparser.parse(feed_url)

    articles = []

    for entry in feed.entries:
        article = {
            "title": entry.get("title"),
            "link": entry.get("link"),
            "published": entry.get("published"),
            "summary": entry.get("summary"),
        }

        articles.append(article)

    return articles


def fetch_all_news(sources: dict):
    all_articles = []

    for source_name, feed_url in sources.items():
        articles = fetch_rss_feed(feed_url)

        for article in articles:
            article["source"] = source_name

        all_articles.extend(articles)

    return all_articles