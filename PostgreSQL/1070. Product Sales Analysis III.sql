-- 1070. Product Sales Analysis III
WITH first_sale as(
    SELECT
        s.product_id,
        MIN(year) OVER (PARTITION BY s.product_id) AS first_year,
        s.year,
        s.quantity,
        s.price
    FROM Sales AS s
)
SELECT
    fs.product_id,
    fs.first_year,
    fs.quantity,
    fs.price
FROM first_sale AS fs
WHERE fs.year = fs.first_year;