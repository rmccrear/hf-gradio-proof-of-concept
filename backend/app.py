import gradio as gr

from backend.hf_inference import answer_question


demo = gr.Interface(
    fn=answer_question,
    inputs="text",
    outputs="text",
    api_name="ask_model",
)


if __name__ == "__main__":
    demo.launch()
