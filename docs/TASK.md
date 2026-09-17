# Real Estate Lead Management --- Task Tracker

## Status Legend

-   ⬜ Not Started
-   🟡 In Progress
-   🟢 Completed
-   🔴 Blocked
-   ⏸️ On Hold

## Roadmap

``` text
Documentation
  ↓
Project Foundation
  ↓
Database
  ↓
FastAPI Backend
  ↓
React Frontend
  ↓
n8n Automation
  ↓
AI Processing
  ↓
Lead Qualification
  ↓
Sales Dashboard
  ↓
Testing
  ↓
VPS Deployment
  ↓
MVP Complete
```

## Phase 1 --- Documentation

-   [🟢] PRD
-   [🟢] System architecture
-   [🟢] API specification
-   [🟢] Database specification
-   [🟢] Technical specification
-   [🟢] README
-   [🟢] AGENTS.md
-   [🟢] Testing strategy
-   [🟢] Deployment specification
-   [🟢] Operations runbook
-   [🟢] ADRs
-   [🟢] Implementation tracker

## Phase 2 --- Project Foundation

-   [🟢] Create Git repository
-   [🟢] Create directory structure
-   [🟢] Add `.gitignore`
-   [🟢] Add `.env.example`
-   [🟢] Add Docker Compose
-   [🟢] Configure backend environment (scaffold + config)
-   [🟢] Configure frontend environment (Vite + React scaffold)

## Phase 3 --- Database

-   [ ] Configure PostgreSQL connection
-   [ ] Create SQLAlchemy models
-   [ ] Configure Alembic
-   [ ] Create initial migration
-   [ ] Create seed data
-   [ ] Add database tests

## Phase 4 --- Backend

-   [🟢] Implement health endpoint (scaffold)
-   [ ] Implement lead creation
-   [ ] Implement lead listing
-   [ ] Implement lead detail
-   [ ] Implement lead update
-   [ ] Implement conversations
-   [ ] Implement messages
-   [ ] Implement qualification endpoint
-   [ ] Implement follow-ups
-   [ ] Add API tests

## Phase 5 --- Frontend

-   [🟢] Create React application (scaffold)
-   [ ] Create customer enquiry/chat interface
-   [ ] Create sales login
-   [ ] Create lead list
-   [ ] Create lead detail
-   [ ] Create conversation view
-   [ ] Create qualification display
-   [ ] Create follow-up interface
-   [ ] Add frontend tests

## Phase 6 --- n8n

-   [ ] Build `PRH-LEAD-PROCESS-MESSAGE`
-   [ ] Build `PRH-LEAD-QUALIFY`
-   [ ] Build `PRH-LEAD-NOTIFY-SALES`
-   [ ] Build `PRH-FOLLOWUP-REMINDER`
-   [ ] Add failure handling
-   [ ] Add duplicate protection
-   [ ] Export workflows to repository

## Phase 7 --- AI

-   [ ] Define structured extraction schema
-   [ ] Define prompt
-   [ ] Validate AI output
-   [ ] Add realistic test cases
-   [ ] Add fallback behavior
-   [ ] Add response generation

## Phase 8 --- Qualification

-   [ ] Implement deterministic scoring
-   [ ] Test score boundaries
-   [ ] Implement lead classification
-   [ ] Implement requalification
-   [ ] Store score history

## Phase 9 --- Testing

-   [ ] Backend tests
-   [ ] Database tests
-   [ ] AI tests
-   [ ] n8n workflow tests
-   [ ] Frontend tests
-   [ ] End-to-end customer journey
-   [ ] Failure-path testing

## Phase 10 --- VPS

-   [ ] Provision VPS
-   [ ] Install Docker
-   [ ] Configure firewall
-   [ ] Configure domain
-   [ ] Configure Nginx
-   [ ] Configure HTTPS
-   [ ] Configure production environment
-   [ ] Run migrations
-   [ ] Configure PostgreSQL backups
-   [ ] Deploy application
-   [ ] Test restart/recovery
-   [ ] Verify complete customer journey

## MVP Definition of Done

A customer can send a message, the system can understand and extract
requirements, create/update a lead, calculate a qualification score,
store the data, generate a response, and notify the sales team when
required.

The sales team can view the lead, conversation, extracted requirements,
score, classification, status, assignment, and follow-up.

## Agentic Development Rule

Read the relevant documentation first. Select one small task. Implement
only that scope. Test it. Update `IMPLEMENTATION.md`. Mark the task
here. Do not silently redesign the system.

## Task Completion

``` text
Task:
Status:
Implementation:
Files Changed:
Tests:
Notes:
Next Task:
```
