# AGENTS.md

## Purpose

This file defines the operating rules for AI coding agents working in
this repository.

## Before Making Changes

1.  Read `README.md`.
2.  Read the relevant PRD, architecture, technical specification, API
    specification, and database specification.
3.  Read `TASK.md`.
4.  Read `IMPLEMENTATION.md`.
5.  Inspect the existing code before creating new files.
6.  Work on one small task or tightly related task group.

## Engineering Rules

-   Do not silently change the architecture.
-   Do not introduce dependencies without a clear reason.
-   Do not expose secrets or commit `.env`.
-   Do not modify database schema without a migration.
-   Keep business logic out of HTTP route handlers where practical.
-   Keep API contracts consistent with `docs/technical/API_SPEC.md`.
-   PostgreSQL is the primary source of truth.
-   n8n is for orchestration and integrations, not primary data storage.
-   AI interprets/extracts information; deterministic application logic
    owns important business rules.
-   Validate AI output before using it.
-   Preserve the customer's original message.
-   Prefer simple, readable code over premature abstraction.

## Testing Rules

Before declaring a task complete:

1.  Run relevant unit tests.
2.  Run integration tests when the changed component crosses a system
    boundary.
3.  Run end-to-end tests for critical customer journeys when applicable.
4.  Confirm error paths do not corrupt data.
5.  Update `IMPLEMENTATION.md`.
6.  Mark the task in `TASK.md`.

## Do Not

-   Rewrite unrelated modules.
-   Add Kubernetes.
-   Add microservices just for separation.
-   Add a second database without an approved decision.
-   Put secrets in source code.
-   Allow AI output to bypass validation.
-   Mark work complete without tests or a documented reason tests cannot
    yet run.

## Task Completion Format

``` text
Task:
Status:
Implementation:
Files Changed:
Tests:
Notes:
Next Task:
```
