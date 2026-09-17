# n8n Workflows

Orchestration layer for AI processing, qualification triggers, notifications and reminders.

## Required workflows (from TECHNICAL_SPEC)

| Workflow ID                    | Purpose                                      |
|--------------------------------|----------------------------------------------|
| `PRH-LEAD-PROCESS-MESSAGE`     | Process incoming customer message → AI extraction |
| `PRH-LEAD-QUALIFY`             | Trigger deterministic qualification          |
| `PRH-LEAD-NOTIFY-SALES`        | Notify sales team for hot/warm leads         |
| `PRH-FOLLOWUP-REMINDER`        | Scheduled follow-up reminders                |

## Rules

- Workflows must have explicit success and failure paths.
- Idempotent processing (use external message IDs).
- PostgreSQL remains the source of truth; n8n does not own primary data.
- Export workflow JSON into the `workflows/` directory once built.
