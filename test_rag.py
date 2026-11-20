
from src.rag.answer_generator import generate_rag_answer


question = "Which company develops Claude and what is happening with it?"

result = generate_rag_answer(question, top_k=3)

print("\nUSER QUESTION:")
print(result["question"])

print("\nAI GENERATED ANSWER:")
print(result["answer"])

print("\nSOURCES:")
for source in result["sources"]:
    print("\nTitle:", source["title"])
    print("Source:", source["source"])
    print("Similarity:", round(source["similarity_score"], 4))
