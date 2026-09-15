# Follow-Ups

## Purpose

Allow sales users to schedule and track customer follow-up.

## Follow-Up Data

-   lead
-   assigned user
-   due date/time
-   type
-   note
-   status
-   completed timestamp

## Lifecycle

``` text
PENDING
 ↓
COMPLETED
```

Potential future status:

``` text
PENDING → MISSED / CANCELLED
```

## Requirements

-   Sales users can create follow-ups.
-   Sales users can view pending follow-ups.
-   Completed follow-ups remain in history.
-   Follow-up activity should be associated with the lead.
