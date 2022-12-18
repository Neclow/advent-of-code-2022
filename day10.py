"""Day 10 of AoC."""

def main(file_path):
    """Main script for day 10.

    Parameters
    ----------
    file_path : str
        Path to input file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read()[:-1].split('\n')

    # Initial value
    value = 1

    # Values during each cycle
    values = []

    # CRT specs
    width = 40
    crt = ''

    # Sprite specs
    sprite_width = 3

    sprite = sprite_width * '#' + (width - sprite_width) * '.'

    for line in lines:
        if line.startswith('noop'):
            # Add cycle results
            values.append(value)
            crt += sprite[len(crt) % width]
        elif line.startswith('addx'):
            # Get increment
            increment = int(line.split(' ')[-1])

            # Add cycle results
            values.extend(2 * [value])
            crt += sprite[len(crt) % width] + sprite[(len(crt) + 1) % width]

            # Update value and sprite position
            value += increment
            sprite = (value-1) * '.' + sprite_width * '#' + (width-sprite_width-value+1) * '.'
        else:
            raise ValueError('Unknown instruction.')

    # Add result of last cycle
    values.append(value)

    # Part 1
    print(sum(i*values[i-1] for i in range(20, 240, 40)))
    # Part 2
    print('\n'.join(crt[i:i+width] for i in range(0, len(crt), width)))

if __name__ == '__main__':
    main('input/day10.txt')
