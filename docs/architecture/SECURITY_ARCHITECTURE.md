# Security Architecture

## Goals

Protect customer data, sales accounts, credentials, and operational
infrastructure while keeping the MVP simple.

## Controls

### Application

-   Validate all incoming data.
-   Require authentication for sales/admin functions.
-   Apply role-based authorization.
-   Do not trust AI output without schema/business validation.
-   Avoid exposing internal errors to customers.

### Secrets

-   Store secrets in environment variables or an appropriate secret
    store.
-   Never commit `.env`.
-   Maintain `.env.example` without real credentials.

### Database

-   Use a dedicated application database user.
-   Restrict database network access.
-   Use backups.
-   Do not expose PostgreSQL publicly unless there is a documented need.

### Infrastructure

-   Firewall should expose only required ports.
-   Use HTTPS.
-   Keep operating system and containers updated.
-   Restrict SSH access.

### Logging

Do not log passwords, tokens, API keys, or unnecessary personal
information.
