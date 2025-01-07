WITH parsed as (
    SELECT
        CAST(regexp_extract(line, '(\d+)\s+(\d+)', 1) AS INT) AS col1,
        CAST(regexp_extract(line, '(\d+)\s+(\d+)', 2) AS INT) AS col2
    FROM input
)

, ordered AS (
    SELECT
        c1.col1,
        c2.col2
    FROM
        UNNEST(generate_series(1, (SELECT COUNT(*) FROM parsed))) t(rowno)
        FULL JOIN
            (SELECT row_number() OVER (ORDER BY col1) AS rowno, col1 FROM parsed) c1
            ON c1.rowno = t.rowno
        FULL JOIN
            (SELECT row_number() OVER (ORDER BY col2) AS rowno, col2 FROM parsed) c2
            ON c2.rowno = t.rowno
)

SELECT SUM(ABS(col1-col2))
FROM ordered
