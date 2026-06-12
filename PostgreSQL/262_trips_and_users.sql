-- Write your PostgreSQL query statement below
WITH trips AS(
    SELECT
        t.id,
        t.client_id,
        t.driver_id,
        t.city_id,
        t.status AS status_drive,
        t.request_at
    FROM Trips AS t
    INNER JOIN Users AS uc
        ON t.client_id = uc.users_id AND uc.banned = 'No'
    INNER JOIN Users AS ud 
        ON t.driver_id = ud.users_id AND ud.banned = 'No'
    WHERE 
        t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
),
all_trips AS (
    SELECT
        t.request_at,
        COUNT(*) AS trips_all
    FROM trips AS t
    GROUP BY request_at
),
trips_canceled AS(
    SELECT
        t.request_at,
        COUNT(*) AS trips_cancelled
    FROM trips AS t
    WHERE t.status_drive IN ('cancelled_by_driver', 'cancelled_by_client')
    GROUP BY request_at

)
SELECT
    request_at AS Day,
    ROUND(COALESCE(tc.trips_cancelled, 0)::numeric / alt.trips_all, 2) AS "Cancellation Rate"
FROM all_trips AS alt
LEFT JOIN trips_canceled AS tc USING(request_at);