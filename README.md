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

With a local virtual environment:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

With Conda:

```bash
conda create -n spaces-tutorial python=3.11
conda activate spaces-tutorial
pip install -r requirements.txt
```

## Run The Backend

```bash
.venv/bin/python -m backend.app
```

From an active Conda environment:

```bash
python -m backend.app
```

The app exposes the named Gradio API endpoint `/ask_model`.

The key idea is that Gradio exposes a regular Python function:

```python
from backend.hf_inference import answer_question

demo = gr.Interface(fn=answer_question, ...)
```

Running the app with `-m backend.app` keeps imports simple because Python treats `backend` as a package.
That means `backend/app.py` can use one normal import, with no direct-file fallback:

```python
from backend.hf_inference import answer_question
```

## Run The Same Function From The CLI

```bash
.venv/bin/python backend/hf_inference.py
```

From an active Conda environment:

```bash
python backend/hf_inference.py
```

That file has an `if __name__ == "__main__":` block, so it can be imported by Gradio or run directly as a script.

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
