from pathlib import Path


def load_input():
    arr = []

    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as f:
        while line := f.readline():
            arr.append(line.split())

    return arr


def generate_sorted_lists():
    input = load_input()

    left_list = []
    right_list = []

    for row in input:
        right_list.append(int(row[1]))
        left_list.append(int(row[0]))

    right_list = sorted(right_list)
    left_list = sorted(left_list)

    return left_list, right_list


def part1():
    left_list, right_list = generate_sorted_lists()
    sum = 0

    for idx, left in enumerate(left_list):
        sum = sum + abs(int(left) - int(right_list[idx]))

    return sum


# two pointer
def part2():
    left_list, right_list = generate_sorted_lists()

    similarity_score = 0

    for _, left in enumerate(left_list):
        for _, right in enumerate(right_list):
            if left == right:
                similarity_score = similarity_score + left
                continue

    return similarity_score


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
