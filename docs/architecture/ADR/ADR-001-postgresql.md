# ADR-001: Use PostgreSQL as the Primary Database

## Status

Accepted

## Context

The application needs relational data, transactions, foreign keys, and
consistent lead/conversation relationships.

## Decision

Use PostgreSQL as the primary source of truth.

## Alternatives

-   MongoDB
-   MySQL
-   Google Sheets as primary storage

## Why

-   Strong relational model
-   Transactions
-   Referential integrity
-   Mature ecosystem
-   Suitable for the MVP and future growth

## Consequences

-   Schema migrations are required.
-   Database backup and recovery must be managed.
-   Reporting integrations should read from or synchronize with
    PostgreSQL rather than replace it.
