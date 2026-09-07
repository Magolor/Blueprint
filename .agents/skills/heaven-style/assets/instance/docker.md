# Docker Operations Owner

For the setup located in [setup.md](setup.md), use the installed `setup-docker`
controller for normal service lifecycle work. Read `assets/docker/control.bash`
and the selected stack's README in that setup checkout for current selectors,
profiles, restart behavior, image preparation, and bootstrap commands.

The setup owns `databases`, `hermes`, and `llm` stack definitions. Its machine
profile chooses runtime scope. Do not infer a default service set from another
machine's note. Start heavy or emulated services only when explicitly needed.
Native/client-only databases do not require a Docker server merely because the
same guide lists container databases.

Use raw `docker` or `docker compose` for inspection, low-level debugging, or a
quick restart of existing containers. A raw restart preserves current images,
networks, definitions, and named volumes. It does not create missing containers,
pull images, apply changed profiles/configuration, remove orphans, or rerun
bootstrap. Use the setup owner when those operations are required.

For recovery after image/container removal, use the setup's image-preparation
stage and then start the required scope. Inspect status and recent logs. Verify
the actual service operation; an existing container name does not prove health.

Keep these checks when diagnosing optional services:

- SQL Server's architecture profile and image tag belong to the setup definition.
- OceanBase bootstrap and preserved-volume recovery belong to its setup wrapper.
  Its upstream `root@sys` bootstrap can be passwordless; this does not describe
  the configured application account or authorize storing its password here.
- Milvus standalone uses etcd and MinIO. Its `MINIO_ACCESS_KEY_ID` and
  `MINIO_SECRET_ACCESS_KEY` must match the MinIO root credentials. A mismatch can
  cause S3 signature errors. Compare inside the consuming process without printing values.
- Hermes and LLM gateway container names, Portkey/Bifrost scope, and native Hermes
  behavior belong to their stack guides. Do not treat a container-only note as
  authority for a native installation.

The previous `ds` examples, fixed service inventory, `--all-profiles`,
`--include-heavy`, `--include-amd64`, and `--restart` recipes are superseded by the
current controller. Do not replay those historical commands on a new setup.
Stateful upgrades follow [macOS service guidance](../MacOS-env.md#stateful-service-changes)
and Setup's maintenance guide.
