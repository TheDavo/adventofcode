# ADVENT OF CODE DAY 2 #####

# Link to problem: https://adventofcode.com/2021/day/2

# ADVENT OF CODE DAY 2 #####

import os
from timeit import default_timer as timer

dirname = os.path.dirname(__file__)
input_path = os.path.join(dirname, '../Inputs/input_day2.txt')

# this input file is formatted as str int

with open(input_path) as input_file:
    commands = [i for i in input_file]


def solve_part_one() -> int:
    horizontal = 0
    vertical = 0

    for command in commands:
        motion, amount = command.split()

        if motion == 'forward':
            horizontal += int(amount)
        elif motion == 'up':
            vertical -= int(amount)
        elif motion == 'down':
            vertical += int(amount)

    return horizontal * vertical


def solve_part_two() -> int:
    horizontal = 0
    vertical = 0
    depth = 0

    for command in commands:
        motion, amount = command.split()

        if motion == 'forward':
            horizontal += int(amount)
            depth += vertical * int(amount)
        elif motion == 'up':
            vertical -= int(amount)
        elif motion == 'down':
            vertical += int(amount)

    return horizontal * depth


start_time = timer()
sol_1 = solve_part_one()
sol_2 = solve_part_two()
print('The solution to Day 2 Problem 1 is {}.'.format(sol_1))
print('The solution to Day 2 Problem 2 is {}.'.format(sol_2))
elapsed_time = timer() - start_time
print('The total elapsed time was {:.2f} ms'.format((elapsed_time*1000)))
