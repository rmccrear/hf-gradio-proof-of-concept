from __future__ import annotations

import gradio as gr

try:
    from backend.hf_inference import DEFAULT_MODEL, SMOLLM2_MODEL, call_hf_inference
except ImportError:
    from hf_inference import DEFAULT_MODEL, SMOLLM2_MODEL, call_hf_inference


def ask_model(prompt: str) -> str:
    try:
        return call_hf_inference(prompt, max_tokens=120, temperature=0.4)
    except Exception as error:
        return f"{type(error).__name__}: {error}"


demo = gr.Interface(
    fn=ask_model,
    inputs=gr.Textbox(
        label="Prompt",
        lines=4,
        value="Explain Gradio Interface in one sentence.",
    ),
    outputs=gr.Textbox(label="Response", lines=8),
    title="Hugging Face Router Demo",
    description=(
        f"Calls {DEFAULT_MODEL} through the Hugging Face OpenAI-compatible router. "
        f"{SMOLLM2_MODEL} is still noted as a local/self-hosted tiny model."
    ),
    api_name="ask_model",
)


if __name__ == "__main__":
    demo.launch()
