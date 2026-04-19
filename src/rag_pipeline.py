from src.llm import generate_response

def retrieve_context(user_message: str) -> str:
    return "Relevant grammar rule retrieved from your documents."

def run_tutor_pipeline(user_message: str, history=None):
    context = retrieve_context(user_message)

    text_response = generate_response(
        user_message=user_message,
        retrieved_context=context,
        history=history
    )

    return text_response