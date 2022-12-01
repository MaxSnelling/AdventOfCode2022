import numpy as np


def sum_largest_elves(calorie_counts: list, n: int) -> int:
    """ Sum largest values in list.

    :param calorie_counts: list of calories each elf has
    :param n: number of top elves to sum
    :return: total calories held by top elves
    """
    np.sort(calorie_counts)
    return np.sum(calorie_counts[-n:])


def get_calories_per_elf(filename: str) -> list:
    """Sum calories held by each elf using input file

    :param filename: File which has list of calories
    :return: total calories held by each elf
    """
    with open(filename) as f:
        lines = f.readlines()
        calories_per_elf = []
        elf_sum = 0
        for line in lines:
            if line.strip() != '':
                elf_sum += int(line)
            else:
                calories_per_elf.append(elf_sum)
                elf_sum = 0
        return calories_per_elf


if __name__ == '__main__':
    #  Part One
    calories_per_elf = get_calories_per_elf('input.txt')
    print(f"Largest: {np.max(calories_per_elf)}")

    #  Part Two
    top_elves_count = 3
    if top_elves_count <= len(calories_per_elf):
        print(f"Sum of largest {top_elves_count} elves: {sum_largest_elves(calories_per_elf, top_elves_count)}")
    else:
        raise ValueError("Not enough elves")

