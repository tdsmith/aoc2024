import typer
from pathlib import Path
import numpy as np


def part1(records: list[np.ndarray]):
    is_ok = 0
    for record in records:
        is_ok += is_safe(record)
    return is_ok


def is_safe(record: np.ndarray) -> bool:
    all_increasing = (record[1:] > record[:-1]).all()
    all_decreasing = (record[1:] < record[:-1]).all()
    deltas = np.abs(np.diff(record))
    deltas_ok = ((deltas >= 1) & (deltas <= 3)).all()
    return bool(((all_increasing | all_decreasing) & deltas_ok).all())


def is_safe_lossy(record: np.ndarray) -> bool:
    if is_safe(record):
        return True
    for i in range(len(record)):
        if is_safe(np.hstack((record[:i], record[i + 1 :]))):
            return True
    return False


def part2(records: list[np.ndarray]):
    is_ok = 0
    for record in records:
        is_ok += is_safe_lossy(record)
    return is_ok


def main(input: Path):
    records = [
        np.array([int(x) for x in line.split()]) for line in input.open("rt") if line
    ]
    print(part1(records))
    print(part2(records))


if __name__ == "__main__":
    typer.run(main)
