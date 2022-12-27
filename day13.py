"""Day 13 of AoC."""
from ast import literal_eval
from functools import cmp_to_key

import numpy as np


def split(sequence, sep):
    """Split a list into sublists

    Parameters
    ----------
    sequence : list
        list with a repeated separator
    sep : str
        separator

    Yields
    ------
    generator
        same as str.split but for lists
    """
    chunk = []
    for val in sequence:
        if val == sep:
            yield chunk
            chunk = []
        else:
            chunk.append(val)
    yield chunk


def compare(left, right):
    """Compare two values according to Aoc2022/day/13.

    Packet data consists of lists and integers

    Parameters
    ----------
    left : Union[list, int]
        First value (of a packet, item in a packet...)
    right : Union[list, int]
        Second value (of a packet, item in a packet...)

    Returns
    -------
    int:
        0: left == right
        1: left side is smaller
        -1: right side is smaller
    """
    l_type, r_type = type(left), type(right)

    if l_type == int and r_type == int:
        return np.sign(left - right)
    else:
        if l_type != list:
            left = [left]
        if r_type != list:
            right = [right]

        if len(left) == 0:
            return -(len(right) > 0)
        if len(right) == 0:
            return 1

        res = compare(left[0], right[0])

        return res if res else compare(left[1:], right[1:])


def main(file_path):
    """Main script for day 13.

    Parameters
    ----------
    file_path : str
        Path to input file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read()[:-1].split('\n')

    good_pairs = sum(
        [
            i+1 for i, pair in enumerate(split(lines, ''))
            if compare(literal_eval(pair[0]), literal_eval(pair[1])) <= 0
        ]
    )

    print(f'Part 1: {good_pairs}')

    packets = [literal_eval(line) for line in lines if line != ''] + [[[2]], [[6]]]

    packets.sort(key=cmp_to_key(compare))

    print(f'Part 2: {(packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)}')


if __name__ == '__main__':
    main('input/day13.txt')
