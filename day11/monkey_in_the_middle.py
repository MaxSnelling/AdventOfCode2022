import operator
import numpy as np


class Monkey:
    """Monkey items and it's worry rules"""
    def __init__(self, items, operation, test_divisible, true_monkey, false_monkey):
        self.items = items
        self.operation = operation
        self.test_divisible = test_divisible
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspect_counter = 0


ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


def generate_monkeys(input_filename):
    """Turn input file into list of Monkey objects"""
    monkeys = []
    with open(input_filename) as f:
        lines = f.readlines()
        i = 1
        while True:
            if i >= len(lines):
                break

            [lines[i].replace(" ", "") for line in lines]
            items = [int(item) for item in lines[i][:-1].split(": ")[-1].split(", ")]
            i += 1
            operator = ops.get(lines[i][:-1].split(" ")[-2])
            operation_value = lines[i][:-1].split(" ")[-1]
            i += 1
            test_divisible = int(lines[i][:-1].split(" ")[-1])
            i += 1
            true_monkey = int(lines[i][:-1].split(" ")[-1])
            i += 1
            false_monkey = int(lines[i][:-1].split(" ")[-1])
            monkeys.append(Monkey(items,
                                  [operator, operation_value],
                                  test_divisible,
                                  true_monkey,
                                  false_monkey))
            i += 3
    return monkeys


def monkey_business_20(monkeys: list) -> int:
    """Calculate monkey business for 20 turns"""
    for _ in range(20):
        for monkey in monkeys.copy():
            for item in monkey.items:
                if monkey.operation[1].isnumeric():
                    operation_value = int(monkey.operation[1])
                else:
                    operation_value = item

                worry = monkey.operation[0](item, operation_value)
                worry = np.floor(worry / 3)
                if worry % monkey.test_divisible == 0:
                    next_monk = monkey.true_monkey
                else:
                    next_monk = monkey.false_monkey

                monkeys[next_monk].items.append(int(worry))

                monkey.inspect_counter += 1
            monkey.items = []

    sorted_counter = np.sort([x.inspect_counter for x in monkeys])
    del monkeys
    return sorted_counter[-2] * sorted_counter[-1]


def monkey_business_10_000(monkeys: list) -> int:
    """Calculate monkey business for 10,000 turns"""
    modulo = 1
    for i in [x.test_divisible for x in monkeys]:
        modulo *= i

    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                if monkey.operation[1].isnumeric():
                    operation_value = int(monkey.operation[1])
                else:
                    operation_value = item

                worry = monkey.operation[0](item, operation_value)
                worry = worry % modulo
                if worry % monkey.test_divisible == 0:
                    next_monk = monkey.true_monkey
                else:
                    next_monk = monkey.false_monkey

                monkeys[next_monk].items.append(int(worry))

                monkey.inspect_counter += 1
            monkey.items = []
    sorted_counter = np.sort([x.inspect_counter for x in monkeys])
    return sorted_counter[-2] * sorted_counter[-1]


input_file = "input.txt"
#  Part 1
print(f"Monkey business for 20 turns: {monkey_business_20(generate_monkeys(input_file))}")
#  Part 2
print(f"Monkey business for 10,000 turns: {monkey_business_10_000(generate_monkeys(input_file))}")
