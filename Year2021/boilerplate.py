# ADVENT OF CODE DAY xx #####

# Link to problem: https://adventofcode.com/2021/day/xx

# ADVENT OF CODE DAY xx #####

import os
from timeit import default_timer as timer

dirname = os.path.dirname(__file__)
input_path_problem = os.path.join(dirname, '../Inputs/input_dayxx.txt')
input_path_test = os.path.join(dirname, '../TestInputs/test_input_dayxx.txt')

test = True


def get_input(input_path):
    pass


def solve_part_one(input):
    pass


def solve_part_two(input):
    pass


# TESTING
if test:

    input = get_input(input_path_test)
    start_time = timer()
    sol_1 = solve_part_one(input)
    sol_2 = solve_part_two(input)
else:
    # REAL PROBLEM
    input = get_input(input_path_problem)
    start_time = timer()
    sol_1 = solve_part_one(input)
    sol_2 = solve_part_two(input)

print('The solution to Day 1 Problem 1 is {}'.format(sol_1))
print('The solution to Day 1 Problem 2 is {}'.format(sol_2))
elapsed_time = timer() - start_time
print('The total elapsed time was {:.2f} ms'.format((elapsed_time*1000)))
