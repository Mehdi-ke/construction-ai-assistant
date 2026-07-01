# Construction AI Assistant

A Flask web app that lets you chat with an AI assistant specialising in UK construction. Ask questions about estimating, tendering, contracts, BIM, and site management — and get instant professional responses.

## Live Demo
[construction-ai-assistant-production.up.railway.app](https://construction-ai-assistant-production.up.railway.app)

## What It Does

- Chat interface built with Flask and Jinja2 templates
- Sends your question to the Anthropic Claude API
- Returns formatted responses rendered as proper HTML
- Dark mode developer aesthetic

## Technology

- Python
- Flask
- Anthropic Claude API (claude-sonnet-4-6)
- Jinja2 templates
- python-dotenv for secure API key management
- markdown library for response formatting

## How to Run Locally

1. Clone the repo
2. Create and activate a virtual environment:
```bash
   python -m venv venv
   venv\Scripts\activate
```
3. Install dependencies:
```bash
   pip install flask anthropic python-dotenv markdown
```

4. Create a `.env` file with your Anthropic API key:

   ANTHROPIC_API_KEY=your-key-here

6. Run the app:
```bash
   python app.py
```
6. Open your browser at `http://127.0.0.1:5000`
