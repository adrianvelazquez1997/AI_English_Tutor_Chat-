# src/chatbot/pipeline.py

from src.rag.retriever import retrieve_context
from src.llm.generator import generate_response
from src.llm.parser import parse_structured_response, extract_text_from_content
from src.multimodal.tts import text_to_speech_file
from src.multimodal.image_gen import generate_image_file
from src.multimodal.filters import is_visual_topic


def run_chat_pipeline(message, history=None) -> dict:
    """
    Ejecuta el flujo completo del chatbot:

    1. Recibe mensaje del usuario
    2. Recupera contexto desde FAISS
    3. Envía mensaje + contexto al LLM
    4. Parsea la respuesta JSON
    5. Genera audio si corresponde
    6. Genera imagen si corresponde
    7. Devuelve texto, audio e imagen
    """

    if history is None:
        history = []

    if isinstance(message, dict):
        message = extract_text_from_content(message.get("content"))

    message = str(message).strip()

    if not message:
        return {
            "text": "",
            "audio": None,
            "image": None,
            "raw": None,
            "parsed": None,
        }

    context = retrieve_context(message)

    raw_answer = generate_response(
        user_message=message,
        retrieved_context=context,
        history=history
    )

    print("\n=== RAW ANSWER ===")
    print(raw_answer)

    parsed = parse_structured_response(raw_answer)

    print("\n=== PARSED ANSWER ===")
    print(parsed)

    final_text = parsed.get("message", raw_answer)

    audio_path = None
    image_path = None

    if parsed.get("generate_audio", False):
        try:
            audio_path = text_to_speech_file(final_text)
            print("AUDIO PATH:", audio_path)
        except Exception as e:
            print("AUDIO ERROR:", repr(e))

    if parsed.get("generate_image", False):
        print("IMAGE TOPIC:", parsed.get("image_topic"))
        print("IMAGE PROMPT:", parsed.get("image_prompt"))

        try:
            if is_visual_topic(parsed.get("image_topic")):
                image_path = generate_image_file(parsed.get("image_prompt"))
                print("IMAGE PATH:", image_path)
            else:
                print("IMAGE BLOCKED BY TOPIC FILTER")
        except Exception as e:
            print("IMAGE ERROR:", repr(e))

    return {
        "text": final_text,
        "audio": audio_path,
        "image": image_path,
        "raw": raw_answer,
        "parsed": parsed,
    }