WITH five_direct AS(
    SELECT
        e.id,
        e.name,
        COUNT(e.id)
    FROM Employee AS e
    INNER JOIN Employee AS em ON e.id = em.managerId
    GROUP BY e.id, e.name
    HAVING COUNT(e.id) >= 5
)
SELECT
    fd.name
FROM five_direct AS fd;