# Integrations

## n8n

Purpose: - orchestrate lead processing - call AI services - send
notifications - manage retryable workflows

## AI Provider

Purpose: - intent detection - requirement extraction - response
generation - optional conversation summarization

Requirements: - structured output - output validation - timeout
handling - retry/fallback strategy

## Notifications

Potential channels: - email - team chat - other sales notification
channel

The chosen provider should be isolated behind an integration boundary.

## Google Sheets

Optional reporting/operational synchronization.

Rule:

``` text
PostgreSQL = source of truth
Google Sheets = secondary operational view
```

A sync failure must not cause lead data loss.

## Integration Principles

-   Credentials must be environment variables.
-   External failures must be observable.
-   Integrations should be retryable where safe.
-   Do not make customer data dependent on a secondary integration.
