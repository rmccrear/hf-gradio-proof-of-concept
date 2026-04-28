from __future__ import annotations

import os

from openai import OpenAI


HF_ROUTER_BASE_URL = "https://router.huggingface.co/v1"
DEFAULT_MODEL = "meta-llama/Llama-3.1-8B-Instruct:novita"
SMOLLM2_MODEL = "HuggingFaceTB/SmolLM2-135M-Instruct"
DEFAULT_SYSTEM_PROMPT = (
    "You are a concise assistant helping someone learn Gradio and "
    "Hugging Face Spaces."
)


def get_hf_token() -> str:
    token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACEHUB_API_TOKEN")
    if not token:
        raise RuntimeError(
            "Missing Hugging Face token. Set HF_TOKEN in your environment."
        )
    return token


def call_hf_inference(
    prompt: str,
    *,
    system_prompt: str = DEFAULT_SYSTEM_PROMPT,
    model: str | None = None,
    max_tokens: int = 120,
    temperature: float = 0.7,
) -> str:
    """Call Hugging Face Inference Providers through the OpenAI-compatible router."""
    cleaned_prompt = prompt.strip()
    if not cleaned_prompt:
        raise ValueError("Prompt cannot be empty.")

    selected_model = model or os.environ.get("HF_MODEL") or DEFAULT_MODEL
    provider = os.environ.get("HF_PROVIDER")
    if provider and ":" not in selected_model:
        selected_model = f"{selected_model}:{provider}"

    client = OpenAI(
        base_url=HF_ROUTER_BASE_URL,
        api_key=get_hf_token(),
        timeout=60,
    )

    completion = client.chat.completions.create(
        model=selected_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": cleaned_prompt},
        ],
        max_tokens=max(1, min(max_tokens, 512)),
        temperature=max(0.0, min(temperature, 2.0)),
    )

    return completion.choices[0].message.content or ""


def call_hf_inference_for_gradio(
    prompt: str,
    max_tokens: int,
    temperature: float,
) -> str:
    try:
        return call_hf_inference(
            prompt,
            max_tokens=max_tokens,
            temperature=temperature,
        )
    except Exception as error:
        return f"{type(error).__name__}: {error}"
