-- 602. Friend Requests II: Who Has the Most Friends
WITH un AS(
    SELECT
        requester_id AS id
    FROM RequestAccepted AS ra

    UNION ALL

    SELECT
        accepter_id AS id
    FROM RequestAccepted AS ra
),
num_friends AS(
    SELECT
        un.id,
        COUNT(*) AS num
    FROM un
    GROUP BY un.id
),
max_friends AS(
    SELECT
        nf.id,
        nf.num,
        DENSE_RANK() OVER(ORDER BY nf.num DESC) AS rnk
    FROM num_friends AS nf
)
SELECT
    mf.id,
    mf.num
FROM max_friends AS mf
WHERE mf.rnk = 1;