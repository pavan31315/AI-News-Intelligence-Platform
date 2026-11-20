import sqlite3


def create_database():
    connection = sqlite3.connect("data/news.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            title TEXT NOT NULL,
            link TEXT UNIQUE NOT NULL,
            published TEXT,
            summary TEXT
        )
    """)

    connection.commit()
    connection.close()
def save_articles(articles: list):
    connection = sqlite3.connect("data/news.db")
    cursor = connection.cursor()

    for article in articles:
        cursor.execute("""
            INSERT OR IGNORE INTO articles
            (source, title, link, published, summary)
            VALUES (?, ?, ?, ?, ?)
        """, (
            article.get("source"),
            article.get("title"),
            article.get("link"),
            article.get("published"),
            article.get("summary")
        ))

    connection.commit()
    connection.close()

    print(f"Saved {len(articles)} articles to database.")

def get_all_articles():
    connection = sqlite3.connect("data/news.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM articles")

    articles = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return articles

def get_articles_by_source(source: str):
    connection = sqlite3.connect("data/news.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM articles WHERE source = ?",
        (source,)
    )

    articles = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return articles
def get_article_by_id(article_id: int):
    connection = sqlite3.connect("data/news.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM articles WHERE id = ?",
        (article_id,)
    )

    article = cursor.fetchone()

    connection.close()

    return dict(article) if article else None

def search_articles(keyword: str):
    connection = sqlite3.connect("data/news.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute(
    """
    SELECT * FROM articles
    WHERE title LIKE ? OR summary LIKE ?
    """,
    (f"%{keyword}%", f"%{keyword}%")
     )

    articles = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return articles
def get_latest_articles(limit: int = 10):
    connection = sqlite3.connect("data/news.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM articles
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )

    articles = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return articles

if __name__ == "__main__":
    create_database()
    print("Database and articles table created successfully!")