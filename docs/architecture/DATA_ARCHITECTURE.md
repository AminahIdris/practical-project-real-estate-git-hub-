# Data Architecture

## Source of Truth

PostgreSQL is the primary source of truth.

## Core Data Flow

``` text
Customer
→ Message
→ Conversation
→ Lead
→ Extracted Requirements
→ Lead Score
→ Assignment
→ Follow-up
→ Activities
```

## Data Principles

-   Use stable IDs.
-   Use foreign keys for relationships.
-   Validate enum-like fields.
-   Use timestamps consistently.
-   Preserve original messages.
-   Keep derived AI fields distinguishable from authoritative
    customer-entered data.
-   Use migrations for schema changes.

## External Synchronization

Google Sheets, if used, is an operational/reporting integration only. It
must not replace PostgreSQL as the source of truth.
