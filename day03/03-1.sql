WITH matches AS (
    SELECT reduce([CAST(x AS INTEGER) FOR x IN string_split(UNNEST(a.instr), ',')], (x, y) -> x * y) p
    FROM (SELECT regexp_extract_all(line, 'mul\((\d{1,3},\d{1,3})\)', 1) instr FROM input) a
)


SELECT SUM(p) FROM matches
