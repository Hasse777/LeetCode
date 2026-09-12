WITH emp_dep AS(
    SELECT
        e.id,
        e.name,
        e.salary,
        e.departmentId,
        d.name AS department_name,
        DENSE_RANK() OVER(PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rank
    FROM Employee AS e
    INNER JOIN Department AS d ON d.id = e.departmentId
)
SELECT
    ed.department_name AS Department,
    ed.name AS Employee,
    ed.salary AS Salary
FROM emp_dep AS ed
WHERE ed.rank <= 3
ORDER BY ed.department_name, ed.salary DESC;
