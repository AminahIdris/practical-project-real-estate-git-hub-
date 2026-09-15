# VPS Deployment Specification

## Goal

Deploy a stable MVP using a simple single-VPS architecture.

## Production Architecture

``` text
Internet
   ↓
Domain
   ↓
Nginx
   ├── React
   ├── FastAPI
   └── n8n
          ↓
      PostgreSQL
```

## VPS Starting Point

Suggested MVP baseline:

``` text
2 vCPU
4 GB RAM
40–80 GB SSD
Ubuntu LTS
```

Actual sizing should be adjusted after observing real workload.

## Containers

Docker Compose manages:

-   Nginx
-   frontend
-   backend
-   PostgreSQL
-   n8n

## Networking

Only required public ports should be exposed.

Typical public access: - SSH - HTTP - HTTPS

PostgreSQL should remain on the internal Docker network unless there is
a documented reason otherwise.

## Persistent Data

Persist: - PostgreSQL data - n8n data

## Environment

Production secrets must be provided through environment configuration,
not committed files.

## HTTPS

Use Nginx with a trusted TLS certificate.

## Deployment Process

``` text
Pull code
→ review changes
→ build containers
→ run migrations
→ restart services
→ health check
→ smoke test
```

## Backups

Configure PostgreSQL backups and periodically test restoration.

## Recovery

After a VPS restart: - containers should restart - database should
persist - n8n data should persist - application should become healthy

## Do Not

Do not introduce Kubernetes, multiple VPS instances, message brokers,
microservices, or complex cloud infrastructure unless actual
requirements justify them.
