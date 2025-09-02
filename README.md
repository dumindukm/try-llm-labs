# try-llm-labs

This project is designed to help you learn about Large Language Models (LLMs) and experiment with their capabilities.

## Package Management

The project uses [UV](https://github.com/astral-sh/uv) as the package manager for fast and efficient dependency management.

## Goals

- Explore and understand LLM concepts
- Implement sample code and experiments
- Manage dependencies using UV

## Getting Started

1. Install UV following the [official instructions](https://github.com/astral-sh/uv).
2. Clone this repository.
3. Use UV to install dependencies:

    ```bash
    uv sync
    ```
4. Set below enviorment variables. you can create .env file
    - AZURE_OPENAI_API_KEY
    - ENDPOINT_URL
    - DEPLOYMENT_NAME
## Helpful commands
- uv init lab1
- uv run main.py  (change to directory as needed)
- .venv\Scripts\activate

- uv add --dev ipykernel (Add ipykernel as a dev dependency.)
