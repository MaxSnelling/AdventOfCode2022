with open('input.txt') as f:
    assignments = f.readlines()
    full_overlap_counter = 0
    partial_overlap_counter = 0
    for pairs in assignments:
        range1, range2 = pairs.split(",")
        lower1, upper1 = int(range1.split("-")[0]), int(range1.split("-")[1])
        lower2, upper2 = int(range2.split("-")[0]), int(range2.split("-")[1])

        #  Part 1
        if (lower1 <= lower2 and upper1 >= upper2) or (lower2 <= lower1 and upper2 >= upper1):
            full_overlap_counter += 1

        #  Part 2
        if (lower1 <= lower2 <= upper1) or (lower2 <= lower1 <= upper2):
            partial_overlap_counter += 1

    print(f"Full overlap: {full_overlap_counter}")
    print(f"Partial overlap: {partial_overlap_counter}")


