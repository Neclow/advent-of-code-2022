"""Day 4 of AoC."""
import re

def main():
    """Day 4 of AoC."""
    with open('input/day4.txt', 'r', encoding='utf-8') as input_file:
        pairs = input_file.read()[:-1].split('\n')

    # Part 1
    fully_contained_pairs = 0

    overlapping_pairs = 0

    for pair in pairs:
        item1, item2, item3, item4 = [int(i) for i in re.findall(r'\d+', pair)]

        set1, set2 = set(range(item1, item2+1)), set(range(item3, item4+1))

        if set1.issubset(set2) | set2.issubset(set1):
            fully_contained_pairs += 1

        if not set1.isdisjoint(set2):
            overlapping_pairs += 1

    print(fully_contained_pairs)

    # Part 2
    print(overlapping_pairs)

if __name__ == '__main__':
    main()
