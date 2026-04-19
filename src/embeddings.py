import os 
from dotenv import load_dotenv 
from openai import OpenAI

load_dotenv()

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
EMBEDDING_MODEL = "text-embedding-3-small"

def embed_text(text:str) -> list[float]:
    response = openai.embeddings.create(
        model = EMBEDDING_MODEL,
        input = text
    )
    return response.data[0].embedding

def embed_texts(texts:str) -> list[list[float]]:
    response = openai.embeddings.create(
        model=EMBEDDING_MODEL,
        input= texts
    )
    return [item.embedding for item in response.data]

