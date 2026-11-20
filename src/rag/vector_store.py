
import json
from pathlib import Path

import faiss
import numpy as np


INDEX_PATH = Path("data/news_faiss.index")
METADATA_PATH = Path("data/news_chunks.json")


def build_vector_store(embeddings, chunks):

    if len(embeddings) != len(chunks):
        raise ValueError("Embeddings and chunks must have the same length")

    if len(chunks) == 0:
        raise ValueError("Cannot build an index with no chunks")

    vectors = np.asarray(embeddings, dtype=np.float32)

    dimension = vectors.shape[1]

    index = faiss.IndexFlatIP(dimension)

    index.add(vectors)

    return index


def save_vector_store(index, chunks):

    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)

    faiss.write_index(index, str(INDEX_PATH))

    with open(METADATA_PATH, "w", encoding="utf-8") as file:
        json.dump(chunks, file, ensure_ascii=False, indent=2)

    print("FAISS index and metadata saved successfully!")


def load_vector_store():

    if not INDEX_PATH.exists() or not METADATA_PATH.exists():
        raise FileNotFoundError("Vector store files not found. Build the index first.")

    index = faiss.read_index(str(INDEX_PATH))

    with open(METADATA_PATH, "r", encoding="utf-8") as file:
        chunks = json.load(file)

    if index.ntotal != len(chunks):
        raise ValueError("FAISS index and metadata counts do not match")

    return index, chunks
