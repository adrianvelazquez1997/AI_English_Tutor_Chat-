import gradio as gr
from src.rag_pipeline import run_tutor_pipeline

def chat_fn(message, history):
    if history is None:
        history = []

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