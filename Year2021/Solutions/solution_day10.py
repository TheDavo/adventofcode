# ADVENT OF CODE DAY 10 #####

# Link to problem: https://adventofcode.com/2021/day/10

# ADVENT OF CODE DAY 10 #####

import os
from timeit import default_timer as timer

dirname = os.path.dirname(__file__)
input_path_problem = os.path.join(dirname, '../Inputs/input_day10.txt')
input_path_test = os.path.join(dirname, '../TestInputs/test_input_day10.txt')

test = False


def get_input(input_path):
    syntax = []
    with open(input_path) as input_file:
        for line in input_file:
            syntax.append([val for val in line.strip()])

    print(syntax)
    return syntax


def solve_part_one(syntax) -> int:
    return sum([get_error_score(line) for line in syntax])


def solve_part_two(syntax) -> int:

    incomplete_lines = [line for line in syntax if get_error_score(line) == 0]

    incomplete_chunks = [get_error_list(line) for line in incomplete_lines]

    scores = [get_incomplete_score(chunks) for chunks in incomplete_chunks]

    scores.sort()

    return scores[int(len(scores) / 2)]


def get_incomplete_score(chunks) -> int:
    error_points = {')': 1, ']': 2, '}': 3, '>': 4}

    score = 0
    for chunk in chunks:
        score = score * 5
        score = score + error_points[chunk]

    return score


def get_error_score(syntax_line) -> int:
    error_score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    closing_lookup = {'(': ')', '[': ']', '{': '}', '<': '>'}
    close_chunk_stack = []
    score = 0

    for chunk in syntax_line:
        if chunk in closing_lookup.keys():
            close_chunk_stack.append(closing_lookup[chunk])
        elif chunk != close_chunk_stack.pop():
            score += error_score[chunk]

    return score


def get_error_list(syntax_line) -> list:
    closing_lookup = {'(': ')', '[': ']', '{': '}', '<': '>'}
    close_chunk_stack = []

    for chunk in syntax_line:
        if chunk in closing_lookup.keys():
            close_chunk_stack.append(closing_lookup[chunk])
        else:
            close_chunk_stack.pop()

    return reversed(close_chunk_stack)


# TESTING
if test:
    syntax = get_input(input_path_test)
    start_time = timer()
    sol_1 = solve_part_one(syntax)
    sol_2 = solve_part_two(syntax)
else:
    # REAL PROBLEM
    syntax = get_input(input_path_problem)
    start_time = timer()
    sol_1 = solve_part_one(syntax)
    sol_2 = solve_part_two(syntax)

print('The solution to Day 1 Problem 1 is {}'.format(sol_1))
print('The solution to Day 1 Problem 2 is {}'.format(sol_2))
elapsed_time = timer() - start_time
print('The total elapsed time was {:.2f} ms'.format((elapsed_time*1000)))
