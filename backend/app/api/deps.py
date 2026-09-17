"""Shared FastAPI dependencies (auth, db session, etc.).

Will be expanded in later phases.
"""

from typing import Generator

from app.core.database import SessionLocal


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
