win_scoring = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3}
}
type_scoring = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
result_conditions = {
    "X": {"A": "Z", "B": "X", "C": "Y"},
    "Y": {"A": "X", "B": "Y", "C": "Z"},
    "Z": {"A": "Y", "B": "Z", "C": "X"}
}
result_scoring = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

if __name__ == '__main__':
    total_score = 0
    strategy_score = 0
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            #  Part One
            total_score += win_scoring[line[0]][line[2]]
            total_score += type_scoring[line[2]]

            #  Part Two
            strategy_score += result_scoring[line[2]]
            strategy_score += type_scoring[result_conditions[line[2]][line[0]]]

    print(f"Total score: {total_score}")
    print(f"Strategy guide score: {strategy_score}")
