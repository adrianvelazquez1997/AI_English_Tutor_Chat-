from openai import OpenAI
from src.config.settings import OPENAI_API_KEY, MODEL_GPT
from src.llm.prompts import get_system_prompt, build_user_prompt
from src.llm.parser import extract_text_from_content


client = OpenAI(api_key=OPENAI_API_KEY)


def generate_response(user_message: str, retrieved_context: str, history=None) -> str:

    if history is None:
        history = []

    messages = [{"role": "system", "content": get_system_prompt()}]

    for item in history:
        if isinstance(item, dict):
            role = item.get("role")
            content = extract_text_from_content(item.get("content"))

            if role in {"user", "assistant"} and content:
                messages.append({"role": role, "content": content})

    messages.append({
        "role": "user",
        "content": build_user_prompt(user_message, retrieved_context)
    })

    response = client.chat.completions.create(
        model=MODEL_GPT,
        messages=messages,
        temperature=0.4
    )

    return response.choices[0].message.content