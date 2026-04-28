---
title: Gradio Spaces Tutorial Monorepo
emoji: 🤗
colorFrom: indigo
colorTo: green
sdk: gradio
sdk_version: 6.13.0
app_file: backend/app.py
pinned: false
---

# Gradio + Hugging Face Router Proof Of Concept

This repo contains a minimal end-to-end demo:

- a Gradio backend Space route at `/ask_model`
- a plain HTML webapp that calls that route with `@gradio/client`
- a command-line Python script that calls the same `answer_question(prompt)` function

## Repo Layout

```text
.
├── backend/
│   ├── __init__.py        # Makes backend importable as a Python package
│   ├── app.py             # Gradio Space app exposing /ask_model
│   └── hf_inference.py    # Defines answer_question(prompt)
├── index.html             # Plain HTML webapp for GitHub Pages
├── requirements.txt       # Space and local Python dependencies
└── README.md
```

## Environment

Set a Hugging Face token before calling the model:

```bash
export HF_TOKEN=hf_your_token_here
```

## Local Setup

Create and activate any Python environment you like, then install the dependencies:

```bash
pip install -r requirements.txt
```

## Run The Backend

```bash
python -m backend.app
```

Gradio exposes the regular Python function `answer_question(prompt)` as both a web UI and a named API endpoint, `/ask_model`:

```python
from backend.hf_inference import answer_question

demo = gr.Interface(fn=answer_question, ...)
```

## Run The Same Function From The CLI

```bash
python backend/hf_inference.py
```

The same file that defines `answer_question(prompt)` also has an `if __name__ == "__main__":` block, so you can run it directly from the command line.

## Webapp

Open `index.html` directly or serve it with GitHub Pages. It imports the Gradio JavaScript client from jsDelivr:

```js
import { Client } from "https://cdn.jsdelivr.net/npm/@gradio/client/dist/index.min.js";
```

The webapp calls:

```js
client.predict("/ask_model", { prompt });
```

## Deployment Notes

Hugging Face Spaces reads the README front matter above. The important settings are:

```yaml
sdk: gradio
app_file: backend/app.py
```

Set `HF_TOKEN` as a Space secret before using the deployed app.
