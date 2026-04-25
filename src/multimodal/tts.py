import uuid
from openai import OpenAI

from src.config.settings import (
    OPENAI_API_KEY,
    TTS_MODEL,
    TTS_VOICE,
    AUDIO_DIR,
)

client = OpenAI(api_key=OPENAI_API_KEY)


def text_to_speech_file(text: str) -> str | None:
    clean_text = text.strip()

    if not clean_text:
        return None

    file_path = AUDIO_DIR / f"audio_{uuid.uuid4().hex}.mp3"

    audio = client.audio.speech.create(
        model=TTS_MODEL,
        voice=TTS_VOICE,
        input=clean_text[:1000],
    )

    with open(file_path, "wb") as f:
        f.write(audio.read())

    return str(file_path)