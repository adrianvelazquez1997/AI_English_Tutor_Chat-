import gradio as gr
from src.config.settings import (
    MARIANNE_NAME,
    GRADIO_SERVER_NAME,
    GRADIO_SERVER_PORT,
)

from src.chatbot.pipeline import run_chat_pipeline
from src.chatbot.intro import introduce_marianne
from src.rag.retriever import initialize_retriever
from src.visualization.embedding_viz import show_vector_space

initialize_retriever()

def respond(message, history):
    if history is None:
        history = []

    message = str(message).strip()

    if not message:
        return history, "", None, None

    result = run_chat_pipeline(message, history)

    history = history + [
        {"role": "user", "content": message},
        {"role": "assistant", "content": result["text"]}
    ]

    return history, "", result["image"], result["audio"]

    text = run_tutor_pipeline(message, history)

    history = history + [
        {"role": "user", "content": message},
        {"role": "assistant", "content": text},
    ]

    return history, history

with gr.Blocks() as demo:
    gr.Markdown("## AI English Tutor Chat")

    chatbot = gr.Chatbot(label="Chat")
    msg = gr.Textbox(label="Write in English")
    state = gr.State([])

    msg.submit(
        chat_fn,
        inputs=[msg, state],
        outputs=[chatbot, state]
    )

demo.launch(server_name="0.0.0.0", server_port=7860)