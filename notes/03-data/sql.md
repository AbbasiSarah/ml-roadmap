# SQL

*Data Skills* · [Open in the interactive roadmap](https://abbasisarah.github.io/roadmap/#sql)

> **In one sentence:** SQL is how you ask a database questions, and in most jobs it is how you get the data in the first place.

## Key ideas
- `SELECT ... FROM ... WHERE ...` filters rows.
- `GROUP BY` with `COUNT`, `SUM`, `AVG` summarises.
- `JOIN` combines tables on a key.
- Window functions (`ROW_NUMBER() OVER (...)`) answer "top N per group" questions.

## Example
```sql
SELECT city,
       COUNT(*)          AS orders,
       ROUND(AVG(total)) AS avg_order
FROM orders
WHERE order_date >= '2026-01-01'
GROUP BY city
ORDER BY orders DESC
LIMIT 5;
```

## Common mistakes
- `SELECT *` on huge tables.
- Joins that multiply rows by accident; check row counts before and after.

## Learn more
- [Kaggle Learn: Intro to SQL](https://www.kaggle.com/learn/intro-to-sql) · Free · Course

## Practice project
Answer five business questions on a public database using only SQL.

---
[← Back to the roadmap](../../README.md) · Notes by Sara Abbasi · [SheCodesAI](https://abbasisarah.github.io)
