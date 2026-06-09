WITH top_three_salaries AS(
    SELECT
        e.departmentId,
        e.name,
        e.salary,
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
    FROM Employee AS e
),
max_rnk AS(
    SELECT
        *
    FROM top_three_salaries AS tts
    WHERE rnk <= 3
)
SELECT
    d.name AS Department,
    mr.name AS Employee,
    mr.salary
FROM max_rnk AS mr
INNER JOIN Department AS d ON d.id = mr.departmentId
ORDER BY Department;