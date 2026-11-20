
from src.rag.retriever import retrieve_relevant_news
from src.llm.gemini_client import generate_response


def generate_rag_answer(question: str, top_k: int = 3):

    # Step 1: Retrieve relevant news
    retrieved_articles = retrieve_relevant_news(
        question,
        top_k=top_k
    )

    if not retrieved_articles:
        return {
            "question": question,
            "answer": "I could not find relevant news articles.",
            "sources": []
        }

    # Step 2: Build context from retrieved articles
    context = ""

    for index, article in enumerate(retrieved_articles, start=1):

        context += f"""
        Article {index}
        Title: {article['title']}
        Source: {article['source']}
        Content: {article['text']}
        """

    # Step 3: Construct the RAG prompt
    prompt = f"""
    You are an AI news intelligence assistant.

    Answer the user's question using ONLY the news context
    provided below.

    If the context does not contain enough information,
    clearly say that the available news articles do not
    provide enough information.

    Do not invent facts or information.

    NEWS CONTEXT:
    {context}

    USER QUESTION:
    {question}

    Provide a clear and concise answer.
    """

    # Step 4: Generate answer using Gemini
    answer = generate_response(prompt)

    # Step 5: Return answer and sources
    sources = [
        {
            "title": article["title"],
            "source": article["source"],
            "similarity_score": article["similarity_score"]
        }
        for article in retrieved_articles
    ]

    return {
        "question": question,
        "answer": answer,
        "sources": sources
    }
