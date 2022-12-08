trees = []
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        row = []
        for tree in line[:-1]:
            row.append(tree)
        trees.append(row)

rows = len(trees)
columns = len(trees[0])

# Part 1
visible_counter = 0
for y in range(rows):
    for x in range(columns):
        current_height = trees[y][x]
        visible = False
        column = [row[x] for row in trees]

        if x == 0 or x == columns - 1 or y == 0 or y == rows - 1:
            visible = True
        elif max(trees[y][:x]) < current_height or \
                max(trees[y][x + 1:]) < current_height or \
                max(column[:y]) < current_height or \
                max(column[y + 1:]) < current_height:
            visible = True

        if visible:
            visible_counter += 1

print(f"Number of tress visible: {visible_counter}")

directions_list = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]

#  Part 2
max_score = 0
for y in range(rows):
    for x in range(columns):
        current_height = trees[y][x]
        score = 1
        for directions in directions_list:
            tree_count = 0
            x_increment, y_increment = directions
            current_x, current_y = x, y
            while True:
                current_x += x_increment
                current_y += y_increment
                if current_x == -1 or current_x == columns or current_y == -1 or current_y == rows:
                    break
                tree_count += 1
                if current_height <= trees[current_y][current_x]:
                    break
            score *= tree_count

        if score > max_score:
            max_score = score

print(f"Maximum visibility score: {max_score}")
