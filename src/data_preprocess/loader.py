from pathlib import Path
from typing import List, Dict

from src.data_preprocess.extractor import extract_pdf, extract_docx
from src.config.settings import DATA_DIR


def load_file(file_path: str, source_type: str) -> List[Dict]:
    ext = Path(file_path).suffix.lower()

    if ext == ".pdf":
        return extract_pdf(file_path, source_type)

    if ext == ".docx":
        return extract_docx(file_path, source_type)

    return []


def load_all_documents(base_data_path: str = DATA_DIR) -> List[Dict]:
    base_path = Path(base_data_path)
    docs = []

    sources = {
        "cheat_sheets": "cheat_sheet",
        "books": "book",
    }

    for folder_name, source_type in sources.items():
        folder_path = base_path / folder_name

        if not folder_path.exists():
            print(f"Carpeta no encontrada: {folder_path}")
            continue

        for file_path in folder_path.rglob("*"):
            if file_path.is_file():
                docs.extend(load_file(str(file_path), source_type))

    return docs