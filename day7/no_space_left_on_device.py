
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
        elif lines[i].startswith("dir "):
            folder_name = lines[i][4:-1]
            if folder.sub_folders.get(folder_name) is None:
                folder.sub_folders.update({folder_name: Folder(folder_name)})
            i += 1
        else:  # File with size, in form "XXXXX name"
            folder.memory_size += int(lines[i].split(" ")[0])
            i += 1


def investigate_children(folder: Folder, sum_of_small_dirs: int):
    sum = folder.memory_size

    for name in folder.sub_folders:
        sub_dir_sum, sum_of_small_dirs = investigate_children(folder.sub_folders.get(name), sum_of_small_dirs)
        sum += sub_dir_sum

    if sum <= 100000:
        sum_of_small_dirs += sum

    return sum, sum_of_small_dirs


def get_size(folder: Folder, min_del_size):
    sum = folder.memory_size

    for name in folder.sub_folders:
        sub_dir_sum, min_del_size = get_size(folder.sub_folders.get(name), min_del_size)
        sum += sub_dir_sum

    if delete_size <= sum < min_del_size:
        min_del_size = sum

    return sum, min_del_size


with open('input.txt') as f:
    lines = f.readlines()
    root, i = build_children(lines, 1, Folder("/"))
    sum, sum_of_small_dirs = investigate_children(root, 0)
    print(f"Sum of directories less than 100000: {sum_of_small_dirs}")

    delete_size = sum - 40000000
    sum, min_del_size = get_size(root, sum)
    print(f"Minimum folder size to remove {delete_size}: {min_del_size}")
