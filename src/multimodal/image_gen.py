import uuid
import base64
from openai import OpenAI

from src.config.settings import (
    OPENAI_API_KEY,
    IMAGE_MODEL,
    IMAGE_DIR,
    CHARACTER_IMAGES,
    MARIANNE_NAME,
)

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_image_file(prompt: str) -> str | None:
    if not prompt or not prompt.strip():
        return None

    image_files = [open(path, "rb") for path in CHARACTER_IMAGES]

    try:
        result = client.images.edit(
            model=IMAGE_MODEL,
            image=image_files,
            input_fidelity="high",
            size="1024x1024",
            prompt=f"""
Use the provided images as the SAME CHARACTER reference.

Create a new image that keeps:
- same chibi robot girl identity
- same face, eyes, proportions
- same hairstyle
- same color palette
- same outfit style
- same kawaii illustration style
- same character identity as {MARIANNE_NAME}

Now generate this new scene:
{prompt.strip()}

Important:
- This is the SAME character in a new situation
- Do not redesign the character
- Only change pose / scene / context
"""
        )
    finally:
        for f in image_files:
            f.close()

    image_b64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_b64)

    file_path = IMAGE_DIR / f"image_{uuid.uuid4().hex}.png"

    with open(file_path, "wb") as f:
        f.write(image_bytes)

    return str(file_path)