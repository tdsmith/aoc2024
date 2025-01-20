WITH parsed AS (
    SELECT
        report,
        generate_subscripts(line, 1) AS level,
        CAST(unnest(line) AS int) AS value,
    FROM (
        SELECT
            row_number() OVER () AS report,
            string_split(line, ' ') AS line
        FROM input
    )
)

, criteria AS (
    SELECT
        *,
        abs(value - lead(value) OVER w) AS delta,
        coalesce(sign(value - lag(value) OVER w) = sign(lead(value) OVER w - value), TRUE) AS sign_matches
    FROM parsed
    WINDOW w AS (PARTITION BY report ORDER BY level ASC)
)

, safety AS (
    SELECT
        report,
        bool_and(delta >= 1 AND delta <= 3 AND sign_matches) AS safe
    FROM criteria
    GROUP BY report
)

SELECT COUNT(*) FROM safety WHERE safe
