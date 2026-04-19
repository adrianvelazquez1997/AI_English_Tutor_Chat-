import json
import faiss
import numpy as np
from pathlib import Path

def build_faiss_index(chunks: list[dict], embeddings: list[list[float]], output_dir:str = "vectorstore"):
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    vectors = np.array(embeddings, dtype="float32")
    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(vectors)

    faiss.write_index(index, f"{output_dir}/index.faiss")

    with open(f"{output_dir}/metadata.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)


def load_faiss_index(input_dir: str = "vectorstore"):
    index = faiss.read_index(f"{input_dir}/index.faiss")

    with open(f"{input_dir}/metadata.json", "r", encoding="utf-8") as f:
        metadata = json.load(f)

    return index, metadata