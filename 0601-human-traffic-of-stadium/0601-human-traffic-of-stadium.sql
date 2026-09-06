# Write your MySQL query statement below
WITH valid_rows AS (
    SELECT
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
),
grouped AS (
    SELECT
        id,
        visit_date,
        people,
        grp,
        COUNT(*) OVER (PARTITION BY grp) AS group_size
    FROM valid_rows
)
SELECT
    id,
    visit_date,
    people
FROM grouped
WHERE group_size >= 3
ORDER BY visit_date ASC;