import numpy as np

from src.rag.embedder import embed_text
from src.rag.vectorstore import load_faiss_index
from src.config.settings import TOP_K


FAISS_INDEX = None
FAISS_METADATA = None


def initialize_retriever():
    global FAISS_INDEX, FAISS_METADATA
    FAISS_INDEX, FAISS_METADATA = load_faiss_index()


def retrieve_similar_chunks(query: str, top_k: int = TOP_K):
    global FAISS_INDEX, FAISS_METADATA

    if FAISS_INDEX is None or FAISS_METADATA is None:
        initialize_retriever()

    query_embedding = embed_text(query)
    query_vector = np.array([query_embedding], dtype="float32")

    distances, indices = FAISS_INDEX.search(query_vector, top_k)

    results = []

    for idx, dist in zip(indices[0], distances[0]):
        if idx == -1:
            continue

        chunk = FAISS_METADATA[idx]

        results.append({
            "text": chunk["text"],
            "metadata": chunk,
            "score": float(dist)
        })

    return results


def retrieve_context(user_message: str, top_k: int = TOP_K) -> str:
    results = retrieve_similar_chunks(user_message, top_k=top_k)

    context_blocks = []

    for result in results:
        meta = result["metadata"]

        context_blocks.append(
            f"[Source: {meta['source_file']} | Page: {meta.get('page', 'N/A')}]\n"
            f"{result['text']}"
        )

    return "\n\n".join(context_blocks)