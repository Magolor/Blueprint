# Local Docker Usage

This machine uses `~/Developer/Setup/assets/docker/control.bash` through the shell
helper `ds` for the default local Docker stacks. The prepared Compose projects live
under `~/Developer/Containers/compose/`.

Use `ds` for normal stack lifecycle work because it prepares the stack assets,
creates expected local folders, applies database profiles, removes orphan
containers, preserves named volumes, and runs the database post-start bootstrap
where needed.

Use raw `docker` or `docker compose` for inspection, low-level debugging, and quick
restarts of containers that already exist.

Use the setup stage to reproduce images from an empty local cache. The default
stage pulls default-stack images; the full-profile switch pulls every
Docker-hosted database profile, including heavy and amd64-only services.

```bash
cd ~/Developer/Setup
bash scripts/7-00-docker.bash
SETUP_DOCKER_DATABASE_FULL_PROFILES=1 bash scripts/7-00-docker.bash
```

## Default Stacks

- `databases`: local databases, search engines, vector stores, graph, and analytics services.
- `hermes`: Hermes gateway/dashboard container.
- `llm`: local LLM proxy containers for Portkey and Bifrost.

```bash
ds databases
ds hermes
ds llm
ds all
```

## Restart Choice

`ds <stack> --restart` is the preferred local restart path when Compose assets,
profiles, environment, or bootstrap behavior matter. In this setup, `--restart`
maps to a Compose force-recreate while preserving named volumes.

```bash
ds databases --restart
ds hermes --restart
ds llm --restart
ds all --restart
```

Use raw `docker restart` only for a quick stop/start cycle of existing containers.
It preserves images, networks, Compose definitions, and named volumes, but it does
not create missing containers, pull images, apply changed Compose profiles, recreate
containers from changed configuration, remove orphans, or run database bootstrap.

```bash
docker restart databases-postgres
docker restart hermes llm-portkey llm-bifrost
docker restart databases-postgres databases-mysql databases-redis databases-mongo databases-qdrant databases-chroma databases-surrealdb
```

Use raw Compose commands when debugging from the prepared stack directory.

```bash
cd ~/Developer/Containers/compose/databases
docker compose ps
docker compose logs --tail=100
docker compose restart
docker compose up -d --remove-orphans
```

```bash
cd ~/Developer/Containers/compose/hermes
docker compose ps
docker compose logs --tail=100 hermes
docker compose restart hermes
```

```bash
cd ~/Developer/Containers/compose/llm
docker compose ps
docker compose logs --tail=100
docker compose restart
```

## Databases

Default database services:

- PostgreSQL with pgvector: `databases-postgres`
- MySQL: `databases-mysql`
- Redis Stack with RediSearch: `databases-redis`
- MongoDB: `databases-mongo`
- Qdrant: `databases-qdrant`
- Chroma: `databases-chroma`
- SurrealDB: `databases-surrealdb`

```bash
ds databases
ds databases --restart
```

Broad routine profiles add Elasticsearch, OpenSearch, SeekDB, Neo4j, Weaviate,
Milvus, StarRocks, and Trino while excluding memory-heavy relational engines and
amd64-only services.

```bash
ds databases --all-profiles
ds databases --restart --all-profiles
ds databases --restart --profiles "elasticsearch opensearch seekdb neo4j weaviate milvus starrocks trino"
```

Full supported database, search, graph, vector, and analytics coverage:

- Native or client-library coverage, no Docker server: SQLite, DuckDB, LanceDB, TinyDB, and Milvus Lite.
- Default containers: PostgreSQL with pgvector, MySQL, Redis Stack with RediSearch, MongoDB, Qdrant, Chroma, and SurrealDB.
- Optional containers: Elasticsearch, OpenSearch, SeekDB, Neo4j, Weaviate, Milvus standalone, Oracle Free, OceanBase CE, SQL Server Developer, Pinecone Local, StarRocks, and Trino.

Start heavier or emulated services explicitly.

```bash
ds databases --restart --profiles oracle
ds databases --restart --profiles oceanbase
ds databases --restart --profiles milvus
ds databases --restart --profiles starrocks
ds databases --restart --profiles trino
ds databases --restart --include-heavy
ds databases --restart --include-amd64
```

After removing Setup-managed containers or images, the reproducible full-profile
database path is:

```bash
cd ~/Developer/Setup
SETUP_DOCKER_DATABASE_FULL_PROFILES=1 bash scripts/7-00-docker.bash
ds databases --restart --all-profiles --include-heavy --include-amd64
```

Local stack notes:

- SQL Server uses the `mssql-amd64` profile and is pinned to `mcr.microsoft.com/mssql/server:2022-latest`; start it explicitly with `ds databases --restart --include-amd64`.
- OceanBase uses upstream `root@sys` without a password. Its entrypoint wrapper regenerates OBD config for preserved `/root/ob` volumes in fresh containers, the bootstrap can still force-start a stuck `obcluster`, and it creates the local `magolor` user. Do not record the local password in this tracked note.
- Milvus standalone uses bundled etcd and MinIO. Its `MINIO_ACCESS_KEY_ID` / `MINIO_SECRET_ACCESS_KEY` values must match the MinIO root credentials or Milvus exits with S3 signature errors.

Inspect database containers directly when needed.

```bash
docker ps --format '{{.Names}}\t{{.Status}}' --filter 'name=databases-'
docker ps -a --format '{{.Names}}\t{{.Status}}' --filter 'name=databases-'
```

## Hermes

The Hermes container is `hermes`.

```bash
ds hermes
ds hermes --restart
```

```bash
docker restart hermes
docker logs --tail=100 hermes
```

## LLM

The LLM stack containers are:

- Portkey gateway: `llm-portkey`
- Bifrost gateway: `llm-bifrost`

```bash
ds llm
ds llm --restart
```

```bash
docker restart llm-portkey llm-bifrost
docker logs --tail=100 llm-portkey
docker logs --tail=100 llm-bifrost
```

## Updates

Do not update stateful database images as routine cleanup. Pull or change database
images only for a concrete fix, compatibility update, security update, or explicit
image refresh. For PostgreSQL major versions, dump, recreate, and restore instead
of blindly changing the image tag on an existing volume.

```bash
cd ~/Developer/Containers/compose/databases
docker compose ps
docker compose logs --tail=100
docker compose pull <service-name>
docker compose up -d <service-name>
docker compose logs --tail=100 <service-name>
```
