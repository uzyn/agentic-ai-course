# Prompt Engineering Workshop

A hands-on workshop covering prompt engineering techniques — from basic zero-shot prompting to advanced tool use with Wikipedia and structured outputs.

## Prerequisites

- Python 3.12+
- [`uv`](https://docs.astral.sh/uv/) package manager

## Setup

uv is a a pacakge manager that helps to create virtual env 

How to create virtual .venv 
```
    uv virtualenv .venv
```

### 1. Install `uv`

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or via Homebrew on macOS:

```bash
brew install uv
```

### 2. Install dependencies

```bash
uv sync
```

This installs all required packages (`openai`, `python-dotenv`, `wikipedia`, `ipykernel`) into an isolated virtual environment.

### 3. Configure environment variables

Create a `.env` file in this directory:

**Option A: OpenAI API**

```env
OPENAI_API_KEY=sk-...
```

**Option B: Local LLM server (e.g. [jan.ai](https://jan.ai))**

```env
LOCAL_API_KEY=nusiss
LOCAL_API_URL=http://127.0.0.1:1337/v1
```

### 4. Open the notebook

```bash
uv run jupyter notebook workshop.ipynb
```

### 5. How to activate your virtual .env 

```
source .venv/bin/activate
```

Then select the appropriate client option in the setup cell (OpenAI or local server).

## Workshop Contents

| Part | Topics |
|------|--------|
| Part 1 | Zero-shot, few-shot, role-based, and clear instruction prompting |
| Part 2 | Chain-of-thought, step-by-step reasoning, output formatting |
| Part 3 | System vs user prompts, temperature control, Wikipedia retrieval, combining techniques |

## Assignment

See [`assignment.md`](assignment.md) — build a natural language cafe order processing system that outputs structured JSON.
