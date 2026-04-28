from __future__ import annotations

import gradio as gr


def summarize_learning_goal(topic: str, hours: int) -> str:
    cleaned_topic = topic.strip() or "Gradio"
    safe_hours = max(1, min(hours, 20))
    return (
        f"Learning goal: spend {safe_hours} focused hour(s) building a "
        f"small {cleaned_topic} demo, then call it from a client."
    )


demo = gr.Interface(
    fn=summarize_learning_goal,
    inputs=[
        gr.Textbox(label="Topic", value="Gradio Interface"),
        gr.Slider(label="Study hours", minimum=1, maximum=20, value=3, step=1),
    ],
    outputs=gr.Textbox(label="Plan"),
    title="Interface Tutorial App",
    description="A minimal gr.Interface example with a named API endpoint.",
    examples=[
        ["Gradio Interface", 2],
        ["Hugging Face Spaces", 4],
        ["Gradio clients", 3],
    ],
    api_name="learning_goal",
)


if __name__ == "__main__":
    demo.launch()

