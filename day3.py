"""Day 3 of AoC."""
import string

MAPPING = {c: i+1 for i, c in enumerate(list(string.ascii_lowercase + string.ascii_uppercase))}

if __name__ == '__main__':
    with open('input/day3.txt', 'r', encoding='utf-8') as f:
        rucksacks = f.read()[:-1].split('\n')

    # Part 1
    print(
        sum(
            MAPPING[min(set(r[:len(r) // 2]) & set(r[-len(r) // 2:]))]
            for r in rucksacks
        )
    )

    # Part 2
    print(
        sum(
           MAPPING[min(set(rucksacks[i]).intersection(*rucksacks[i+1:i+3]))]
           for i in range(0, len(rucksacks), 3)
        )
    )
