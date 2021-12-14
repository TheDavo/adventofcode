##### ADVENT OF CODE DAY 11 #####

# Link to problem: https://adventofcode.com/2021/day/11

##### ADVENT OF CODE DAY 11 #####

import os
from timeit import default_timer as timer

dirname = os.path.dirname(__file__)
input_path_problem = os.path.join(dirname, '../Inputs/input_day11.txt')
input_path_test = os.path.join(dirname, '../TestInputs/test_input_day11.txt')

test = False


def get_input(input_path) -> dict:
    octopi_levels = {}
    with open(input_path) as input_file:
        x = 0
        y = 0
        for line in input_file:
            for octo in line.strip():
                octopi_levels[(x, y)] = int(octo)
                y += 1
            x += 1
            y = 0

    return octopi_levels


def solve_part_one(maptopi, num_days) -> int:
    num_flashes = 0
    flashed_octopi = []

    # octopus_lov, leve -> tuple, int
    for _ in range(num_days):
        for octopus_loc, level in maptopi.items():
            if octopus_loc not in flashed_octopi:
                maptopi[octopus_loc] += 1
            # Flash logic
            if maptopi[octopus_loc] > 9:
                flashed_octopi.append(octopus_loc)
                maptopi[octopus_loc] = 0

        for octopus in flashed_octopi:
            neighbors = get_neighbors(octopus, maptopi)
            for neighbor in neighbors:
                if neighbor not in flashed_octopi:
                    maptopi[neighbor] += 1
                    if maptopi[neighbor] > 9:
                        flashed_octopi.append(neighbor)
                        maptopi[neighbor] = 0

        num_flashes += len(flashed_octopi)
        flashed_octopi = []
    print(maptopi)
    return num_flashes


def solve_part_two(maptopi):
    flashed_octopi = []
    days_gone = 0
    # octopus_lov, leve -> tuple, int
    while True:
        for octopus_loc, level in maptopi.items():
            if octopus_loc not in flashed_octopi:
                maptopi[octopus_loc] += 1
            # Flash logic
            if maptopi[octopus_loc] > 9:
                flashed_octopi.append(octopus_loc)
                maptopi[octopus_loc] = 0

        for octopus in flashed_octopi:
            neighbors = get_neighbors(octopus, maptopi)
            for neighbor in neighbors:
                if neighbor not in flashed_octopi:
                    maptopi[neighbor] += 1
                    if maptopi[neighbor] > 9:
                        flashed_octopi.append(neighbor)
                        maptopi[neighbor] = 0

        days_gone += 1
        if len(flashed_octopi) == len(maptopi.keys()):
            print(maptopi)
            return days_gone
        flashed_octopi = []


def get_neighbors(loc, maptopi) -> set:
    x = loc[0]
    y = loc[1]
    neighbors = set()

    for x_nei in range(-1, 2):
        for y_nei in range(-1, 2):
            x_check = x + x_nei
            y_check = y + y_nei

            if (x_check, y_check) in maptopi.keys() and \
                    (x_check, y_check) != loc:
                neighbors.add((x_check, y_check))
    return neighbors


# TESTING
if test:
    num_days = 100
    maptopi = get_input(input_path_test)
    start_time = timer()
    sol_1 = solve_part_one(maptopi, num_days)
    maptopi = get_input(input_path_test)
    sol_2 = solve_part_two(maptopi)
else:
    # REAL PROBLEM
    num_days = 100
    maptopi = get_input(input_path_problem)
    start_time = timer()
    sol_1 = solve_part_one(maptopi, num_days)
    maptopi = get_input(input_path_problem)
    sol_2 = solve_part_two(maptopi)

print('The solution to Day 1 Problem 1 is {}'.format(sol_1))
print('The solution to Day 1 Problem 2 is {}'.format(sol_2))
elapsed_time = timer() - start_time
print('The total elapsed time was {:.2f} ms'.format((elapsed_time*1000)))
