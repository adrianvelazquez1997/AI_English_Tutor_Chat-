from src.data_preprocess.loader import load_all_documents
from src.data_preprocess.cleaner import preprocess_documents
from src.rag.chunker import chunk_documents
from src.rag.embedder import embed_texts
from src.rag.vectorstore import build_faiss_index

"""
Este script se encarga de generar el vector store una única vez a partir de los documentos.

El resultado (índice FAISS y metadata) se persiste en disco y luego es cargado por la aplicación 
en tiempo de ejecución.

De esta manera, se evita la recomputación de embeddings y la inicialización repetitiva del vector 
store, optimizando el rendimiento y reduciendo el costo de llamadas a la API.
"""


def main():
    docs = load_all_documents()
    cleaned_docs = preprocess_documents(docs)
    chunks = chunk_documents(cleaned_docs)

    if not chunks:
        raise ValueError("No se encontraron chunks para indexar.")

    texts = [chunk["text"] for chunk in chunks]
    embeddings = embed_texts(texts)

    build_faiss_index(chunks, embeddings)

    print(f"Documentos cargados: {len(docs)}")
    print(f"Chunks generados: {len(chunks)}")
    print("Vectorstore creado correctamente.")


if __name__ == "__main__":
    main()