# ADVENT OF CODE DAY 7 #####

# Link to problem: https://adventofcode.com/2021/day/7

# ADVENT OF CODE DAY 7 #####

import os
from timeit import default_timer as timer

dirname = os.path.dirname(__file__)
input_path_problem = os.path.join(dirname, '../Inputs/input_day7.txt')
input_path_test = os.path.join(dirname, '../TestInputs/test_input_day7.txt')

test = False


def get_init_pos(input_path):

    with open(input_path) as input_file:
        crab_pos = [int(x) for x in input_file.readline().split(',')]

    return crab_pos


def solve_part_one(my_crabs):
    crab_pos = my_crabs

    crab_book = dict.fromkeys([crab for crab in crab_pos], 0)
    for crab in crab_pos:
        crab_book[crab] += 1

    min_crab, max_crab = min(crab_pos), max(crab_pos)
    crab_range = range(min_crab, max_crab+1)
    fuel_costs = [0] * len(crab_range)

    for i in crab_range:
        for key, value in crab_book.items():
            fuel_costs[i] += abs(key - i) * value

    return min(fuel_costs)


def solve_part_two(my_crabs):
    crab_pos = my_crabs

    crab_book = dict.fromkeys([crab for crab in crab_pos], 0)
    for crab in crab_pos:
        crab_book[crab] += 1

    min_crab, max_crab = min(crab_pos), max(crab_pos)
    crab_range = range(min_crab, max_crab+1)
    fuel_costs = [0] * len(crab_range)

    for i in crab_range:
        for key, value in crab_book.items():
            pos_diff = abs(key-i)
            # Gauss's method of finding sum between two numbers
            fuel_costs[i] += (((pos_diff + 1)*(pos_diff)) / 2) * value

    return int(min(fuel_costs))


# TESTING
if test:
    my_crabs = get_init_pos(input_path_test)
    start_time = timer()
    sol_1 = solve_part_one(my_crabs)
    sol_2 = solve_part_two(my_crabs)
else:
    # REAL PROBLEM
    my_crabs = get_init_pos(input_path_problem)
    start_time = timer()
    sol_1 = solve_part_one(my_crabs)
    sol_2 = solve_part_two(my_crabs)

print('The solution to Day 1 Problem 7 is {}'.format(sol_1))
print('The solution to Day 1 Problem 7 is {}'.format(sol_2))
elapsed_time = timer() - start_time
print('The total elapsed time was {:.2f} ms'.format((elapsed_time*1000)))
