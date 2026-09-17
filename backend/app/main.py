"""FastAPI application entrypoint."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.health import router as health_router
from app.core.config import settings

app = FastAPI(
    title="Real Estate Lead Management API",
    description="Lead capture, AI qualification, and sales workflow API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS – restrict in production via settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health_router, prefix="/api/v1", tags=["health"])

# Future routers (to be added in later phases):
# app.include_router(leads_router, prefix="/api/v1/leads", tags=["leads"])
# app.include_router(conversations_router, prefix="/api/v1/conversations", tags=["conversations"])
# app.include_router(messages_router, prefix="/api/v1/messages", tags=["messages"])
# app.include_router(follow_ups_router, prefix="/api/v1/follow-ups", tags=["follow-ups"])
# app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])
