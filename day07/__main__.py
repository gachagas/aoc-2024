from pathlib import Path
import itertools


def load_input():
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as f:
        data = f.read().splitlines()

    return data


def main():
    data = load_input()

    total_calibration_result = 0
    for row in data:
        sum_str, valus_str = row.split(":")
        sum = int(sum_str)
        values = [int(value) for value in valus_str.strip().split()]

        operator_matrix = list(itertools.product("+*", repeat=len(values) - 1))

        for operator_array in operator_matrix:
            sum_temp = values[0]
            for idx, operator in enumerate(operator_array):
                if operator == "*":
                    sum_temp *= values[idx + 1]

                if operator == "+":
                    sum_temp += values[idx + 1]

            if sum == sum_temp:
                total_calibration_result = total_calibration_result + sum_temp
                break

    return total_calibration_result


if __name__ == "__main__":
    print(main())
