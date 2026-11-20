def chunk_text(text: str, chunk_size: int = 100, overlap: int = 20):
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk size")

    if not isinstance(text, str) or not text.strip():
        return []

    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunks.append(" ".join(words[start:end]))

        if end >= len(words):
            break

        start = end - overlap

    return chunks


def chunk_articles(articles: list, chunk_size: int = 100, overlap: int = 20):
    all_chunks = []

    for article in articles:
        text = article.get("summary") or ""

        chunks = chunk_text(text, chunk_size, overlap)

        for index, chunk in enumerate(chunks):
            all_chunks.append({
                "article_id": article.get("id"),
                "title": article.get("title"),
                "source": article.get("source"),
                "chunk_index": index,
                "text": chunk
            })

    return all_chunks