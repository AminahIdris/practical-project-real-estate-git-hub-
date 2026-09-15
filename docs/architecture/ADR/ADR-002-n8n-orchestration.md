# ADR-002: Use n8n for Workflow Orchestration

## Status

Accepted

## Context

The product needs integrations, AI calls, notifications, retries, and
workflow visibility.

## Decision

Use n8n for workflow orchestration and external integrations.

## Boundaries

FastAPI owns application/API boundaries and PostgreSQL owns persisted
business data. n8n does not become the primary database.

## Consequences

-   Workflows are visible and easy to modify.
-   Integration logic is separated from core application logic.
-   Workflow exports should be version-controlled.
-   Important business rules should remain deterministic and testable
    outside AI prompts.
