"""Day 5 of AoC."""
import re

from argparse import ArgumentParser, BooleanOptionalAction
from pprint import pprint

def parse_args():
    """Parse a default argument to use the part one or part two crane."""
    parser = ArgumentParser(description='Arguments for day 5')

    parser.add_argument(
        '--part_two',
        type=bool,
        default=False,
        action=BooleanOptionalAction,
        help='Use the crane from part two'
    )

    return parser.parse_args()

def main(file_path, spaces):
    """Main script for day 5.

    Parameters
    ----------
    file_path : str
        Path to input file
    spaces : int
        Number of whitespaces between each stack
    """
    args = parse_args()
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read()[:-1].split('\n')

    # Separte the stacks and moves
    moves = []
    stack_lines = []

    for line in lines:
        if len(line) == 0:
            continue
        elif 'move' in line:
            moves.append(line)
        else:
            stack_lines.append(line)

    stacks = [
        [stack[i:i+spaces+1].strip() for i in range(0, len(stack), spaces+1)]
        for stack in stack_lines[:-1][::-1] # Ignore the line with the stack numbers
    ]

    # Transpose the stacks to match the desired format
    stacks = list(map(lambda x: list(filter(None, x)), zip(*stacks)))

    pprint(stacks)

    # Update the stacks at each move
    for move in moves:
        n_moves, stack1, stack2 = [int(i) for i in re.findall(r'\d+', move)]

        moved = [stacks[stack1-1].pop() for _ in range(n_moves)]

        # Use the crane from part 2 with the flag --part_two
        stacks[stack2-1] += moved[::-1] if args.part_two else moved

    # Assemble the last boxes in each stack to form the message
    print(''.join([re.findall('[A-Z]', stack[-1])[0] for stack in stacks]))

if __name__ == '__main__':
    main(file_path='input/day5.txt', spaces=3)
