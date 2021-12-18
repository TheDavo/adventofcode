# ADVENT OF CODE DAY 12 #####

# Link to problem: https://adventofcode.com/2021/day/12

# ADVENT OF CODE DAY 12 #####

import os
from timeit import default_timer as timer

dirname = os.path.dirname(__file__)
input_path_problem = os.path.join(dirname, '../Inputs/input_day12.txt')
input_path_test = os.path.join(dirname, '../TestInputs/test_input_day12.txt')

test = False


def get_input(input_path):
    input = {}

    with open(input_path) as input_file:
        for line in input_file:
            split_line = line.strip().split('-')
            if split_line[0] not in input.keys():
                input[split_line[0]] = [split_line[1]]
            elif split_line[1] not in input[split_line[0]]:
                input[split_line[0]].append(split_line[1])

            if split_line[1] not in input.keys():
                input[split_line[1]] = [split_line[0]]
            elif split_line[0] not in input[split_line[1]]:
                input[split_line[1]].append(split_line[0])

    print(input)

    return input


def traverse_caves(input, visited_caves, current_cave, paths):

    visited_caves.append(current_cave)
    # Simple base condition
    if current_cave == 'end':
        visited_caves.append(current_cave)

        paths += 1
        return paths

    for next_cave in input[current_cave]:
        if next_cave != 'start' \
                and (next_cave.isupper()
                     or (next_cave.islower()
                         and next_cave not in visited_caves)):
            paths = traverse_caves(
                input, visited_caves.copy(), next_cave, paths)

    return paths


def traverse_caves_mod(input, visited_caves, current_cave, paths, can_revisit):
    visited_caves.append(current_cave)
    # Simple base condition
    if current_cave == 'end':
        print('Path completed')
        paths += 1
        return paths

    for next_cave in input[current_cave]:
        if next_cave == 'start':
            continue

        # print('Cave: {}->{}, can_revisit: {}'.format(current_cave,
        #                                              next_cave,
        #                                              can_revisit))

        if (next_cave.isupper() or (next_cave.islower()
                                    and next_cave not in visited_caves)):
            paths = traverse_caves_mod(
                input, visited_caves.copy(), next_cave, paths, can_revisit)
        elif next_cave.islower() and next_cave in visited_caves and can_revisit:
            paths = traverse_caves_mod(
                input, visited_caves.copy(), next_cave, paths, False)

    return paths


def solve_part_one(input):
    visited_caves = []
    num_paths = 0

    num_paths = traverse_caves(input, visited_caves, 'start', num_paths)

    return num_paths


def solve_part_two(input):
    visited_caves = []
    num_paths = 0

    num_paths = traverse_caves_mod(input, visited_caves, 'start', num_paths,
                                   True)

    return num_paths


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
