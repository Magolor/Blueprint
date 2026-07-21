---
id: sql
title: SQL
enabled: true
blocking: true
order: 70
category: code-quality
keywords: [sqlalchemy, embedded sql, f-string sql, orm, ddl, migration, raw sql, database layer]
description: Use when Python code touches database queries, raw SQL, migrations, DDL, binds, SQLAlchemy, ORM, or SQL resources.
---

# SQL

## Core rule

Use the target repository's declared database abstraction or ORM for application queries. If no project layer exists, use the selected driver/ORM directly and consistently. Do not add HeavenBase or invent a wrapper merely to avoid a mature database API.

Raw SQL is acceptable when it expresses behavior the chosen abstraction cannot model clearly. Keep substantial static SQL in package resources or migrations, parameterize values, and keep provider-specific policy with the provider/database layer rather than business modules.

## Apply when

- Code executes database queries, migrations, DDL, or raw SQL.
- Code introduces SQL resources, query helpers, engines, sessions, transactions, or connection lifecycle.
- A project database facade, SQLAlchemy, or another ORM/driver may own the behavior.

## Do

- Identify and use the repository's existing database owner.
- Parameterize every caller-controlled value through the driver/ORM bind mechanism.
- Keep transaction and connection lifecycle explicit at the owning boundary.
- Put schema changes in the repository's migration system or declared scripts.
- Keep substantial static raw SQL under package resources and load it through the repository resource policy.
- Preserve contextual database errors or translate them once at the public boundary.

## Avoid

- f-string SQL, string interpolation, or concatenation with caller data.
- Ad-hoc DDL in handlers or business services.
- A second database abstraction around an already coherent project layer.
- Raw engine/connection access in high-level code when the project database owner supplies the operation.
- Requiring a HeavenBase `Database` object in an unrelated package.

## ORM example

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

## Raw SQL exception

```python
from importlib.resources import files


sql = files("acme.resources.sql").joinpath("refresh_catalog.sql").read_text(encoding="utf-8")
connection.execute(text(sql), {"target_id": target_id})
```

The query remains static and values remain bound. Use the target repository's resource and database helpers when it declares them.

## HeavenBase profile

In a repository that explicitly adopts HeavenBase's database surface, use its `Database` and resource helpers for the concerns they own. That conditional profile does not override a generic package's declared ORM, driver, migration tool, or transaction policy.

## Related rules

Also apply [config.md](config.md) for database settings/resources, [util.md](util.md) for resource ownership, [types.md](types.md) for query result contracts, and [error.md](error.md) for database-boundary failures.
