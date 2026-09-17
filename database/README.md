# Database

PostgreSQL is the single source of truth.

## Layout

```text
database/
├── migrations/     # Alembic migration scripts
└── seed/           # Seed data scripts
```

## Core tables (see docs/technical/DATABASE.md)

- users, roles
- leads
- conversations, messages
- lead_scores, lead_assignments
- follow_ups, activities
- integration_syncs

## Migrations

Alembic will be configured in Phase 3. Never change the production schema manually.
