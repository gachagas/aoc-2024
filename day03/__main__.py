from pathlib import Path


def load_input():
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as f:
        str = f.read()

    return str


def main():
    data: str = load_input()
    stack: str = ""
    has_open = False
    has_comma = False
    result = 0
    ctr = 0

    enabled = True
    for idx, character in enumerate(data):
        if idx < 3:
            continue

        ### if else block for part 2
        if enabled:
            if data[idx - 7 : idx] == "don't()":
                enabled = False
                has_open = False
                has_comma = False
                stack = ""
                continue
        else:
            if data[idx - 4 : idx] == "do()":
                enabled = True
            continue

        if character == "(" and not has_open:
            if data[idx - 3 : idx] == "mul":
                has_open = True
                continue

        if character == "," and not has_comma:
            stack = stack + character
            has_comma = True
            continue

        if character == ")" and has_open and has_comma:
            split = stack.split(",")
            ctr += 1
            result += int(split[0]) * int(split[1])
            stack = ""

            has_comma = False
            has_open = False
            continue

        if character.isdigit():
            stack = stack + character
            continue

        has_open = False
        has_comma = False
        stack = ""

    print(result)
    print(ctr)


if __name__ == "__main__":
    main()
