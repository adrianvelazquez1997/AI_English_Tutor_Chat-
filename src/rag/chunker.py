from typing import List, Dict
from src.config.settings import CHUNK_SIZE, CHUNK_OVERLAP


def chunk_text(
    text: str,
    chunk_size: int = CHUNK_SIZE,
    overlap: int = CHUNK_OVERLAP
) -> List[str]:
    if not text.strip():
        return []

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= text_length:
            break

        start += chunk_size - overlap

    return chunks


def chunk_documents(
    documents: List[Dict],
    chunk_size: int = CHUNK_SIZE,
    overlap: int = CHUNK_OVERLAP
) -> List[Dict]:
    chunked_docs = []

    for doc in documents:
        chunks = chunk_text(
            doc["text"],
            chunk_size=chunk_size,
            overlap=overlap
        )

        page_label = doc["page"] if doc["page"] is not None else "docx"

        for idx, chunk in enumerate(chunks):
            chunked_docs.append({
                **doc,
                "text": chunk,
                "chunk_id": f"{doc['source_file']}_{page_label}_{idx}",
                "chunk_index": idx,
            })

    return chunked_docs