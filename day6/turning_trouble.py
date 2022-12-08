
def get_index_of_unique_characters(input_file: str, unique_size: int) -> int:
    """Gets index when unique characters of given size
    are found

    Args:
        unique_size: Number of unique characters to find
    """
    with open(input_file) as f:
        input = f.readlines()[0][:-1]

        i = unique_size - 1
        while i <= len(input) - unique_size:
            values = set()
            for j in range(unique_size):
                values.add(input[i-j])

            if len(values) == unique_size:
                return i

            i += 1


input_file = 'input.txt'
#  Part 1
four_char_index = get_index_of_unique_characters(input_file, 4)
print(f"The {four_char_index+1}th value is the first time 4 unique values appear")

#  Part 2
fourteen_char_index = get_index_of_unique_characters(input_file, 14)
print(f"The {fourteen_char_index+1}th value is the first time 14 unique values appear")
