---
name: ts-sql
description: Own TypeScript database clients, queries, transactions, rows, and migrations.
---

# TypeScript SQL and Data Access

## Summary

Prefer the highest-level existing database API that honestly supplies the operation. Keep domain operations on their owning object, use ORM queries whenever practical, and externalize SQL text as packaged resources when lower-level SQL is necessary.

## Preference order

Use the first suitable choice in this order:

1. The package's wrapped instance operation, such as `database.count()`.
2. An existing generic wrapped/introspection API, such as SQLAlchemy `inspect(database.engine)` through the declared database boundary.
3. ORM queries using the package's selected ORM.
4. File-read generic SQL.
5. File-read dialect-specific SQL.
6. File-read SQL with explicit dialect transpilation.
7. Hard-coded SQL text in source, only when the preceding options are impractical for a concrete reason.

Do not create a redundant wrapper merely to climb the list. The first two choices reuse owned APIs; a low-level driver is not automatically preferred over an ORM. Python uses SQLAlchemy ORM when the package has no stronger database owner; TypeScript follows the same ORM-first intent with the selected ORM. This rule does not select a new TypeScript dependency by popularity or require adding database infrastructure to a package that does not need it.

Generic SQL is preferred only when it correctly expresses the operation on the supported databases. Keep dialect-specific behavior with its adapter. Transpilation must preserve binds and verified target-dialect semantics; it is not a reason to add inline source SQL. Never trade correct behavior for a higher position on this list.

## Principle

Parameterize caller-controlled values. Make connection/transaction lifetime explicit. Validate decoded rows at the trust boundary. Keep dialect/provider details out of domain orchestration. Prefer SQL text in external `.sql` resources whenever practical, including short built-in queries. Read it as a raw string and execute it through the selected database owner. Keep inline SQL only when resource loading or dynamic query composition makes externalization impractical; document the concrete reason.

## Do

- Identify the existing database owner and transaction convention from repository metadata, nearby code, migrations, and tests.
- Bind every caller-controlled value through the driver/query-builder parameter mechanism. Dynamic identifiers require a validated allowlist or the library's identifier API. Values and identifiers have different contracts.
- Keep pools, clients, prepared statements, cursors, and subscriptions under an explicit async lifecycle owner. Await close/disposal and prove teardown in tests.
- Pass a transaction-scoped client/context explicitly through the operations that participate in one transaction. Do not let nested helpers silently escape to a global pool.
- Put schema changes in the repository's migration system. Migrations are ordered, restart-safe or transactionally bounded, and tested against the supported database versions.
- Bundle built-in SQL in `resources/sql/` or an equivalent owned folder. Include it in the package file allowlist or copy it into emitted assets during build. Verify the packed consumer can load it. Migrations keep their declared owner.
- Load SQL through [utilities and platform APIs](util.md), relative to the emitted module layout rather than `process.cwd()`. Use the driver’s raw/text/unsafe-string entry when needed; that name never permits interpolating caller data. Bind values separately.
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

These are private data-access adapter sketches showing the database contract. The public domain API exposes this work through its owning object, such as `users.get(user_id)` in Python or `users.get(userId)` in TypeScript; do not add a parallel public `load_user`/`loadUser` helper.

**Anti-pattern:**

```ts
export async function loadUser(client: DbClient, userId: string): Promise<UserRow | undefined> {
  const result = await client.query(`select * from users where id = '${userId}'`)
  return result.rows[0]
}
```

**Recommended pattern:**

The package includes `resources/sql/load-user.sql`:

```sql
select id, email, status from users where id = $1
```

Illustrative Node ESM adapter emitted as `dist/users.js`, with `resources/` beside `dist/`:

```ts
import { readFile } from 'node:fs/promises'

export async function loadUser(client: DbClient, userId: UserId): Promise<User | undefined> {
  const sql = await readFile(new URL('../resources/sql/load-user.sql', import.meta.url), 'utf8')
  const result = await client.query(sql, [userId])
  const row: unknown = result.rows[0]
  return row === undefined ? undefined : UserRowSchema.parse(row)
}
```

Placeholder syntax and raw-string entry names are driver-specific. For example, a driver may call its bound raw-string entry `unsafe(sql, params)`. Use the selected driver's documented API and the package's resource helper when available. Loading a resource does not sanitize SQL; only trusted package SQL supplies statement text. Resource caching belongs to the resource/lifecycle owner.

## Transaction contract

- The transaction owner begins, commits, and rolls back exactly once.
- Every participating operation receives the scoped transaction/client explicitly.
- Errors retain the operation and safe database context.
- Cancellation/timeouts do not imply rollback completed until the driver confirms it.
- Retried transactions rerun only effects proven safe to repeat.
