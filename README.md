# Real Estate Lead Management & AI Qualification System

A practical real-estate lead management system that captures customer
enquiries, understands natural-language requirements, qualifies leads,
stores them in PostgreSQL, automates workflows with n8n, and gives the
sales team a clear follow-up workflow.

## MVP Architecture

``` text
Customer
   ↓
React Frontend
   ↓
FastAPI Backend
   ├── PostgreSQL
   └── n8n
        ├── AI processing
        ├── Lead qualification
        └── Sales notifications
```

## Technology

-   Frontend: React (Vite + TypeScript)
-   Backend: Python + FastAPI
-   Database: PostgreSQL
-   Automation: n8n
-   AI: structured extraction/classification/response generation
-   Deployment: Docker Compose on one VPS
-   Reverse proxy: Nginx

## Core Customer Journey

``` text
Customer message
→ validate
→ understand intent
→ extract requirements
→ validate AI output
→ qualify lead
→ calculate score
→ store/update lead
→ generate response
→ notify sales when required
→ follow up
```

## Repository Structure

``` text
docs/
  product/
  architecture/
  technical/
  features/
  testing/
  operations/
  ADR/
  AGENTS.md
  TASK.md
  IMPLEMENTATION.md
  CONTRIBUTING.md
frontend/
backend/
database/
n8n/
tests/
```

## Source of Truth

Use this order when making decisions:

1.  `docs/product/PRD.md` — why and what
2.  `docs/architecture/SYSTEM_ARCHITECTURE.md` — system structure
3.  `docs/technical/API_SPEC.md` and `DATABASE.md` — contracts
4.  `docs/technical/TECHNICAL_SPEC.md` — implementation approach
5.  Code and tests — implementation evidence
6.  `docs/TASK.md` — what to do next
7.  `docs/IMPLEMENTATION.md` — what has actually been done

## Local Development

The repository is being built incrementally. Do not assume every command
below works until the corresponding implementation task is completed.

### Backend

```bash
cd backend
python -m venv .venv
# activate the environment
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Health: http://localhost:8000/api/v1/health  
Docs: http://localhost:8000/docs

### Frontend

```bash
cd frontend
npm install
npm run dev
```

App: http://localhost:3000

### Docker (all services)

```bash
docker compose up --build
```

### Tests

```bash
pytest
```

## Development Rule

Build the simplest reliable system that solves the business problem. Do
not introduce microservices, Kubernetes, message brokers, multiple
databases, or other infrastructure unless an actual requirement
justifies them.
