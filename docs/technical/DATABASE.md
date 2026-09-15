# Database Specification

## Database

PostgreSQL

## Core Tables

### users

Stores authenticated application users.

Key fields: - id - name - email - password_hash - status - created_at -
updated_at

### roles

Defines user roles.

Examples: - ADMIN - SALES

### leads

Stores customer lead information.

Key fields: - id - customer name - email - phone - intent -
property_type - bedrooms - location - budget_min - budget_max -
transaction_type - timeline - status - source - created_at - updated_at

### conversations

Represents a customer conversation.

Key fields: - id - lead_id - session/external identifier - status -
created_at - updated_at

### messages

Stores individual customer/bot messages.

Key fields: - id - conversation_id - direction - external_message_id -
content - processing_status - created_at

The original customer message must be preserved.

### lead_scores

Stores qualification results.

Key fields: - id - lead_id - score - classification - score_breakdown -
created_at

### lead_assignments

Stores sales assignment history.

### follow_ups

Stores scheduled and completed follow-up actions.

### activities

Stores important lead activity history.

### integration_syncs

Tracks external integration attempts and failures.

## Relationships

``` text
User
  └── Role

Lead
  ├── Conversations
  │     └── Messages
  ├── Lead Scores
  ├── Assignments
  ├── Follow-ups
  └── Activities
```

## Data Integrity

-   Foreign keys required for relationships.
-   Unique constraints where appropriate.
-   Valid enum values.
-   Non-negative bedroom counts.
-   Non-negative monetary amounts.
-   Required fields enforced at the correct layer.
-   Transactions used for multi-record operations that must succeed
    together.

## Migrations

Use Alembic.

Never modify a production schema manually without recording the change
as a migration.

## Retention

Retention rules should be defined before production use based on
business and legal requirements.
