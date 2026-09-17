# Backend (FastAPI)

## Structure

```text
backend/
├── app/
│   ├── main.py              # Application entrypoint
│   ├── api/                 # HTTP routers (thin)
│   ├── models/              # SQLAlchemy ORM models
│   ├── schemas/             # Pydantic request/response models
│   ├── services/            # Business logic
│   ├── repositories/        # Data access layer
│   └── core/                # Config, database, security helpers
├── requirements.txt
└── Dockerfile
```

## Local development

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt

# Copy root .env.example → .env and fill values
uvicorn app.main:app --reload --port 8000
```

Health check: http://localhost:8000/api/v1/health  
API docs: http://localhost:8000/docs
