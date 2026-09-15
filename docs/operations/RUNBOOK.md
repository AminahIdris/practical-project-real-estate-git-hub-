# Operations Runbook

## Health Check

Backend:

``` text
GET /api/v1/health
```

Expected:

``` json
{
  "status": "ok"
}
```

## Common Checks

### Containers

``` bash
docker compose ps
```

### Logs

``` bash
docker compose logs --tail=200
```

### Restart

``` bash
docker compose restart
```

### Rebuild

``` bash
docker compose up -d --build
```

## Database

Before migrations: - confirm backup availability - confirm production
environment - review migration

## n8n

Check: - workflow enabled - credentials valid - recent executions -
failed executions - notification integration

## Incident: AI Failure

1.  Confirm customer message remains stored.
2.  Inspect workflow execution.
3.  Check AI provider availability.
4.  Retry safely.
5.  If persistent, use fallback/clarification behavior.

## Incident: Notification Failure

1.  Confirm lead is stored.
2.  Confirm score is stored.
3.  Inspect notification integration.
4.  Retry notification.
5.  Do not recreate the lead.

## Incident: Database Failure

1.  Check PostgreSQL container.
2.  Check disk/storage.
3.  Check database logs.
4.  Confirm persistent volume.
5.  Restore from backup only when necessary.

## Deployment Checklist

-   [ ] frontend builds
-   [ ] backend starts
-   [ ] PostgreSQL starts
-   [ ] n8n starts
-   [ ] migrations complete
-   [ ] domain works
-   [ ] HTTPS works
-   [ ] health endpoint works
-   [ ] customer message works
-   [ ] AI processing works
-   [ ] qualification works
-   [ ] sales notification works
-   [ ] backups configured
-   [ ] restart test completed
