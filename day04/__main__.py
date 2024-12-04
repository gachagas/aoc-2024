from pathlib import Path


def load_input():
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as f:
        str = f.read().splitlines()

    return str


def part1():
    data = load_input()

    total = 0
    for r_idx, row in enumerate(data):
        for c_idx, col in enumerate(row):
            # ount of bounds check
            if r_idx == 3 and c_idx == 9:
                pass

            # horizontal
            if row[c_idx : c_idx + 4] == "XMAS" or row[c_idx : c_idx + 4] == "SAMX":
                total = total + 1

            directions = [
                ("XMAS", 0, 1),  # vertical down
                ("SAMX", 0, 1),  # reverse vertical down
                ("SAMX", 1, 1),  # southeast
                ("XMAS", 1, 1),  # southeast reverse
                ("XMAS", -1, 1),  # southwest
                ("SAMX", -1, 1),  # southwest reverse
            ]
            for word, dx, dy in directions:
                try:
                    if (
                        col == word[0]
                        and data[r_idx + 1 * dy][c_idx + 1 * dx] == word[1]
                        and data[r_idx + 2 * dy][c_idx + 2 * dx] == word[2]
                        and data[r_idx + 3 * dy][c_idx + 3 * dx] == word[3]
                    ):
                        if c_idx + (3 * dx) < 0:
                            continue

                        total += 1
                except IndexError:
                    continue  # Skip out-of-bounds cases

    return total


def part2():
    data = load_input()

    total = 0
    for r_idx, row in enumerate(data):
        for c_idx, col in enumerate(row):
            if r_idx - 1 < 0 or c_idx - 1 < 0:
                continue

            directions = [
                "SMSM",
                "SSMM",
                "MMSS",
                "MSMS",
            ]

            for word in directions:
                try:
                    if (
                        col == "A"
                        and data[r_idx - 1][c_idx - 1] == word[0]
                        and data[r_idx - 1][c_idx + 1] == word[1]
                        and data[r_idx + 1][c_idx - 1] == word[2]
                        and data[r_idx + 1][c_idx + 1] == word[3]
                    ):
                        total += 1
                except IndexError:
                    continue  # Skip out-of-bounds cases

    return total


if __name__ == "__main__":
    print(part1())
    print(part2())
