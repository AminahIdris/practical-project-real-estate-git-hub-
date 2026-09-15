# Conversations

## Purpose

Maintain the customer conversation context required for lead
understanding and sales follow-up.

## Requirements

-   Each conversation belongs to a lead.
-   Messages are ordered chronologically.
-   Customer and bot messages are distinguishable.
-   Original messages are preserved.
-   Processing status can be tracked.
-   Duplicate external messages are handled idempotently.

## Conversation Context

AI processing may use relevant recent conversation history plus current
lead state.

Do not send unnecessary sensitive data to an AI provider.
