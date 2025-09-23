# Demo files for Architecting agentic AI solutions course & workshop for NUS-ISS

## Quick Start

### Prerequisites
- Python 3.11+
- uv package manager ([install here](https://docs.astral.sh/uv/getting-started/installation/))
- VS Code with Python and Jupyter extensions (optional)

### Required Environment Variables

Each demo notebook requires specific API keys. Here's a complete list:

| Notebook | Required Environment Variables |
|----------|-------------------------------|
| d1-openai-agents-demo.ipynb | `OPENAI_API_KEY` |
| d2-mcp-demo.ipynb | `ANTHROPIC_API_KEY` |
| d3-smolagents-demo.ipynb | `OPENAI_API_KEY` |
| d4-autogen-demo.ipynb | `OPENAI_API_KEY` |
| d5-crewai-demo.ipynb | `OPENAI_API_KEY`, `SERPER_API_KEY` (optional) |
| d6-langgraph-demo.ipynb | `OPENAI_API_KEY` |

**Optional Environment Variables:**
- `OPENWEATHER_API_KEY` - For real weather data in demos
- `SERPER_API_KEY` - For web search in CrewAI demos
- `TELEGRAM_BOT_TOKEN` - For Telegram integration in workshops

### Setup Instructions

1. **Install dependencies:**
   ```bash
   # From the project root directory
   uv sync
   ```

2. **Set up Jupyter kernel:**
   ```bash
   uv run python -m ipykernel install --user --name agentic-ai-course --display-name "Python (agentic-ai-course)"
   ```

3. **Configure API keys:**
   ```bash
   # Copy environment template and edit with your keys
   cp .env.example .env
   # Edit .env file to add:
   # - OPENAI_API_KEY (for OpenAI demos)
   # - ANTHROPIC_API_KEY (for MCP and Anthropic demos)
   ```

4. **Start Jupyter:**
   ```bash
   # JupyterLab (recommended)
   uv run jupyter lab

   # Or classic notebook interface
   uv run jupyter notebook
   ```

### VS Code Setup
1. Open this folder in VS Code
2. Select interpreter: ⌘⇧P → "Python: Select Interpreter" → choose `.venv/bin/python`
3. Open any `.ipynb` file and select the "Python (agentic-ai-course)" kernel

## Project Structure

- **Demo Notebooks:** `d1-*` through `d6-*` (instructor-led demonstrations)
- **Workshops:** `w1-*` and `w2-*` (hands-on student exercises)
- **Documentation:** `docs/` directory with course materials

## Adding Dependencies

```bash
# Add new packages to the project
uv add package_name

# Update environment
uv sync
```

## Remote Jupyter Server

```bash
# Start server (no browser)
uv run jupyter lab --no-browser --port 8888

# SSH tunnel for remote access
ssh -N -L 8888:localhost:8888 user@server
```

Then open `http://localhost:8888` in your local browser.
