# Technical Specification

## 1. Backend Structure

Recommended backend modules:

``` text
backend/app/
├── main.py
├── api/
├── models/
├── schemas/
├── services/
├── repositories/
└── core/
```

Keep HTTP routing thin. Put reusable business logic in services.

## 2. Lead Processing

``` text
Receive message
→ persist message
→ identify/create lead context
→ trigger processing
→ AI extraction
→ schema validation
→ business validation
→ update lead
→ qualification
→ response generation
→ persist response
```

## 3. AI Boundary

AI receives relevant conversation context and returns structured data.

Example:

``` json
{
  "intent": "BUY",
  "property_type": "APARTMENT",
  "bedrooms": 3,
  "location": "Lekki",
  "budget_max": 80000000,
  "timeline": "WITHIN_3_MONTHS",
  "confidence": 0.94
}
```

Missing values must remain missing. The AI must not invent budget,
location, bedrooms, or other facts.

## 4. AI Output Validation

``` text
AI
↓
Structured JSON
↓
Schema validation
↓
Business validation
↓
Use result
```

Invalid results must not be stored blindly.

## 5. Qualification

The qualification service receives validated lead information and
calculates a deterministic score.

Initial model:

``` text
Intent             20
Property need      15
Location           15
Budget             20
Timeline           20
Contact            10
----------------------
Total              100
```

Classification:

``` text
80–100 HOT
60–79  WARM
30–59  COLD
0–29   UNQUALIFIED
```

## 6. Duplicate Processing

Where an external message ID exists, store it and enforce idempotent
processing.

Repeated delivery should not create: - duplicate messages - duplicate
leads - duplicate notifications

## 7. Error Handling

Errors should be categorized as: - validation -
authentication/authorization - not found - database - AI - workflow -
notification - external integration

Errors should be logged with enough context for troubleshooting without
leaking secrets.

## 8. Frontend

The React application should contain:

``` text
Customer enquiry/chat
Sales login
Lead list
Lead detail
Conversation
Qualification
Follow-ups
```

API calls should go through a consistent API client layer.

## 9. n8n

Workflows:

-   `PRH-LEAD-PROCESS-MESSAGE`
-   `PRH-LEAD-QUALIFY`
-   `PRH-LEAD-NOTIFY-SALES`
-   `PRH-FOLLOWUP-REMINDER`

Workflows should have explicit success and failure paths.

## 10. Google Sheets

If used, Google Sheets is an optional operational/reporting integration.
PostgreSQL remains authoritative.

## 11. Implementation Order

1.  Environment configuration
2.  Backend skeleton
3.  PostgreSQL connection
4.  Models
5.  Migrations
6.  Health endpoint
7.  Lead API
8.  Conversation/message API
9.  React customer interface
10. n8n processing workflow
11. AI integration
12. Qualification
13. Sales dashboard
14. Testing
15. VPS deployment
