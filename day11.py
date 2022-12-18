"""Day 11 of AoC."""
import math
import re

from dataclasses import dataclass, field

import pandas as pd

from tqdm import tqdm

@dataclass
class Monkey:
    worry_inputs: list[str] = field(default_factory=list)
    operation: str = ''
    divider: int = 1
    true_id: int = -1
    false_id: int = -1
    count: int = 0

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

def update(monkey_dict, monkey_id, worry_inputs, operation, divider, true_id, false_id, relief_factor, divider_prod=None):
    """_summary_

    Parameters
    ----------
    monkey_dict : dict
        Monkey data
    monkey_id : str
        ID of monkey to update
    worry_inputs : list
        list of worry levels
    operation : str
        Operation applied on a worry level
    divider : int
        Test divider
    true_id : str
        Receiver monkey ID if the test is successful
    false_id : str
        Receiver monkey ID if the test is NOT successful
    relief_factor : int
        Worry relief factor
    divider_prod : int, optional
        Product of all dividers, by default None
    """
    for w in worry_inputs:
        worry_output = pd.eval(operation.replace('old', w)) // relief_factor # type: ignore
        if divider_prod is not None:
            worry_output %= divider_prod
        if worry_output % divider == 0:
            # worry_output -= 10*divider
            monkey_dict[true_id].worry_inputs.append(str(worry_output)) # type: ignore
        else:
            monkey_dict[false_id].worry_inputs.append(str(worry_output)) # type: ignore

    monkey_dict[monkey_id].worry_inputs = []
    monkey_dict[monkey_id].count += len(worry_inputs)

def main(file_path, n_rounds, relief_factor):
    """Main script for day 11.

    Parameters
    ----------
    file_path : str
        Path to input file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read()[:-1].split('\n')

    # Initialize n_monkeys
    n_monkeys = (len(lines) + 1) // 7
    monkey_dict = {str(i): Monkey() for i in range(n_monkeys)}

    # Regex to find numbers
    prog = re.compile(r'\b\d+\b')

    # First round
    for monkey_attrs in split(lines, ''):
        operation = monkey_attrs[2].split('new = ')[-1].strip()

        worry_inputs = prog.findall(monkey_attrs[1])

        # Extract data
        monkey_id, divider, true_id, false_id = [
            prog.search(monkey_attrs[i]).group() # type: ignore
            for i in [0, 3, 4, 5]
        ]

        # Update info for Monkey monkey_id
        monkey_dict[monkey_id].__dict__.update(
            {
                'operation': operation,
                'divider': int(divider),
                'true_id': true_id,
                'false_id': false_id,
                'count': 0,
            }
        )

        # Do the first round
        update(
            monkey_dict,
            monkey_id,
            worry_inputs=worry_inputs + monkey_dict[monkey_id].worry_inputs,
            operation=operation,
            divider=int(divider),
            true_id=true_id,
            false_id=false_id,
            relief_factor=relief_factor
        )

    # Product of all dividers
    # Allows to deal with smaller numbers in Part 2
    divider_prod = math.prod([monkey_dict[str(monkey_id)].divider for monkey_id in range(n_monkeys)])

    # Update for the remaining rounds
    for _ in tqdm(range(n_rounds-1)):
        for monkey_id in range(n_monkeys):
            current_monkey = monkey_dict[str(monkey_id)]
            update(
                monkey_dict,
                str(monkey_id),
                current_monkey.worry_inputs,
                current_monkey.operation,
                current_monkey.divider,
                current_monkey.true_id,
                current_monkey.false_id,
                relief_factor,
                divider_prod
            )

    # Print summary table
    final_table = pd.DataFrame({k: v.__dict__ for k, v in monkey_dict.items()}).T.infer_objects()
    print(final_table)

    # Monkey business = product ot two largest counts
    monkey_business = final_table['count'].nlargest(2).product()
    print(f'Monkey business: {monkey_business}')

if __name__ == '__main__':
    # Part 1
    main('input/day11.txt', n_rounds=20, relief_factor=3)
    # Part 2
    main('input/day11.txt', n_rounds=10000, relief_factor=1)
