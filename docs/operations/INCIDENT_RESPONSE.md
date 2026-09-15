# Incident Response

## Severity

### P1 --- Critical

Core customer journey unavailable or data integrity is at risk.

### P2 --- Major

Important functionality degraded but the system remains partially
usable.

### P3 --- Minor

Non-critical issue with an available workaround.

## Response Process

``` text
Detect
→ Confirm
→ Contain
→ Diagnose
→ Recover
→ Verify
→ Document
```

## Principles

-   Protect customer data first.
-   Preserve evidence and logs.
-   Do not make risky production changes without understanding the
    failure.
-   Prefer reversible changes.
-   Record the root cause and corrective action.

## Post-Incident

Document: - impact - timeline - root cause - fix - tests - prevention
