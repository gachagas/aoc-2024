from pathlib import Path
from typing import Tuple, List


def load_input() -> List[int]:
    arr = []

    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as f:
        while line := f.readline():
            arr.append([int(x) for x in line.split()])

    return arr


def is_safe(row: list[int]) -> bool:
    is_increasing = False
    has_safe = False
    for idx, column in enumerate(row):
        if idx == len(row) - 1:
            has_safe = True
            break

        diff = column - row[idx + 1]

        if idx == 0:
            if diff < 0:
                is_increasing = True

        # for all increasing
        if is_increasing:
            if diff < 0 and abs(diff) <= 3:
                continue
            else:
                break

        # decreasing
        else:
            if diff > 0 and abs(diff) <= 3:
                continue
            else:
                break

    return has_safe


def part1() -> Tuple[int, List[int]]:
    data = load_input()
    safe_count = 0
    safe_indexes = []

    for row_idx, row in enumerate(data):
        if is_safe(row=row):
            safe_indexes.append(row_idx)
            safe_count += 1

    return safe_count, safe_indexes


def part2(safe_indexes: int) -> int:
    data = load_input()

    new_safe_count = 0

    for idx, row in enumerate(data):
        # don't execute on safe indexes
        if idx in safe_indexes:
            continue

        for popped_idx in range(len(row)):
            temp = row.copy()
            temp.pop(popped_idx)

            if is_safe(row=temp):
                new_safe_count += 1
                break
    return new_safe_count


def main():
    safe, safe_indexes = part1()
    new_safe_count = part2(safe_indexes=safe_indexes)
    print(f"p1: {safe}")
    print(f"p2: {safe+ new_safe_count}")


if __name__ == "__main__":
    main()
