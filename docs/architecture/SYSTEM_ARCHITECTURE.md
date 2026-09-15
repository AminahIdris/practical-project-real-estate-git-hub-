# System Architecture

## 1. Architecture Goal

Use a simple modular system that is easy to develop locally, operate on
one VPS, and extend when actual requirements justify it.

## 2. High-Level Architecture

``` text
                    CUSTOMER
                       |
                       v
                 REACT FRONTEND
                       |
                       v
                 FASTAPI BACKEND
                  /           \
                 /             \
                v               v
          POSTGRESQL           N8N
          source of truth       |
                                +--> AI
                                +--> Notifications
                                +--> Optional Sheets sync
```

## 3. Responsibilities

### React

-   Customer interface
-   Sales interface
-   Loading/error states
-   API communication

### FastAPI

-   HTTP API
-   Request validation
-   Authentication boundary
-   Business service boundaries
-   Persistence access
-   Integration entry points

### PostgreSQL

-   Source of truth
-   Leads
-   Conversations
-   Messages
-   Scores
-   Assignments
-   Follow-ups
-   Activities
-   Integration records

### n8n

-   Workflow orchestration
-   External notifications
-   AI orchestration
-   Retryable integrations
-   Optional Google Sheets synchronization

### AI

-   Intent understanding
-   Structured requirement extraction
-   Conversation summarization
-   Response generation

AI does not directly own database writes or deterministic business
rules.

## 4. Request Flow

``` text
Customer
→ React
→ FastAPI
→ store original message
→ trigger n8n
→ retrieve context
→ AI extraction
→ validate AI result
→ update lead
→ calculate qualification
→ generate response
→ persist response
→ return/notify customer
→ notify sales if required
```

## 5. Architectural Style

The initial backend is a modular monolith rather than microservices.

Service boundaries should remain logical inside one deployable backend
until scale or ownership requirements justify separation.

## 6. Data Flow Principles

-   PostgreSQL is authoritative.
-   External systems are integrations, not sources of truth.
-   Original customer messages are immutable records.
-   Derived AI information can be corrected or reprocessed.
-   Score history should be retained where practical.

## 7. Failure Handling

If AI fails: - Keep the original message. - Log the failure. - Do not
write invalid extracted data. - Retry or ask for clarification.

If notification fails: - Keep the lead and score. - Record integration
failure. - Retry when appropriate.

If Google Sheets sync fails: - PostgreSQL data remains authoritative. -
Record the sync failure. - Retry later.

## 8. Security

-   HTTPS in production
-   Secrets in environment configuration
-   Authentication for sales/admin APIs
-   Authorization based on role
-   Input validation
-   No secrets in Git
-   Minimize sensitive data exposure in logs

## 9. Scalability

Start with vertical scaling on one VPS. Introduce additional
infrastructure only when actual workload or reliability requirements
justify it.

## 10. Observability

At minimum: - application logs - workflow execution/error visibility -
health endpoint - database backup status - container status

## 11. Explicit Non-Goals

Do not introduce: - Kubernetes - multiple VPS instances - message
brokers - complex event architecture - microservices - multiple
databases

without an approved requirement and architecture decision.
