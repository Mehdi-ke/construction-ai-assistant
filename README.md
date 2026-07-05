# Construction AI Assistant

**An AI assistant that understands UK construction — contracts, estimating, BIM, tendering, and site management.**

General-purpose AI tools give generic answers to construction questions. They don't know the difference between a JCT Intermediate and a Minor Works contract, they can't interpret an NEC early warning clause in context, and they won't frame a response around how a UK site manager or QS actually works. This tool does.

---

## The Problem It Solves

Construction professionals regularly need fast, accurate answers to technical questions — during a tender review, mid-negotiation on a contract clause, or when a site issue needs a quick commercial steer. Searching through contract documents, RICS guidance, or online forums takes time and rarely gives a direct answer.

This assistant gives immediate, professionally framed responses calibrated to UK construction practice — available from any browser, with no setup required for the end user.

---

## Who Uses It

- **Estimators** — pricing queries, rate build-ups, tender strategy questions
- **QS and commercial managers** — contract clause interpretation, variation procedures, payment notices
- **Site managers** — programme questions, site management decisions, subcontractor management
- **BIM coordinators** — BIM process, coordination workflow, model management questions
- **Anyone in UK construction** who needs a fast, knowledgeable second opinion

---

## Example Exchanges

**User:** What's the difference between a JCT Design and Build contract and a JCT Standard Building Contract?

**Assistant:** The key distinction is risk and design responsibility. Under JCT Design and Build (DB), the contractor takes on both design and construction obligations — the employer issues an Employer's Requirements, and the contractor responds with Contractor's Proposals, taking full responsibility for delivering to that brief. Under the Standard Building Contract (SBC), the design is led by the employer's professional team; the contractor builds to that design but holds no design liability unless specific Contractor's Designed Portions are included...

---

**User:** We've received a payment notice late. What are our options under the Construction Act?

**Assistant:** Under the Housing Grants, Construction and Regeneration Act 1996 (as amended by the Local Democracy, Economic Development and Construction Act 2009), if a payment notice is not issued by the due date, you as the payee can issue a Default Payment Notice specifying the sum you consider due...

---

## Features

- **Full conversation history** — the assistant remembers the context of your conversation, so follow-up questions work naturally
- **Markdown rendering** — responses format properly with headings, bullet points, and structured lists where appropriate
- **UK construction system prompt** — responses are framed around UK contracts, standards, and practice, not generic international content
- **Dark mode interface** — designed for comfortable use on screen during long working sessions
- **New chat button** — clear the session and start a fresh conversation at any point

---

## Technology

- Python / Flask
- Anthropic Claude API (claude-sonnet-4-6)
- Jinja2 templates
- markdown library for response rendering
- python-dotenv

---

## How to Run

```bash
# 1. Clone the repo
git clone https://github.com/Mehdi-ke/construction-ai-assistant
cd construction-ai-assistant

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install flask anthropic python-dotenv markdown

# 4. Add your API key
# Create a .env file in the project root:
ANTHROPIC_API_KEY=your-key-here

# 5. Run the app
python app.py
```

Open your browser at `http://127.0.0.1:5000`

---
