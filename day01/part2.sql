WITH parsed as (
    SELECT
        CAST(regexp_extract(line, '(\d+)\s+(\d+)', 1) AS INT) AS col1,
        CAST(regexp_extract(line, '(\d+)\s+(\d+)', 2) AS INT) AS col2
    FROM input
)

, counts as (
    SELECT
        col1,
        (SELECT COUNT(*) FROM parsed p2 WHERE p2.col2 = p1.col1) AS n
    FROM parsed p1
)

SELECT SUM(col1*n)
FROM counts
