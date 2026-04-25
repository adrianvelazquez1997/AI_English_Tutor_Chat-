import re
from typing import List, Dict


def clean_text(text: str) -> str:
    text = text.replace("\t", " ")
    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"[ ]{2,}", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def preprocess_documents(documents: List[Dict]) -> List[Dict]:
    cleaned_docs = []

    for doc in documents:
        cleaned_text = clean_text(doc["text"])

        if cleaned_text:
            cleaned_docs.append({
                **doc,
                "text": cleaned_text
            })

    return cleaned_docs