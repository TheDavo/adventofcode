# ADVENT OF CODE DAY 5 #####

# Link to problem: https://adventofcode.com/2021/day/5

# ADVENT OF CODE DAY 5 #####

import os
import re
from timeit import default_timer as timer

dirname = os.path.dirname(__file__)
input_path_problem = os.path.join(dirname, '../Inputs/input_day5.txt')
input_path_test = os.path.join(dirname, '../TestInputs/test_input_day5.txt')

test = False

"""
    Returns a list of the vents in this problem
    vents: list of lists which are in the format of [x1, y1, x2, y2]
"""


def get_vents(input_path) -> list:

    with open(input_path) as input_file:
        vents = []
        for line in input_file:
            matched_vents_re = re.match("(\d+),(\d+) -> (\d+),(\d+)", line)
            vents.append((int(x) for x in matched_vents_re.groups()))

    return vents


def solve_part_one(input_path):
    vents = get_vents(input_path)

    vents_dict = {}

    for vent in vents:
        x1, y1, x2, y2 = [val for val in vent]
        # print('{},{} -> {},{}'.format(x1,y1,x2,y2))
        if x1 == x2:  # Horizontal line
            for y in range(min(y1, y2), max(y1, y2)+1):
                # print('x{},y{}'.format(x1,y))
                if (x1, y) not in vents_dict.keys():
                    vents_dict[(x1, y)] = 0
                vents_dict[(x1, y)] = vents_dict[(x1, y)] + 1

        if y1 == y2:  # Vertical line
            for x in range(min(x1, x2), max(x1, x2)+1):
                # print('x{},y{}'.format(x,y1))
                if (x, y1) not in vents_dict.keys():
                    vents_dict[(x, y1)] = 0
                vents_dict[(x, y1)] = vents_dict[(x, y1)] + 1

    num_overlap = 0
    for value in vents_dict.values():
        if value >= 2:
            num_overlap += 1

    return num_overlap


def solve_part_two(input_path):
    vents = get_vents(input_path)

    vents_dict = {}

    for vent in vents:
        x1, y1, x2, y2 = [val for val in vent]

        # Determine rise and run, since problem states purely 45degree angles
        # this is used to judge direction of line
        rise = y2 - y1
        run = x2 - x1

        # Normalize rise and run, since we are finding all integer points
        # between start and stop points
        if rise != 0:
            if rise < 0:
                rise = -1 * int(rise / rise)
            else:
                rise = int(rise/rise)
        if run != 0:
            if run < 0:
                run = -1 * int(run/run)
            else:
                run = int(run/run)

        # print('For vent system of {},{} -> {},{}\n'.format(x1,y1,x2,y2))

        while x1 != x2 or y1 != y2:
            if (x1, y1) not in vents_dict.keys():
                vents_dict[(x1, y1)] = 0
            vents_dict[(x1, y1)] = vents_dict[(x1, y1)] + 1

            x1 += run
            y1 += rise
            if x1 == x2 and y1 == y2:
                if (x1, y1) not in vents_dict.keys():
                    vents_dict[(x1, y1)] = 0
                vents_dict[(x1, y1)] = vents_dict[(x1, y1)] + 1
            # print('Latest change x1 {}, y1 {}'.format(x1,y1))

    num_overlap = 0
    for key, value in vents_dict.items():
        # print('Vent {}, nums overlapped: {}'.format(key,value))
        if value >= 2:
            num_overlap += 1

    return num_overlap


# TESTING
if test:
    start_time = timer()
    sol_1 = solve_part_one(input_path_test)
    sol_2 = solve_part_two(input_path_test)
else:
    # REAL PROBLEM
    start_time = timer()
    sol_1 = solve_part_one(input_path_problem)
    sol_2 = solve_part_two(input_path_problem)

print('The solution to Day 1 Problem 5 is {}'.format(sol_1))
print('The solution to Day 1 Problem 5 is {}'.format(sol_2))
elapsed_time = timer() - start_time
print('The total elapsed time was {:.2f} ms'.format((elapsed_time*1000)))
