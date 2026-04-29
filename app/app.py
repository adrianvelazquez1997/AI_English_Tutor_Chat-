import gradio as gr
from src.config.settings import (MARIANNE_NAME)
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

with gr.Blocks() as demo:
    gr.Markdown(f"# {MARIANNE_NAME} - English Tutor AI")

    with gr.Tab("Chat"):
        with gr.Row():
            with gr.Column(scale=3):
                chatbot = gr.Chatbot(
                    label="Chat",
                    height=500,
                    type="messages"
                )

                msg = gr.Textbox(
                    label="Write here",
                    placeholder="Type your message..."
                )

                with gr.Row():
                    start_btn = gr.Button(f"Introduce {MARIANNE_NAME}")
                    send = gr.Button("Send")

            with gr.Column(scale=2):
                image_output = gr.Image(
                    label="Visual aid",
                    value=None,
                    height=500
                )

        audio_output = gr.Audio(
            label="Voice",
            visible=False,
            autoplay=True
        )

        start_btn.click(
            fn=introduce_marianne,
            outputs=[chatbot, image_output, audio_output]
        )

        send.click(
            fn=respond,
            inputs=[msg, chatbot],
            outputs=[chatbot, msg, image_output, audio_output]
        )

        msg.submit(
            fn=respond,
            inputs=[msg, chatbot],
            outputs=[chatbot, msg, image_output, audio_output]
        )

    with gr.Tab("Vector Space"):
        btn = gr.Button("Visualize Embedding Space")
        plot = gr.Plot()

        btn.click(
            fn=show_vector_space,
            outputs=plot
        )

demo.launch(
    server_name="0.0.0.0",
    server_port=7860,
    share=True
    )