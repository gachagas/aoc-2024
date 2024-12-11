from pathlib import Path
from typing import List


def load_input():
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as f:
        arr = f.readline()
    return arr


def is_digit_length_even(num: str):
    return len(num) % 2 == 0


def blink(input: List[int]):
    modified_input = input
    ptr = 0

    while 0 <= ptr < len(modified_input):
        curr_num = str(modified_input[ptr])

        if int(curr_num) == 0:
            modified_input[ptr] = 1
        elif is_digit_length_even(curr_num):
            number_of_digits = len(curr_num)

            first_half = int(curr_num[: number_of_digits // 2])
            second_half = int(curr_num[number_of_digits // 2 :])

            modified_input[ptr : ptr + 1] = [first_half, second_half]

            ptr += 1
        else:
            modified_input[ptr] *= 2024

        ptr += 1

    return modified_input


def part1(num_blinks: int):
    data = load_input()

    casted_data = [int(datum) for datum in data.split(" ")]
    ptr = 0
    while ptr < num_blinks:
        casted_data = blink(casted_data)
        ptr += 1
        print(f"{len(casted_data)=} {ptr=}")
    print(casted_data)
    print(len(casted_data))


if __name__ == "__main__":
    part1(num_blinks=25)
