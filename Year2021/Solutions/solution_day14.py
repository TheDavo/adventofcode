# ADVENT OF CODE DAY 14 #####

# Link to problem: https://adventofcode.com/2021/day/14

# ADVENT OF CODE DAY 14 #####

import os
from timeit import default_timer as timer

dirname = os.path.dirname(__file__)
input_path_problem = os.path.join(dirname, '../Inputs/input_day14.txt')
input_path_test = os.path.join(dirname, '../TestInputs/test_input_day14.txt')

test = True


def get_input(input_path):
    template = ''
    pair_insertions = {}

    with open(input_path) as open_file:
        template = open_file.readline().strip()
        _ = open_file.readline()

        for line in open_file:
            split_insertion = line.strip().split(' -> ')
            pair_insertions[split_insertion[0]] = split_insertion[1]

    return template, pair_insertions


def solve_part_one(template, pair_insertions):
    pass


def solve_part_two(template, pair_insertions):
    pass


def create_polymer(template, pair_insertions, num_steps):
    pass


# TESTING
if test:

    template, pair_insertions = get_input(input_path_test)
    num_steps = 0
    start_time = timer()
    sol_1 = solve_part_one(template, pair_insertions, num_steps)
    sol_2 = solve_part_two(template, pair_insertions, num_steps)
else:
    # REAL PROBLEM
    template, pair_insertions = get_input(input_path_problem)
    num_step = 0
    start_time = timer()
    sol_1 = solve_part_one(template, pair_insertions, num_steps)
    sol_2 = solve_part_two(template, pair_insertions, num_steps)

print('The solution to Day 1 Problem 1 is {}'.format(sol_1))
print('The solution to Day 1 Problem 2 is {}'.format(sol_2))
elapsed_time = timer() - start_time
print('The total elapsed time was {:.2f} ms'.format((elapsed_time*1000)))
