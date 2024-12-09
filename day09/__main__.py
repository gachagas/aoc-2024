from pathlib import Path
from typing import List


def load_input():
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as f:
        data = f.read()

    return data


def get_checksum(input: str):
    checksum = 0
    for idx, item in enumerate(input):
        if item == ".":
            continue
        checksum = checksum + idx * (int(item))

    return checksum


def build_disk_map(input: List[str]):
    disk_map = ""
    memory_block_ctr = 0

    for idx, number in enumerate(input):
        if idx % 2 == 0:
            disk_map += str(memory_block_ctr) * number
            memory_block_ctr += 1

        else:
            disk_map += "." * number

    return disk_map


def compact_disk_map(disk_map: str):
    disk_map = list(disk_map)

    ptr_a = 0
    ptr_b = len(disk_map) - 1

    while ptr_a < ptr_b:
        if disk_map[ptr_a] != ".":
            ptr_a += 1
            continue

        if disk_map[ptr_b] == ".":
            ptr_b -= 1
            continue

        disk_map[ptr_a] = disk_map[ptr_b]
        disk_map[ptr_b] = "."

        ptr_a += 1
        ptr_b -= 1

    return "".join(disk_map)


def main():
    data = load_input()

    num_input = [int(item) for item in data]

    disk_map = build_disk_map(num_input)
    compact_map = compact_disk_map(disk_map=disk_map)
    print(compact_map)
    print(get_checksum(compact_map))


if __name__ == "__main__":
    main()
