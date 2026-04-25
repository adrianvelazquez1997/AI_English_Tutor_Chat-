import json
def extract_text_from_content(content):
    if content is None:
        return None

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        texts = []

        for block in content:
            if isinstance(block, dict):
                if block.get("type") == "text":
                    texts.append(block.get("text", ""))
                elif "text" in block:
                    texts.append(block.get("text", ""))

        return "\n".join(texts).strip()

    return str(content)


def parse_structured_response(raw_text: str) -> dict:
    fallback = {
        "type": "chat",
        "message": raw_text,
        "generate_audio": True,
        "generate_image": False,
        "image_topic": None,
        "image_prompt": None,
    }

    try:
        data = json.loads(raw_text)
    except Exception:
        return fallback

    return {
        "type": data.get("type", "chat"),
        "message": data.get("message", raw_text),
        "generate_audio": bool(data.get("generate_audio", False)),
        "generate_image": bool(data.get("generate_image", False)),
        "image_topic": data.get("image_topic"),
        "image_prompt": data.get("image_prompt"),
    }