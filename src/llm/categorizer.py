import json
from src.llm.gemini_client import generate_response


ALLOWED_CATEGORIES = [
    "Artificial Intelligence",
    "Technology",
    "Cybersecurity",
    "Business",
    "Gaming",
    "Science",
    "Politics",
    "Other"
]


def validate_category_result(result: dict):

    if not isinstance(result, dict):
        raise ValueError("AI response must be a dictionary")

    category = result.get("category")
    confidence = result.get("confidence")
    reason = result.get("reason")

    if category not in ALLOWED_CATEGORIES:
        raise ValueError(f"Invalid category: {category}")

    if (
        isinstance(confidence, bool)
        or not isinstance(confidence, (int, float))
        or not 0 <= confidence <= 1
    ):
        raise ValueError("Confidence must be between 0 and 1")

    if not isinstance(reason, str) or not reason.strip():
        raise ValueError("Reason must be a non-empty string")

    return result


def categorize_article(article: dict):

    prompt = f"""
    You are an expert news classification system.

    Analyze the following news article.

    Choose exactly ONE category from:
    {", ".join(ALLOWED_CATEGORIES)}

    Article Title:
    {article.get("title")}

    Article Summary:
    {article.get("summary")}

    Return ONLY valid JSON in this format:

    {{
        "category": "Gaming",
        "confidence": 0.96,
        "reason": "The article discusses a video game."
    }}

    Confidence must be a number between 0 and 1.
    Do not include Markdown or additional text.
    """

    response = generate_response(prompt)

    try:
        result = json.loads(response)

    except json.JSONDecodeError as error:
        raise ValueError(f"Gemini returned invalid JSON: {error}") from error

    return validate_category_result(result)

def categorize_articles(articles: list):
    categorized_articles = []
    failed_articles = []

    for article in articles:
        try:
            result = categorize_article(article)

            categorized_articles.append({
                "id": article.get("id"),
                "title": article.get("title"),
                "category": result["category"],
                "confidence": result["confidence"],
                "reason": result["reason"]
            })

        except Exception as error:
            failed_articles.append({
                "title": article.get("title"),
                "error": str(error)
            })

    return categorized_articles, failed_articles