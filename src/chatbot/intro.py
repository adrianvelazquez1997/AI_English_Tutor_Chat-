from src.config.settings import MARIANNE_PROFILE_TEXT, MARIANNE_AVATAR
from src.multimodal.tts import text_to_speech_file


def introduce_marianne():
    history = [
        {"role": "assistant", "content": MARIANNE_PROFILE_TEXT}
    ]

    image_path = str(MARIANNE_AVATAR)

    audio_path = None

    try:
        audio_path = text_to_speech_file(MARIANNE_PROFILE_TEXT)
    except Exception as e:
        print("INTRO AUDIO ERROR:", repr(e))

    return history, image_path, audio_path