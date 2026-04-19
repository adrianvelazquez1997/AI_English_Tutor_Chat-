from pathlib import Path
from typing import List, Dict
from pypdf import PdfReader
from docx import Document


def extract_pdf(pdf_path: str, source_type: str) -> List[Dict]:
    """
    Extrae texto de un PDF página por página.
    Devuelve una lista de documentos con metadata.
    """
    reader = PdfReader(pdf_path)
    docs = []

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if text and text.strip():
            docs.append({
                "text": text.strip(),
                "source_file": Path(pdf_path).name,
                "source_path": str(pdf_path),
                "source_type": source_type,
                "file_type": "pdf",
                "page": page_num,
            })

    return docs


def extract_docx(docx_path: str, source_type: str) -> List[Dict]:
    """
    Extrae texto de un DOCX.
    Devuelve una lista con un solo documento.
    """
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


def load_file(file_path: str, source_type: str) -> List[Dict]:
    """
    Detecta tipo de archivo y usa el extractor correcto.
    """
    ext = Path(file_path).suffix.lower()

    if ext == ".pdf":
        return extract_pdf(file_path, source_type)
    if ext == ".docx":
        return extract_docx(file_path, source_type)

    return []


def load_all_documents(base_data_path: str = "data") -> List[Dict]:
    """
    Recorre data/cheat_sheets y data/books.
    Carga todos los PDF y DOCX encontrados.
    """
    base_path = Path(base_data_path)
    docs: List[Dict] = []

    sources = {
        "cheat_sheets": "cheat_sheet",
        "books": "book",
    }

    for folder_name, source_type in sources.items():
        folder_path = base_path / folder_name

        if not folder_path.exists():
            continue

        for file_path in folder_path.rglob("*"):
            if file_path.is_file():
                extracted_docs = load_file(str(file_path), source_type)
                docs.extend(extracted_docs)

    return docs