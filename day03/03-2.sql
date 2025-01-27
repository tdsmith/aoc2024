WITH concat_input AS (
    SELECT 'do()' || reduce(
        ARRAY_AGG(line),
        (x, y) -> x || y
    ) AS line
    FROM input
)


, pairs AS (
    SELECT
        flatten(
            list(
                regexp_extract_all(
                    regexp_extract(instr, 'do\(\)(.*)', 1),
                    'mul\((\d{1,3},\d{1,3})\)',
                    1
                )
            )
        ) AS pair
    FROM concat_input CROSS JOIN UNNEST(string_split(line, 'don''t()')) t(instr)
)

-- list of strings like '12,345'
SELECT sum(reduce([CAST(i AS int) FOR i IN string_split(p, ',')], (x, y) -> x * y))
FROM pairs CROSS JOIN UNNEST(pair) t(p)
