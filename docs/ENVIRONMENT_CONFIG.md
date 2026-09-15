# Environment Configuration

## Purpose

Define configuration required by local and production environments.

## Rules

-   Never commit real secrets.
-   `.env.example` contains placeholders only.
-   Production secrets must be supplied securely.

## Application

Expected categories:

``` text
APP_ENV
APP_SECRET_KEY
DATABASE_URL
API_BASE_URL
FRONTEND_BASE_URL
```

## AI

``` text
AI_PROVIDER
AI_API_KEY
AI_MODEL
```

## n8n

``` text
N8N_BASE_URL
N8N_WEBHOOK_SECRET
```

## Notifications

Provider-specific credentials should be added only when the integration
is implemented.

## Database

``` text
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_PORT
```

Exact variable names must remain synchronized with the implementation
and deployment files.
