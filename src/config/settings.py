import os 
from pathlib import Path 
from dotenv import load_dotenv 

load_dotenv()

# BASE PATHS
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
CHEAT_SHEETS_DIR = DATA_DIR / "cheat_sheets"
BOOKS_DIR = DATA_DIR / "books"

VECTORSTORE_DIR = BASE_DIR / "vectorstore"
AUDIO_DIR = BASE_DIR / "audio_outputs"
IMAGE_DIR = BASE_DIR / "image_outputs"
CHARACTER_DIR = BASE_DIR / "assets"

AUDIO_DIR.mkdir(parents=True, exist_ok=True)
IMAGE_DIR.mkdir(parents=True, exist_ok=True)
VECTORSTORE_DIR.mkdir(parents=True, exist_ok=True)

# API KEYS
OPENAI_API_KEY = os.getenv("")

if not OPENAI_API_KEY: 
    raise ValueError("OPENAI_API_KEY no está definida en el archivo .env")

# OPENAI MODELS
MODEL_GPT = "gpt-4o-mini"
EMBEDDING_MODEL = "text-embedding-3-small"
TTS_MODEL = "gpt-4o-mini-tts"
TTS_VOICE = "nova"
IMAGE_MODEL = "gpt-image-1"

# RAG CONFIG
CHUNK_SIZE = 700
CHUNK_OVERLAP = 120
TOP_K = 3

# MARIANNE CONFIG 
MARIANNE_NAME = "Marianne_V2"

MARIANNE_AVATAR = CHARACTER_DIR / "Marianne_V2_1.png"

CHARACTER_IMAGES = [
    CHARACTER_DIR / "Marianne_V2_1.png",
    CHARACTER_DIR / "Marianne_V2_2.png",
    CHARACTER_DIR / "Marianne_V2_3.png",
]

MARIANNE_PROFILE_TEXT = """
Hello! I'm Marianne_V2 👩‍🏫🤖

I'm your English AI tutor.

My fictional background:
- English tutor specialized in grammar, conversation, and vocabulary
- Experienced in helping students improve fluency and confidence
- Focused on clear explanations, natural conversation, and visual learning

What I can help you with:
- Correct your English
- Explain grammar in a simple way
- Practice conversation
- Show visual examples for specific topics

Let's start learning together!
""".strip()

# TOPIC FILTER FOR THE IMAGE
VISUAL_TOPICS = {
    "animal", "animals", "food", "place", "places", "city", "country",
    "planet", "planets", "space", "solar system", "weather", "house",
    "kitchen", "body", "body parts", "transport", "vehicle", "vehicles",
    "job", "jobs", "clothes", "colors", "shapes", "nature", "jungle",
    "ocean", "mountain", "volcano", "school objects", "fruits", "vegetables"
}
