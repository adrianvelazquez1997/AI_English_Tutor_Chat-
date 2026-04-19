import re
from typing import List, Dict


def clean_text(text: str) -> str:
    """
    Limpieza básica:
    - espacios múltiples
    - saltos de línea innecesarios
    - tabs
    """
    text = text.replace("\t", " ")
    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"[ ]{2,}", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def preprocess_documents(documents: List[Dict]) -> List[Dict]:
    """
    Aplica limpieza a todos los documentos manteniendo metadata.
    """
    cleaned_docs = []

    for doc in documents:
        cleaned_text = clean_text(doc["text"])

        if not cleaned_text:
            continue

        cleaned_doc = {**doc, "text": cleaned_text}
        cleaned_docs.append(cleaned_doc)

    return cleaned_docs