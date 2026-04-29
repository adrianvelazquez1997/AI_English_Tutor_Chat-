import json
import faiss
import numpy as np
from pathlib import Path

from src.config.settings import VECTORSTORE_DIR


def build_faiss_index(
    chunks: list[dict],
    embeddings: list[list[float]],
    output_dir: Path = VECTORSTORE_DIR
):
    output_dir.mkdir(parents=True, exist_ok=True)

    vectors = np.array(embeddings, dtype="float32")
    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(vectors)

    faiss.write_index(index, str(output_dir / "index.faiss"))

    with open(output_dir / "metadata.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)
    np.save(output_dir / "embeddings.npy", vectors)

def load_faiss_index(input_dir: Path = VECTORSTORE_DIR):
    index_path = input_dir / "index.faiss"
    metadata_path = input_dir / "metadata.json"

    if not index_path.exists():
        raise FileNotFoundError(f"No existe el índice FAISS: {index_path}")

    if not metadata_path.exists():
        raise FileNotFoundError(f"No existe metadata.json: {metadata_path}")

    index = faiss.read_index(str(index_path))

    with open(metadata_path, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    return index, metadata

def load_embeddings(input_dir: Path = VECTORSTORE_DIR):
    file_path = input_dir / "embeddings.npy"

    if not file_path.exists():
        raise FileNotFoundError(f"No existe embeddings.npy en {file_path}")

    return np.load(file_path)