from collections import Counter
from collections.abc import Sequence
from pathlib import Path

import typer


def part1(col1: Sequence[int], col2: Sequence[int]) -> int:
    col1 = sorted(col1)
    col2 = sorted(col2)
    v = sum(abs(c1 - c2) for c1, c2 in zip(col1, col2))
    return v


def part2(col1: Sequence[int], col2: Sequence[int]) -> int:
    c = Counter(col2)
    return sum(v * c[v] for v in col1)


def main(input: Path):
    col1, col2 = zip(
        *[(int(i) for i in line.split()) for line in input.read_text().splitlines()]
    )
    print(part1(col1, col2))
    print(part2(col1, col2))


if __name__ == "__main__":
    typer.run(main)
