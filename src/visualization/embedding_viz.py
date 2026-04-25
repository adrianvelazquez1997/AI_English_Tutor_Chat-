import numpy as np
import pandas as pd
import plotly.express as px

from sklearn.decomposition import PCA
from src.rag.vectorstore import load_embeddings, load_faiss_index


def show_vector_space():
    """
    Visualiza embeddings SIN recalcular nada.
    Todo sale del vectorstore.
    """

    embeddings = load_embeddings()
    _, metadata = load_faiss_index()

    if len(embeddings) < 3:
        raise ValueError("Se necesitan al menos 3 embeddings.")

    # PCA
    pca = PCA(n_components=3)
    reduced = pca.fit_transform(embeddings)

    # DataFrame
    df = pd.DataFrame({
        "x": reduced[:, 0],
        "y": reduced[:, 1],
        "z": reduced[:, 2],
        "source_type": [m.get("source_type", "unknown") for m in metadata],
        "source_file": [m.get("source_file", "unknown") for m in metadata],
        "preview": [
            (m.get("text", "")[:120] + "...") for m in metadata
        ],
    })

    # Plot
    fig = px.scatter_3d(
        df,
        x="x",
        y="y",
        z="z",
        color="source_type",
        hover_name="source_file",
        hover_data={"preview": True},
        title="Embedding Space (FAISS)"
    )

    fig.update_traces(marker=dict(size=5))

    return fig