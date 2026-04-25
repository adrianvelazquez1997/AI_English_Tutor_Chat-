from pathlib import Path
from typing import List, Dict
from pypdf import PdfReader
from docx import Document

def extract_pdf (pdf_path: str, source_type: str) -> List[Dict]:
    reader = PdfReader(pdf_path)
    docs = []

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text and text.strip():
            docs.append({
                "text":text.strip(),
                "source_file": Path(pdf_path).name,
                "source_path": str(pdf_path),
                "source_type": source_type,
                "file_type": "pdf",
                "page": page_num,
            })
    return docs

def extract_docx(docx_path: str, source_type: str) -> List[Dict]:
    doc = Document(docx_path)
    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    text = "\n".join(paragraphs)

    if not text.strip():
        return []

    return [{
        "text": text,
        "source_file": Path(docx_path).name,
        "source_path": str(docx_path),
        "source_type": source_type,
        "file_type": "docx",
        "page": None,
    }]