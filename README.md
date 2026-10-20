
# ResearchFlow AI
### Multi-Agent Research & Report Writer

## 1. Project Overview

ResearchFlow AI is an AI-powered research and report-writing application developed for the Module 27 Capstone Project.

Users enter a research topic, and the application retrieves web sources, analyses evidence, generates a structured report, reviews the draft, and provides a downloadable PDF.

## 2. Main Features

- Research topic submission through a web interface
- Web research using Tavily
- Four specialised AI agents: Researcher, Analyst, Writer and Editor
- Language model access through OpenRouter
- Structured report generation
- Source links and references
- PDF report download
- FastAPI backend and Streamlit frontend

## 3. Technology Stack

- Python 3.13
- Streamlit
- FastAPI
- CrewAI
- OpenRouter API
- Tavily Search API
- ReportLab
- Git and GitHub

## 4. Project Structure

- `frontend/app.py` — Streamlit user interface
- `backend/main.py` — FastAPI endpoints
- `backend/research.py` — Web search and source collection
- `backend/agents.py` — AI agent definitions
- `backend/tasks.py` — Agent tasks and workflow
- `backend/pdf_generator.py` — PDF generation
- `docs/project_proposal.md` — Project proposal
- `docs/final_report.md` — Final report template
- `requirements.txt` — Python dependencies
- `.env.example` — Example environment configuration

## 5. Requirements

- Python 3.13
- An OpenRouter API key
- A Tavily API key
- Internet access

Free model availability, request limits and provider capacity may vary. API providers may change their terms and limits.

## 6. Local Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/AnikSharker01/ResearchFlow-AI.git
cd ResearchFlow-AI
```

### Step 2: Create a virtual environment

```bash
py -3.13 -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Configure environment variables

Copy the example file:

```powershell
Copy-Item .env.example .env
```

Add your own keys and model configuration to `.env`:

```text
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_MODEL=minimax/minimax-m3.1-flash:free
TAVILY_API_KEY=your_tavily_api_key
BACKEND_URL=http://127.0.0.1:8000
```

Use a currently available model ID from OpenRouter if the example model is unavailable.

Never commit or publish your real `.env` file or API keys.

### Step 5: Start the backend

```bash
python -m uvicorn backend.main:app --reload
```

Backend API documentation:

http://127.0.0.1:8000/docs

### Step 6: Start the frontend

Open a second terminal, activate the virtual environment, and run:

```bash
python -m streamlit run frontend/app.py
```

Open the local URL shown in the terminal, usually:

http://localhost:8501

## 7. AI Workflow

1. Researcher: reviews retrieved web sources.
2. Analyst: identifies themes, evidence gaps and limitations.
3. Writer: produces a structured report.
4. Editor: reviews clarity, consistency and source support.

## 8. PDF Reports

The application provides a PDF download endpoint that converts the generated report and retrieved source links into a PDF document.

## 9. Limitations

- AI-generated information may be inaccurate.
- Search snippets do not always provide enough evidence to verify a claim.
- Source quality and currency vary.
- Free model access and rate limits may change.
- Generated reports require human review before academic or professional use.

## 10. Project Status

The project has a working local prototype. Online deployment and final evaluation should be completed and documented before final submission.
