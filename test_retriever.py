
from src.rag.retriever import retrieve_relevant_news


queries = [
    "Which company develops Claude?",
    "What is happening in the video game industry?",
    "What cybersecurity problems are affecting technology?"
]


for query in queries:

    print("\n" + "=" * 70)
    print("USER QUESTION:", query)
    print("=" * 70)

    results = retrieve_relevant_news(query, top_k=3)

    for result in results:
        print("\nTitle:", result["title"])
        print("Source:", result["source"])
        print("Similarity:", round(result["similarity_score"], 4))
        print("Content:", result["text"])
