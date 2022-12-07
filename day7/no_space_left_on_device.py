
class Folder:
    def __init__(self, name=""):
        self.name = name
        self.sub_folders = {}
        self.memory_size = 0


def build_children(lines: list, i: int, folder: Folder):
    while True:
        if i == len(lines):
            return folder, i
        if lines[i].startswith("$ cd .."):
            return folder, i+1
        elif lines[i].startswith("$ cd"):
            child_folder_name = lines[i][5:-1]
            child_folder, i = build_children(lines, i+1, folder.sub_folders.get(child_folder_name))
            folder.sub_folders.update({child_folder_name: child_folder})
        elif lines[i].startswith("$ ls"):
            i += 1
            pass
        elif lines[i].startswith("dir "):
            folder_name = lines[i][4:-1]
            if folder.sub_folders.get(folder_name) is None:
                folder.sub_folders.update({folder_name: Folder(folder_name)})
            i += 1
            pass
        else:
            folder.memory_size += int(lines[i].split(" ")[0])
            i += 1


def investigate_children(folder: Folder, total_sum: int):
    sum = folder.memory_size

    if len(folder.sub_folders) == 0:
        if sum <= 100000:
            total_sum += sum
        return folder, sum, total_sum

    for name in folder.sub_folders:
        sub_folder2 = folder.sub_folders.get(name)
        sub_folder, sub_sum, total_sum = investigate_children(sub_folder2, total_sum)
        sum += sub_sum

    if sum <= 100000:
        total_sum += sum

    return folder, sum, total_sum


def get_sum(folder: Folder):
    sum = 0

    if len(folder.sub_folders) == 0:
        return folder.memory_size

    for name in folder.sub_folders:
        sub_folder2 = folder.sub_folders.get(name)
        sum += get_sum(sub_folder2)

    return sum


def get_size(folder:Folder, min_del_size):
    sum = folder.memory_size

    if len(folder.sub_folders) == 0:
        if delete_size <= sum < min_del_size:
            min_del_size = sum
        return sum, min_del_size

    for name in folder.sub_folders:
        sub_folder2 = folder.sub_folders.get(name)
        sub_sum, min_del_size = get_size(sub_folder2, min_del_size)
        sum += sub_sum

    if delete_size <= sum < min_del_size:
        min_del_size = sum

    return sum, min_del_size


with open('input.txt') as f:
    lines = f.readlines()
    i = 1
    root, i = build_children(lines, i, Folder("/"))
    root, sum, total_sum = investigate_children(root, 0)
    print(sum)
    print(total_sum)
    delete_size = sum - 40000000
    min_size = get_size(root, sum)
    print(delete_size)
    print(min_size)
    print(f"sum: {sum}")
