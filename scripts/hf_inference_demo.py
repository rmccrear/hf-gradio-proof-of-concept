from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from backend.hf_inference import DEFAULT_MODEL, SMOLLM2_MODEL, call_hf_inference


def main() -> None:
    prompt = "Explain Gradio Interface in one sentence."
    try:
        response = call_hf_inference(prompt, max_tokens=80, temperature=0.4)
    except RuntimeError as error:
        print(error)
        print("Example: export HF_TOKEN=hf_your_token_here")
        return
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        print("Check your network, HF_TOKEN permissions, HF_MODEL, and HF_PROVIDER.")
        return

    print(f"Model: {DEFAULT_MODEL}")
    print(f"SmolLM2 local/self-hosted model: {SMOLLM2_MODEL}")
    print(f"Prompt: {prompt}")
    print("Response:")
    print(response)


if __name__ == "__main__":
    main()
