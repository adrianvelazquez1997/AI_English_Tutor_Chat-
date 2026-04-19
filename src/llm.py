import os
from openai import OpenAI
from dotenv import load_dotenv
from src.prompts import get_system_prompt, build_user_prompt

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL_GPT = "gpt-4o-mini"


def generate_response(user_message: str, retrieved_context: str, history=None) -> str:
    if history is None:
        history = []

    messages = [{"role": "system", "content": get_system_prompt()}]

    for msg in history:
        role = msg.get("role")
        content = msg.get("content")

        if role in {"user", "assistant"} and content:
            messages.append({
                "role": role,
                "content": str(content)
            })

    messages.append({
        "role": "user",
        "content": build_user_prompt(user_message, retrieved_context)
    })

    response = client.chat.completions.create(
        model=MODEL_GPT,
        messages=messages
    )

    return response.choices[0].message.content