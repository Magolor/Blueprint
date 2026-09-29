---
name: sql
description: Use Python database APIs, binding, SQL resources, and migrations.
---

# SQL

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

Prefer SQL text in external `.sql` resources whenever practical, including short built-in queries. Read it as a raw string through the package resource owner and execute it through the selected database API. Parameterize values. Keep provider-specific policy with the provider/database layer rather than business modules. Keep inline SQL only when resource loading or dynamic composition makes externalization impractical, with a concrete reason.

## Do

- Identify and use the repository's existing database owner.
- Parameterize every caller-controlled value through the driver/ORM bind mechanism.
- Keep transaction and connection lifecycle explicit at the owning boundary.
- Put schema changes in the repository's migration system or declared scripts.
- Bundle built-in SQL under an owned `resources/sql/` folder or equivalent. Include it in wheel/sdist package data and verify loading from an installed distribution. Keep migration files with their migration owner.
- Use the driver’s raw/text/unsafe-string entry when required for loaded SQL; “unsafe” does not permit interpolating caller data. Bind values separately and constrain dynamic identifiers with the driver’s identifier API or an allowlist.
- Preserve contextual database errors or translate them once at the public boundary.

## Avoid

- f-string SQL, string interpolation, or concatenation with caller data.
- Ad-hoc DDL in handlers or business services.
- A second database abstraction around an already coherent project layer.
- Raw engine/connection access in high-level code when the project database owner supplies the operation.
- Requiring an unrelated platform database object in an otherwise independent package.

## ORM example

These are private data-access adapter sketches showing the database contract. The public domain API exposes this work through its owning object, such as `users.get(user_id)` in Python or `users.get(userId)` in TypeScript; do not add a parallel public `load_user`/`loadUser` helper.

**Anti-pattern:**

```python
def load_user(db, user_id: str):
    return db.execute(f"select * from users where id = '{user_id}'")
```

**Recommended pattern:**

```python
from sqlalchemy import select


def load_user(session: Session, user_id: str) -> User:
    stmt = select(User).where(User.id == user_id)
    return session.execute(stmt).scalar_one()
```

## SQL resource pattern

```python
from importlib.resources import files
from sqlalchemy import text


sql = files("acme.resources.sql").joinpath("refresh_catalog.sql").read_text(encoding="utf-8")
connection.execute(text(sql), {"target_id": target_id})
```

The query remains static and values remain bound. Use the target repository's resource and database helpers when it declares them.
