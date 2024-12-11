from pathlib import Path
from typing import List
from functools import lru_cache


def load_input():
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as f:
        data = f.readline().strip()
    return [int(datum) for datum in data.split(" ")]


@lru_cache(maxsize=None)
def count_after_blink(number: int, remaining_blinks: int) -> int:
    # base condition, count +1 at final blink
    if remaining_blinks == 0:
        return 1

    if number == 0:
        return count_after_blink(1, remaining_blinks - 1)

    num_str = str(number)

    if len(num_str) % 2 == 0:
        half_len = len(num_str) // 2
        first_half = int(num_str[:half_len])
        second_half = int(num_str[half_len:])

        # get the calculations of both new numbers
        return count_after_blink(first_half, remaining_blinks - 1) + count_after_blink(
            second_half, remaining_blinks - 1
        )

    else:
        return count_after_blink(number * 2024, remaining_blinks - 1)


def part1(casted_data: List[int], num_blinks: int):
    total_count = 0  # for single number
    for number in casted_data:
        total_count += count_after_blink(number=number, remaining_blinks=num_blinks)
    return total_count


if __name__ == "__main__":
    data = load_input()
    blinks = part1(data, 75)
    print(blinks)
