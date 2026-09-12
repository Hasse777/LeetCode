-- Write your PostgreSQL query statement below
WITH weighted_sums AS (
    SELECT
        q.person_name,
        SUM(weight) OVER(ORDER BY q.turn) AS total_weight
    FROM Queue AS q
)
SELECT
    ws.person_name AS person_name
FROM weighted_sums AS ws
WHERE ws.total_weight <= 1000
ORDER BY ws.total_weight DESC
LIMIT 1;
