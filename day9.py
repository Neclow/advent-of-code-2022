"""Day 9 of AoC."""
def move_tail(head_pos, tail_pos):
    """Move the tail's position based on the head's position

    2 cases:
    1. The head is two steps directly up, down, left, or right from the tail:
    --> The tail must move one step in that direction

    2. The head and tail aren't touching and aren't in the same row or column
    --> The tail always moves one step diagonally

    Parameters
    ----------
    head_pos : list
        [x, y] position of the head
    tail_pos : list
        [x, y] position of the tail
    """
    diff = [head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1]]
    diff_abs = [abs(diff[0]), abs(diff[1])]

    for i in range(2):
        # Valid values of diff for a move:
        # (0, 2), (0, -2), (2, 0), (-2, 0)
        # (1, 2), (1, -2), (2, 1), (-2, 1)
        if (diff_abs[i] > 1) | (sum(diff_abs) > 2):
            tail_pos[i] += int(diff[i]/diff_abs[i])


def main(file_path, n_tails):
    """Main script for day 9.

    Parameters
    ----------
    file_path : str
        Path to input file
    n_tails : int
        Number of knots - 1
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read()[:-1].split('\n')

    positions = {i: [0, 0] for i in range(n_tails+1)}

    # Visited position by the real tail
    visited = [tuple(positions[n_tails])]

    for line in lines:
        direction, norm = line.split(' ')

        norm_dir = -1 if direction in ['L', 'D'] else 1
        axis = 0 if direction in ['U', 'D'] else 1

        for _ in range(int(norm)):
            # Move head
            positions[0][axis] += norm_dir

            # Move tails
            for i in range(n_tails):
                prev_tail = positions[i+1].copy()

                # Move the current tail depending on its head
                move_tail(positions[i], positions[i+1])

                # If the tail didn't move, don't bother moving the subsequent tails
                if prev_tail == positions[i+1]:
                    break

            # Add visited position by the real tail
            visited.append(tuple(positions[n_tails]))

    print(len(set(visited)))

if __name__ == '__main__':
    # Part 1
    main('input/day9.txt', n_tails=1)
    # Part 2
    main('input/day9.txt', n_tails=9)
