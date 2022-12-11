"""Day 1 of AoC."""

def main():
    with open('input/day1.txt', 'r', encoding='utf-8') as f:
        elf_calories = f.read()[:-1].split('\n\n')

    sum_elf_calories = [sum([int(cal) for cal in ec.split('\n')]) for ec in elf_calories]
    # Part 1
    print(max(sum_elf_calories))

    # Part 2
    print(sum(sorted(sum_elf_calories)[::-1][:3]))

if __name__ == '__main__':
    main()
