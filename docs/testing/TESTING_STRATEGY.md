# Testing Strategy

## Goal

Test the important customer and sales paths without creating unnecessary
complexity.

## Testing Areas

1.  Backend/API
2.  Database
3.  AI
4.  n8n workflows
5.  Frontend
6.  End-to-end

## Backend

Test: - health - valid lead creation - invalid input - lead retrieval -
lead update - conversations - messages - duplicate messages

Example invalid input:

``` json
{
  "name": "",
  "bedrooms": -2
}
```

Expected: `400` or `422`.

## AI

Test realistic examples:

### Complete buying enquiry

Expected extraction: - BUY - APARTMENT - 3 bedrooms - Lekki - ₦80M -
within 3 months

### Rental

``` text
I need a 2 bedroom apartment to rent in Ikeja.
```

Expected: - RENT - APARTMENT - 2 - Ikeja

### Land

``` text
I'm looking for land around Ibadan below ₦20 million.
```

Expected: - LAND - Ibadan - budget max ₦20M

### Incomplete

``` text
I want to buy a house in Lekki.
```

The system should ask for missing information.

### Unclear

``` text
I need something nice around there.
```

The system must not invent requirements.

## Qualification

Test deterministic scoring independently.

Boundary tests:

``` text
80 → HOT
79 → WARM
60 → WARM
59 → COLD
30 → COLD
29 → UNQUALIFIED
```

## n8n

Test: - successful workflow - AI failure - notification failure -
duplicate message - Google Sheets failure

Failures must not corrupt or delete PostgreSQL data.

## Frontend

Test: - chat loads - message sends - loading state - bot response - API
failure - empty message - lead list - lead detail - follow-up creation

## End-to-End

At least one realistic journey must pass:

``` text
Customer message
→ FastAPI
→ message stored
→ AI extraction
→ lead updated
→ qualification
→ response
→ sales notification
```

## Definition of Done

A feature is tested when: - normal case works - invalid input is
handled - important edge cases are considered - errors do not corrupt
data - relevant automated tests pass - the complete flow still works
where applicable
