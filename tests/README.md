# Tests

## Layout

```text
tests/
├── unit/          # Fast, isolated unit tests (services, scoring, validation)
├── integration/   # Tests that cross boundaries (API + DB, etc.)
└── e2e/           # End-to-end customer journey tests
```

## Running tests

From repository root (once pytest is configured):

```bash
pytest
# or
pytest tests/unit
pytest tests/integration
```

See `docs/testing/TESTING_STRATEGY.md` for the full strategy.
