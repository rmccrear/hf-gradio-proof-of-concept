import gradio as gr

try:
    from backend.hf_inference import answer_question
except ImportError:
    from hf_inference import answer_question


demo = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(
        label="Prompt",
        lines=4,
        value="Explain Gradio Interface in one sentence.",
    ),
    outputs=gr.Textbox(label="Response", lines=8),
    title="Hugging Face Router Demo",
    description="A Gradio app that exposes a plain Python function as a web API.",
    api_name="ask_model",
)


if __name__ == "__main__":
    demo.launch()
