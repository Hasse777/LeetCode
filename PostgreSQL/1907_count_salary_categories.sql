WITH account_categories AS (
    SELECT
        a.account_id,
        CASE 
            WHEN a.income < 20000 THEN 'Low Salary'
            WHEN a.income BETWEEN 20000 AND 50000 THEN 'Average Salary'
            WHEN a.income > 50000 THEN 'High Salary'
        END AS category
    FROM Accounts AS a
),
categories AS(
    SELECT 'High Salary' AS category
    UNION
    SELECT 'Average Salary'
    UNION
    SELECT 'Low Salary'
)
SELECT
    c.category AS category,
    COALESCE(COUNT(ac.account_id), 0) AS accounts_count 
FROM account_categories AS ac
RIGHT JOIN categories AS c USING(category)
GROUP BY c.category;
