-- Write your PostgreSQL query statement below
WITH cust_product_count AS(
    SELECT
        c.customer_id AS c_id,
        COUNT(DISTINCT c.product_key) AS p_count
    FROM Customer AS c
    GROUP BY c.customer_id
),
product_count AS(
    SELECT
        COUNT(DISTINCT p.product_key) AS p_count
    FROM Product AS p
)
SELECT
    cpc.c_id AS customer_id 
FROM cust_product_count AS cpc
INNER JOIN product_count AS pc ON pc.p_count = cpc.p_count
ORDER BY cpc.c_id;
