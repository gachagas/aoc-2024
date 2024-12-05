# TODO: clean this up

from pathlib import Path
import math

from typing import List, Tuple


def load_input() -> Tuple[List[str], List[str]]:
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path, "r") as f:
        str = f.read().splitlines()

    empty_found = False
    rules = []
    updates = []
    for row in str:
        if row == "":
            empty_found = True
            continue

        if not empty_found:
            rules.append(row)
        else:
            updates.append(row)

    return rules, updates


def build_ruleset_dict(rules: List[str]):
    rule_dict: dict[str, List[str]] = {}

    for rule in rules:
        num_before, num_after = rule.split("|")

        try:
            rule_dict[num_before].append(num_after)
        except KeyError:
            rule_dict[num_before] = [num_after]

    return rule_dict


def build_ruleset_dict_int_value(rules: List[str]):
    rule_dict: dict[str, List[str]] = {}

    for rule in rules:
        num_before, num_after = rule.split("|")

        try:
            rule_dict[num_before].append(num_after)
        except KeyError:
            rule_dict[num_before] = [num_after]

    for key, val in rule_dict.items():
        rule_dict[key] = [int(x) for x in val]
    return rule_dict


def part1():
    rules, updates = load_input()

    sum = 0
    bad_updates = []

    rule_dict = build_ruleset_dict(rules=rules)

    # process updates
    for update in updates:
        arr = update.split(",")
        check = set()
        for idx, number in enumerate(arr):
            check.add(number)

            # skip or fail row if intersection found
            if number in rule_dict:
                if set(rule_dict[number]) & check:
                    bad_updates.append(update)
                    break

            if idx == len(arr) - 1:
                middle_element = math.floor(len(arr) / 2)
                sum = sum + int(arr[middle_element])

    return sum, bad_updates


def part2(bad_updates: List[str]):
    rules, _ = load_input()
    rule_dict = build_ruleset_dict_int_value(rules=rules)

    fixed_updates = []

    bad_updates_split = [update.split(",") for update in bad_updates]
    bad_updates_int = [
        [int(number) for number in bad_update] for bad_update in bad_updates_split
    ]

    for update in bad_updates_int:
        check = set()
        idx = 0

        while idx < len(update):
            number = update[idx]
            check.add(number)

            if str(number) in rule_dict:
                if set(rule_dict[str(number)]) & check:
                    bad_item = set(rule_dict[str(number)]) & check
                    set_item = next(iter(bad_item))

                    swap_a = update.index(set_item)
                    swap_b = update.index(number)
                    temp = update[swap_a]
                    update[swap_a] = update[swap_b]
                    update[swap_b] = temp

                    idx = 0
                    check = set()

                    continue

            idx += 1
        fixed_updates.append(update)

    sum = 0
    for item in fixed_updates:
        middle_element = math.floor(len(item) / 2)
        sum = sum + item[middle_element]
    return sum


if __name__ == "__main__":
    sum, bad_updates = part1()
    print(sum)
    print(part2(bad_updates=bad_updates))
