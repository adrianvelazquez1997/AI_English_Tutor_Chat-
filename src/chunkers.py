from typing import List, Dict


def chunk_text(text: str, chunk_size: int = 700, overlap: int = 120) -> List[str]:
    """
    Divide texto en chunks por caracteres con overlap.
    """
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


def chunk_documents(documents: List[Dict], chunk_size: int = 700, overlap: int = 120) -> List[Dict]:
    """
    Convierte documentos limpios en chunks con metadata enriquecida.
    """
    chunked_docs: List[Dict] = []

    for doc in documents:
        chunks = chunk_text(doc["text"], chunk_size=chunk_size, overlap=overlap)

        for idx, chunk in enumerate(chunks):
            chunked_doc = {
                **doc,
                "text": chunk,
                "chunk_id": f"{doc['source_file']}_{doc['page']}_{idx}",
                "chunk_index": idx,
            }
            chunked_docs.append(chunked_doc)

    return chunked_docs