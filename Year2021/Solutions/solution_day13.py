# ADVENT OF CODE DAY 13 #####

# Link to problem: https://adventofcode.com/2021/day/13

# ADVENT OF CODE DAY 13 #####

import os
from timeit import default_timer as timer

dirname = os.path.dirname(__file__)
input_path_problem = os.path.join(dirname, '../Inputs/input_day13.txt')
input_path_test = os.path.join(dirname, '../TestInputs/test_input_day13.txt')

test = False


def get_input(input_path):
    paper = {}  # Dictionary of hash_loc[(y,x)] = '#''
    fold_along = []  # Will be tuple of (axis, amount)
    with open(input_path) as input_file:
        for line in input_file:
            if ',' in line:  # this is a # location
                locs = [int(x) for x in line.strip().split(',')]
                paper[locs[0], locs[1]] = '#'
            elif '=' in line:
                instruct = line.strip().split('=')
                fold_along.append((instruct[0].split()[2], int(instruct[1])))

    return fold_along, paper


def solve_part_one(fold_along, paper):
    return len(fold_paper(fold_along, paper.copy(), True))


def solve_part_two(fold_along, paper):
    folded_paper = fold_paper(fold_along, paper, False)

    # To print paper, let's get size of the paper
    max_x, max_y = 0, 0
    for key in folded_paper.keys():
        max_x = max(max_x, key[0])
        max_y = max(max_y, key[1])

    print(max_x, max_y)
    printed_paper = ''
    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x, y) not in folded_paper.keys():
                printed_paper += '.'
            else:
                printed_paper += folded_paper[(x, y)]
        printed_paper += '\n'

    print(printed_paper)
    return 0


def fold_paper(fold_along, paper, once=False):

    for instruction in fold_along:
        if instruction[0] == 'y':
            # Get list of all '#' that are below the fold line
            fold_line = instruction[1]
            fold_keys = [key for key in paper.keys() if key[1] > fold_line]
            # Math for new 'y' location (same 'x') is:
            # 1-> diff_y = cur_y - fold_line
            # 2-> new_y =  fold_line - diff_y
            for key in fold_keys:
                print(key)
                diff_y = key[1] - fold_line
                new_y = fold_line - diff_y
                paper[(key[0], new_y)] = '#'
                paper.pop(key)
        elif instruction[0] == 'x':
            # Get list of all '#' that are to the right the fold line
            fold_line = instruction[1]
            fold_keys = [key for key in paper.keys() if key[0] > fold_line]

            # Math for new 'y' location (same 'x') is:
            # 1-> diff_x = cur_x - fold_line
            # 2-> new_x =  fold_line - diff_x
            for key in fold_keys:
                diff_x = key[0] - fold_line
                new_x = fold_line - diff_x
                paper[(new_x, key[1])] = '#'
                paper.pop(key)
        if once:
            break
    return paper


# TESTING
if test:

    fold_along, paper = get_input(input_path_test)
    start_time = timer()
    sol_1 = solve_part_one(fold_along, paper)
    sol_2 = solve_part_two(fold_along, paper)
else:
    # REAL PROBLEM
    fold_along, paper = get_input(input_path_problem)
    start_time = timer()
    sol_1 = solve_part_one(fold_along, paper)
    sol_2 = solve_part_two(fold_along, paper)

print('The solution to Day 13 Problem 1 is {}'.format(sol_1))
print('The solution to Day 13 Problem 2 is {}'.format(sol_2))
elapsed_time = timer() - start_time
print('The total elapsed time was {:.2f} ms'.format((elapsed_time*1000)))
