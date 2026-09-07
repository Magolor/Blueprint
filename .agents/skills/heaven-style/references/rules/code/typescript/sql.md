---
id: ts-sql
title: TypeScript SQL and data access
blocking: true
description: Own TypeScript database clients, queries, transactions, rows, and migrations.
---

# TypeScript SQL and Data Access

## Core rule

Use the repository's declared database owner, ORM, query builder, or driver directly and consistently. Keep database mechanics behind the owning data-access boundary without inventing a second abstraction that merely renames a mature client.

Parameterize caller-controlled values. Make connection/transaction lifetime explicit. Validate decoded rows at the trust boundary. Keep dialect/provider details out of domain orchestration. Raw SQL is valid when it expresses the contract more clearly than the selected abstraction.

## Do

- Identify the existing database owner and transaction convention from repository metadata, nearby code, migrations, and tests.
- Bind every caller-controlled value through the driver/query-builder parameter mechanism. Dynamic identifiers require a validated allowlist or the library's identifier API. Values and identifiers have different contracts.
- Keep pools, clients, prepared statements, cursors, and subscriptions under an explicit async lifecycle owner. Await close/disposal and prove teardown in tests.
- Pass a transaction-scoped client/context explicitly through the operations that participate in one transaction. Do not let nested helpers silently escape to a global pool.
- Put schema changes in the repository's migration system. Migrations are ordered, restart-safe or transactionally bounded, and tested against the supported database versions.
- Keep substantial static SQL in an owned resource or migration file when that improves review, syntax tooling, and reuse. Load it through [utilities and platform APIs](util.md), not `process.cwd()` assumptions.
- Treat driver rows and JSON/database values as external data. Validate or map them once into domain types; generated static row types do not prove runtime schema or migration alignment.
- Preserve the original database failure with `cause` when translating it into a stable public error. Retry only documented transient failures and only under an idempotent/transactional contract.
- Redact credentials and sensitive bind values from logs. Query timing/shape may be observable without logging full statements or payloads.

## Avoid

- Template literals, concatenation, or string replacement for caller-controlled SQL values.
- Accepting arbitrary table, column, ordering, or operator text because bind parameters cannot represent identifiers.
- Ambient process-global clients hidden behind generic helpers.
- High-level domain or interface modules importing concrete database drivers.
- Opening one connection per operation when the driver expects a pool, or sharing one transactional connection concurrently without a proven contract.
- Returning driver rows directly as public domain objects.
- Catching a database failure and returning empty success, stale data, or `undefined` as though the row were absent.
- Adding an ORM or repository layer solely to make TypeScript resemble another codebase.

## Example

**Anti-pattern:**

```ts
export async function loadUser(client: DbClient, userId: string): Promise<UserRow | undefined> {
  const result = await client.query(`select * from users where id = '${userId}'`)
  return result.rows[0]
}
```

**Recommended pattern:**

```ts
export async function loadUser(client: DbClient, userId: UserId): Promise<User | undefined> {
  const result = await client.query(
    'select id, email, status from users where id = $1',
    [userId],
  )
  const row: unknown = result.rows[0]
  return row === undefined ? undefined : UserRowSchema.parse(row)
}
```

Placeholder syntax is driver-specific. Use the selected driver's binding API. Do not copy this example mechanically.

## Transaction contract

- The transaction owner begins, commits, and rolls back exactly once.
- Every participating operation receives the scoped transaction/client explicitly.
- Errors retain the operation and safe database context.
- Cancellation/timeouts do not imply rollback completed until the driver confirms it.
- Retried transactions rerun only effects proven safe to repeat.
