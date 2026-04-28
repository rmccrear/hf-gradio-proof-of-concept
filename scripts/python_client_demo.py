from __future__ import annotations

import os

from gradio_client import Client


GRADIO_APP_URL = os.environ.get("GRADIO_APP_URL", "http://127.0.0.1:7860")


def main() -> None:
    client = Client(GRADIO_APP_URL)

    print(f"Connected to {GRADIO_APP_URL}")
    print("Available API endpoints:")
    print(client.view_api())

    result = client.predict("Grace", 3, api_name="/greet")
    print("\n/greet result:")
    print(result)


if __name__ == "__main__":
    main()

