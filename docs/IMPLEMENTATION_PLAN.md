# Implementation Plan

## Current Objective

Build the smallest working vertical slice first.

## Vertical Slice 1

``` text
POST /messages
→ store message
→ create/update lead
→ return accepted response
```

## Vertical Slice 2

``` text
Message
→ n8n
→ AI extraction
→ validated structured data
→ update lead
```

## Vertical Slice 3

``` text
Lead
→ deterministic score
→ classification
→ persist score
```

## Vertical Slice 4

``` text
Qualified lead
→ response generation
→ sales notification
```

## Vertical Slice 5

``` text
Sales dashboard
→ view lead
→ view conversation
→ update status
→ create follow-up
```

## Final Slice

``` text
Customer
→ React
→ FastAPI
→ PostgreSQL
→ n8n
→ AI
→ qualification
→ response
→ sales
→ follow-up
```

## Working Method

For each task:

1.  Read docs.
2.  Implement one bounded change.
3.  Test.
4.  Update implementation log.
5.  Update task status.
6.  Commit.

Do not build large layers in isolation for weeks if a smaller end-to-end
slice can validate the design earlier.
