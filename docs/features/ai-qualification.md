# AI Qualification

## Purpose

Use AI to understand natural-language customer enquiries and extract
structured information.

## Example

Input:

``` text
Hi, I'm looking for a 3-bedroom apartment in Lekki.
My budget is ₦80 million and I want to buy within 3 months.
```

Expected extraction:

``` json
{
  "intent": "BUY",
  "property_type": "APARTMENT",
  "bedrooms": 3,
  "location": "Lekki",
  "budget_max": 80000000,
  "timeline": "WITHIN_3_MONTHS"
}
```

## Missing Information

If a customer says:

``` text
I want to buy a house in Lekki.
```

Do not invent: - budget - timeline - bedrooms

Ask a useful follow-up question.

## Ambiguity

If the customer says:

``` text
My budget is around 50-ish.
```

Do not assume a currency or unit. Ask for clarification.

## Human Handoff

If the customer asks to speak to a person, classify the intent as
`HUMAN_AGENT` and trigger the handoff path.

## Qualification Boundary

AI extraction and qualification scoring are separate responsibilities.

AI extracts facts.

Deterministic code calculates the score.
