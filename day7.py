"""Day 7 of AoC."""
import os

def update_current_folder(current_folder, target):
    """Update the current folder with the target from a cd command

    If target is ".." --> go up a level (unless the current_folder is root)
    Else --> go down a level

    Parameters
    ----------
    current_folder : str
        path//to//current//folder
    target : str
        target folder (can be "..")

    Returns
    -------
    current_folder : str
        updated//path//to//current//folder
    """
    # Windows + os doesn't cope well with '/' as a folder, so renamed it root
    if target == '/':
        target = 'root'
    # cd .. --> go up a level
    elif target == '..':
        if current_folder == 'root':
            pass
        else:
            current_folder = os.path.dirname(current_folder)
    # else --> go down a level
    else:
        current_folder = os.path.join(current_folder, target)

    return current_folder

def get_folder_sizes(file_sizes):
    """Get the size of each folder and subfolder

    Folder size = sum of the size of its leaf nodes.

    We iterate from the leaf-nodes up to the root

    Parameters
    ----------
    file_sizes : dict
        key: path//to//file (str)
        value: file size (int)

    Returns
    -------
    dict
        key: path//to//folder (str)
        value: file size (int)
    """
    folder_sizes = {}
    for file_path, size in file_sizes.items():
        folder_path = os.path.dirname(file_path)

        while folder_path != '':
            if folder_path in folder_sizes:
                folder_sizes[folder_path] += size
            else:
                folder_sizes[folder_path] = size

            folder_path = os.path.dirname(folder_path)

    return folder_sizes

def main(file_path):
    """Main script for day 7.

    Parameters
    ----------
    file_path : str
        Path to input file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read()[:-1].split('\n')

    current_folder = 'root'
    cmd = ''
    file_sizes = {}

    for line in lines:
        cmd_parts = line.split(' ')
        if line[0] == '$':
            cmd = cmd_parts[1]
            if cmd == 'cd':
                current_folder = update_current_folder(current_folder, target=cmd_parts[2])
            elif cmd == 'ls':
                # ls doesn't update the level
                continue
            else:
                raise ValueError(f'{cmd} is not recognized as an internal or external command.')
        else:
            if cmd == 'ls':
                outputs = line.split(' ')
                if outputs[0] == 'dir':
                    continue
                else:
                    file_size, file_name = outputs
                    file_sizes[os.path.join(current_folder, file_name)] = int(file_size)
            else:
                continue

    # Part 1
    folder_sizes = get_folder_sizes(file_sizes)

    print(sum([folder_size for folder_size in folder_sizes.values() if folder_size <= 100000]))

    # Part 2
    TOTAL_SPACE = 70000000
    NEEDED_SPACE = 30000000
    UNUSED_SPACE = TOTAL_SPACE - folder_sizes['root']
    print(min([size for size in folder_sizes.values()  if UNUSED_SPACE + size >= NEEDED_SPACE]))


if __name__ == '__main__':
    main('input/day7.txt')
