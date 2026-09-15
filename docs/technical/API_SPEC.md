# API Specification

## Base URL

``` text
/api/v1
```

## General Rules

-   JSON request/response bodies.
-   Versioned API.
-   Validate all input.
-   Return meaningful HTTP status codes.
-   Do not expose internal stack traces.

## Health

### GET `/health`

Response:

``` json
{
  "status": "ok"
}
```

Expected status: `200`.

## Leads

### POST `/leads`

Creates a lead.

Example request:

``` json
{
  "name": "John Doe",
  "phone": "08000000000",
  "email": "john@example.com",
  "property_type": "APARTMENT",
  "bedrooms": 3,
  "location": "Lekki",
  "budget_max": 80000000,
  "transaction_type": "BUY"
}
```

### GET `/leads`

Returns leads.

Initial query capabilities: - pagination - search - filtering - sorting

### GET `/leads/{id}`

Returns one lead.

### PATCH `/leads/{id}`

Updates allowed lead fields such as status, assignment, or extracted
requirements.

## Conversations

### POST `/conversations`

Creates a conversation associated with a lead/customer context.

### GET `/conversations/{id}`

Returns conversation metadata.

### GET `/conversations/{id}/messages`

Returns messages in chronological order.

## Messages

### POST `/messages`

Example:

``` json
{
  "conversation_id": "conversation-id",
  "content": "I want a 3-bedroom apartment in Lekki."
}
```

The original message must be persisted before downstream processing is
considered successful.

## Qualification

### POST `/leads/{id}/qualify`

Calculates/recalculates the lead score using deterministic application
rules.

## Follow-ups

### POST `/follow-ups`

Creates a follow-up.

### GET `/follow-ups`

Lists follow-ups.

### PATCH `/follow-ups/{id}`

Updates follow-up status or scheduling information.

## Error Shape

Use a consistent error structure:

``` json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request.",
    "details": {}
  }
}
```

## Idempotency

Message processing should support an external/customer message
identifier when available so duplicate delivery does not create
duplicate processing.

## Authentication

Sales/admin endpoints require authentication. Exact authentication
implementation is defined in the technical specification and must remain
consistent across frontend and backend.
