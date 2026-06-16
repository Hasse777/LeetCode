-- Write your PostgreSQL query statement below
WITH first_day AS(
    SELECT
        a.player_id AS pi,
        a.event_date AS ed,
        ROW_NUMBER() OVER(PARTITION BY a.player_id ORDER BY a.event_date) AS rn,
        LAG(a.event_date, 1) OVER(PARTITION BY a.player_id ORDER BY a.event_date) AS lg
    FROM Activity AS a
),
player_next_day AS(
    SELECT
        COUNT(DISTINCT fd.pi) AS next_day_players_count
    FROM first_day as fd
    WHERE
        rn = 2 AND
        lg IS NOT null AND
        ed = lg + INTERVAL '1 day'
),
all_players AS(
    SELECT
        COUNT(DISTINCT a.player_id) AS players_count
    FROM Activity AS a
)
SELECT
    ROUND(
        pnd.next_day_players_count::numeric / ap.players_count,
        2
    ) AS fraction
FROM all_players ap
CROSS JOIN player_next_day pnd;
