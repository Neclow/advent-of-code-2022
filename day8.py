"""Day 8 of AoC."""
import numpy as np

def main(file_path):
    """Main script for day 8.

    Parameters
    ----------
    file_path : str
        Path to input file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read()[:-1].split('\n')

    arr = np.array([list(line) for line in lines], dtype=int)

    # Part 1
    n_visible = arr.shape[0]*2 + arr.shape[1]*2 - 4

    # Part 2
    scenic_scores = np.ones_like(arr)
    scenic_scores[[0, -1], :] = 0
    scenic_scores[:, [0, -1]] = 0

    for i in range(1, arr.shape[0]-1):
        for j in range(1, arr.shape[1]-1):
            lrtb = [
                arr[:i, j][::-1], # left
                arr[i+1:, j], # right
                arr[i, :j][::-1], # top
                arr[i, j+1:] # bottom
            ]

            # Part 1
            for trees in lrtb:
                if all([arr[i, j] > tree for tree in trees]):
                    n_visible += 1
                    break

            # Part 2
            for trees in lrtb:
                blocked = np.where(arr[i, j] <= trees)[0]
                if len(blocked) == 0:
                    scenic_scores[i, j] *= len(trees)
                else:
                    scenic_scores[i, j] *= blocked[0] + 1

    # Part 1
    print(n_visible)
    # Part 2
    print(scenic_scores.max())

if __name__ == '__main__':
    main('input/day8.txt')
