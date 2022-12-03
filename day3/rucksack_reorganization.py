import numpy as np


def get_compartment_priority_sum(filename: str) -> int:
    """Find common item between compartments for each
    elf, sum the priorities of these values.

    :param filename: filename of input data
    :return: sum of priorities of common item
    """
    with open(filename) as f:
        rucksacks = f.readlines()
        priorities_sum = 0
        for rucksack in rucksacks:
            middle_index = int(np.floor(len(rucksack)/2))
            compartment1 = rucksack[0:middle_index]
            compartment2 = rucksack[middle_index:-1]
            item_match = None
            for item in compartment1:
                if item in compartment2:
                    item_match = item
                    break
            if 'A' <= item_match <= 'Z':
                priorities_sum += ord(item_match) - 38
            elif 'a' <= item_match <= 'z':
                priorities_sum += ord(item_match) - 96
            else:
                raise ValueError(f"Item does not have a priority value: {priorities_sum}")

        return priorities_sum


def get_badges_sum(filename: str) -> int:
    """Find badge between 3 elves and sum the priorities of
    these badges.

    :param filename: filename of input data
    :return: sum of priority values for all badges
    """
    with open(filename) as f:
        rucksacks = f.readlines()
        priorities_sum = 0
        i = 0
        while i <= len(rucksacks) - 3:
            badge = None
            for item in rucksacks[i]:
                if item in rucksacks[i+1] and item in rucksacks[i+2]:
                    badge = item
                    break
            if 'A' <= badge <= 'Z':
                priorities_sum += ord(badge) - 38
            elif 'a' <= badge <= 'z':
                priorities_sum += ord(badge) - 96
            else:
                raise ValueError(f"Badge does not have a priority value: {badge}")
            i += 3

        return priorities_sum


if __name__ == '__main__':
    input_filename = 'input.txt'

    #  Part One
    compartment_sum = get_compartment_priority_sum(input_filename)
    print(f"Match priority sum: {compartment_sum}")

    #  Part Two
    badges_sum = get_badges_sum(input_filename)
    print(f"Badges priority sum: {badges_sum}")

