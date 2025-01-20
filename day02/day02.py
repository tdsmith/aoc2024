import typer
from pathlib import Path
import numpy as np


def part1(records: list[np.ndarray]):
    is_ok = 0
    for record in records:
        all_increasing = (record[1:] > record[:-1]).all()
        all_decreasing = (record[1:] < record[:-1]).all()
        deltas = np.abs(np.diff(record))
        deltas_ok = ((deltas >= 1) & (deltas <= 3)).all()
        is_ok += ((all_increasing | all_decreasing) & deltas_ok).all()
    return is_ok


def main(input: Path):
    records = [
        np.array([int(x) for x in line.split()]) for line in input.open("rt") if line
    ]
    print(part1(records))


if __name__ == "__main__":
    typer.run(main)
