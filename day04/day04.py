import typer
from pathlib import Path
from collections.abc import Iterable
from itertools import product


def part1(arr: list[list[str]]) -> int:
    # maximum dimensions
    I, J = len(arr), len(arr[0])

    def expand(i: int, j: int) -> Iterable[tuple[int, int, str]]:
        for di, dj in product((-1, 0, 1), (-1, 0, 1)):
            if di == 0 and dj == 0:
                continue
            ii, jj = i + di, j + dj
            if ii >= 0 and jj >= 0 and ii < I and jj < J:
                yield (ii, jj, arr[ii][jj])

    def is_root(i: int, j: int, needle: str = "XMAS") -> bool:
        if not needle:
            return True
        if arr[i][j] != needle[0]:
            return False
        return any(is_root(i, j, needle[1:]) for (i, j, _) in expand(i, j))

    n_xmas = 0
    for i, j in product(range(I), range(J)):
        n_xmas += int(is_root(i, j))

    return n_xmas


def main(input: Path):
    arr = [list(line.strip()) for line in input.read_text().splitlines()]
    print(part1(arr))


if __name__ == "__main__":
    typer.run(main)
