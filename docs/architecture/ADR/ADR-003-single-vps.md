# ADR-003: Start With One VPS

## Status

Accepted

## Context

The MVP needs a production environment that is affordable,
understandable, and easy to troubleshoot.

## Decision

Start with one VPS running Docker Compose, Nginx, React, FastAPI,
PostgreSQL, and n8n.

## Consequences

-   Simple operations.
-   Lower infrastructure cost.
-   Easier deployment and troubleshooting.
-   Limited horizontal scaling.
-   Scaling decisions will be revisited when actual requirements appear.
