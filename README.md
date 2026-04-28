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

# Gradio + Hugging Face Spaces Tutorial Monorepo

This repo is a small frontend/backend playground for learning:

- Gradio app authoring for Hugging Face Spaces
- the Gradio JavaScript client: https://www.gradio.app/docs/js-client
- the Gradio Python client: https://www.gradio.app/docs/python-client/introduction
- the Gradio Interface API: https://www.gradio.app/docs/gradio/interface

## Repo Layout

```text
.
├── backend/              # Gradio Space app
│   ├── app.py
│   ├── hf_inference.py
│   ├── interface_app.py
│   └── requirements.txt
├── frontend/             # Vite + TypeScript app using @gradio/client
│   ├── package.json
│   └── src/
├── scripts/              # Small client examples and utilities
│   └── python_client_demo.py
└── AGENTS.md             # Contributor and Codex guidance
```

## Backend

Create a local virtual environment and install the backend dependencies:

```bash
python3 -m venv .venv
.venv/bin/pip install -r backend/requirements.txt
```

If you prefer Conda:

```bash
conda create -n spaces-tutorial python=3.11
conda activate spaces-tutorial
pip install -r backend/requirements.txt
```

Run the local Gradio server:

```bash
.venv/bin/python backend/app.py
```

Or, from an active Conda environment:

```bash
python backend/app.py
```

By default, Gradio serves at http://127.0.0.1:7860.

To run the smaller `gr.Interface` tutorial app instead:

```bash
.venv/bin/python backend/interface_app.py
```

From an active Conda environment:

```bash
python backend/interface_app.py
```

## Python Client Tutorial

With the backend running:

```bash
.venv/bin/python scripts/python_client_demo.py
```

From an active Conda environment, use `python scripts/python_client_demo.py`.

The script connects to `http://127.0.0.1:7860`, prints the API info, and calls the named `/greet` endpoint.

## Hugging Face Inference

This repo includes a small helper that calls Hugging Face Inference Providers through the OpenAI-compatible router with `meta-llama/Llama-3.1-8B-Instruct:novita` by default.

`HuggingFaceTB/SmolLM2-135M-Instruct` is a great tiny tutorial model, but it is not currently deployed by Hugging Face Inference Providers. Use it locally with Transformers or deploy it yourself before calling it through an inference endpoint.

Set your token first:

```bash
export HF_TOKEN=hf_your_token_here
```

Optional model/provider override:

```bash
export HF_MODEL=meta-llama/Llama-3.1-8B-Instruct:novita
```

Or keep the provider separate:

```bash
export HF_MODEL=meta-llama/Llama-3.1-8B-Instruct
export HF_PROVIDER=novita
```

Run the direct Python demo:

```bash
.venv/bin/python scripts/hf_inference_demo.py
```

From an active Conda environment, use `python scripts/hf_inference_demo.py`.

The main Gradio app also exposes this as the named `/hf_inference` endpoint in the "HF Inference" tab.

## JavaScript Client Tutorial

Install frontend dependencies:

```bash
cd frontend
npm install
```

Run the frontend:

```bash
npm run dev
```

The frontend reads `VITE_GRADIO_APP_URL` and defaults to `http://127.0.0.1:7860`.

## Deploying To Hugging Face Spaces

The README front matter points Spaces at `backend/app.py`, so the Blocks-based Gradio backend is the deployable Space app. `backend/interface_app.py` is a focused companion for the Interface tutorial. The frontend is intentionally separate for local experiments with the JS client.
