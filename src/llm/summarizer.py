from src.llm.gemini_client import generate_response


def summarize_article(article: dict):
    prompt = f"""
    You are an AI news analyst.

    Summarize the following news article in 3 concise sentences.

    Title: {article.get("title")}

    Article Summary:
    {article.get("summary")}

    Focus on:
    1. What happened?
    2. Why is it important?
    3. What is the potential impact?

    Return only the summary.
    """

    return generate_response(prompt)