import os

from openai import OpenAI


MODEL = "meta-llama/Llama-3.1-8B-Instruct:novita"


def answer_question(prompt):
    if not os.environ.get("HF_TOKEN"):
        return "Missing HF_TOKEN. Set it before running this app."

    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=os.environ["HF_TOKEN"],
    )

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt},
        ],
        max_tokens=120,
        temperature=0.4,
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    prompt = input("Ask a question: ").strip()
    if not prompt:
        prompt = "Explain Gradio Interface in one sentence."

    response = answer_question(prompt)

    print(f"Model: {MODEL}")
    print(f"Prompt: {prompt}")
    print("Response:")
    print(response)
