# TODO: clean this up

from pathlib import Path
from typing import List, Tuple


def load_input():
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as f:
        data = f.read().splitlines()

    return data


def count_distinct_positions(matrix):
    count = 0
    for row in matrix:
        count += row.count("X")

    return count


def find_start_index(matrix: List[str]) -> Tuple[int, int]:
    for row_idx, row in enumerate(matrix):
        try:
            col_idx = row.index("^")
            return row_idx, col_idx
        except ValueError:
            pass


def pretty_print_index(data, start_row: int = None, end_row: int = None):
    if start_row and end_row:
        for idxx, rowie in enumerate(data):
            if idxx < start_row or idxx > end_row:
                continue
            print(f"{idxx+1:03d} {rowie}")

    else:
        for idxx, rowwie in enumerate(data):
            print(f"{idxx+1:03d} {rowwie}")


def part1() -> List[List[str]]:
    data = load_input()
    row, col = find_start_index(data)
    directions = ["^", ">", "v", "<"]
    direction_index = 0

    data[row] = data[row][:col] + "X" + data[row][col + 1 :]
    ctr = -1

    while 1:
        ctr = ctr + 1

        try:
            if directions[direction_index] == "^":
                # Out of bounds check
                if row - 1 == -1:
                    break

                if data[row - 1][col] == "#":
                    direction_index = 1
                    continue
                row -= 1

            if directions[direction_index] == ">":
                if col + 1 == len(data[row]):
                    break

                if data[row][col + 1] == "#":
                    direction_index = 2
                    continue

                col += 1

            if directions[direction_index] == "v":
                if row + 1 == len(data):
                    break

                if data[row + 1][col] == "#":
                    direction_index = 3
                    continue

                row += 1

            if directions[direction_index] == "<":
                if col - 1 == -1:
                    break

                if data[row][col - 1] == "#":
                    direction_index = 0
                    continue
                col -= 1

            data[row] = data[row][:col] + "X" + data[row][col + 1 :]

        except IndexError:
            break

    return data


if __name__ == "__main__":
    matrix = part1()
    count = count_distinct_positions(matrix=matrix)
