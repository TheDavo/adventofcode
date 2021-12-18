# ADVENT OF CODE DAY 9 #####

# Link to problem: https://adventofcode.com/2021/day/9

# ADVENT OF CODE DAY 9 #####

import os
from timeit import default_timer as timer

dirname = os.path.dirname(__file__)
input_path_problem = os.path.join(dirname, '../Inputs/input_day9.txt')
input_path_test = os.path.join(dirname, '../TestInputs/test_input_day9.txt')

test = False


def get_input(input_path):
    topograph = []
    with open(input_path) as input_file:
        for line in input_file:
            topograph.append([(int(x), False) for x in line.strip()])

    return topograph


def solve_part_one(topograph):
    total_risk = 0

    for i, row in enumerate(topograph):
        can_left, can_right, can_up, can_down = False, False, False, False

        if i == 0:
            can_up, can_down = False, True
        elif i == len(topograph) - 1:
            can_up, can_down = True, False
        else:
            can_up, can_down = True, True

        # print(row)

        for j, item in enumerate(row):
            high_left, high_right, high_up, high_down = False, False, False, False
            # print(item)

            if j == 0:
                can_left, can_right = False, True
            elif j == len(row) - 1:
                can_left, can_right = True, False
            else:
                can_left, can_right = True, True
            if can_up and (topograph[i-1][j][0] > item[0]):
                high_up = True
            if can_down and (topograph[i+1][j][0] > item[0]):
                high_down = True
            if can_right and (topograph[i][j+1][0] > item[0]):
                high_right = True
            if can_left and (topograph[i][j-1][0] > item[0]):
                high_left = True

            if [can_up, can_down, can_right, can_left] == \
                    [high_up, high_down, high_right, high_left]:
                total_risk += item[0] + 1

    return total_risk


def solve_part_two(topograph):

    def search_basin(topograph, i, j, basin_size_input, compare_to):

        basin_size = basin_size_input + 1

        # print(basin_size)

        if topograph[i][j][0] == 9 or topograph[i][j][1] is True \
                or topograph[i][j][0] < compare_to:
            return basin_size - 1

        topograph[i][j] = (topograph[i][j][0], True)

        can_left, can_right, can_up, can_down = False, False, False, False

        if i == 0:
            can_up, can_down = False, True
        elif i == len(topograph) - 1:
            can_up, can_down = True, False
        else:
            can_up, can_down = True, True

        if j == 0:
            can_left, can_right = False, True
        elif j == len(topograph[i]) - 1:
            can_left, can_right = True, False
        else:
            can_left, can_right = True, True

        if can_left:
            basin_size = search_basin(
                topograph, i, j-1, basin_size, topograph[i][j][0])
        if can_right:
            basin_size = search_basin(
                topograph, i, j+1, basin_size, topograph[i][j][0])
        if can_up:
            basin_size = search_basin(
                topograph, i-1, j, basin_size, topograph[i][j][0])
        if can_down:
            basin_size = search_basin(
                topograph, i+1, j, basin_size, topograph[i][j][0])

        return basin_size

    top_basins = [0, 0, 0]

    for i, row in enumerate(topograph):
        can_left, can_right, can_up, can_down = False, False, False, False

        if i == 0:
            can_up, can_down = False, True
        elif i == len(topograph) - 1:
            can_up, can_down = True, False
        else:
            can_up, can_down = True, True

        # print(row)

        for j, item in enumerate(row):
            high_left, high_right, high_up, high_down = False, False, False, False
            # print(item)

            if j == 0:
                can_left, can_right = False, True
            elif j == len(row) - 1:
                can_left, can_right = True, False
            else:
                can_left, can_right = True, True

            if can_up and (topograph[i-1][j][0] > item[0]):
                high_up = True
            if can_down and (topograph[i+1][j][0] > item[0]):
                high_down = True
            if can_right and (topograph[i][j+1][0] > item[0]):
                high_right = True
            if can_left and (topograph[i][j-1][0] > item[0]):
                high_left = True

            # Finds a valley, from here we can explore around until we cannot
            if [can_up, can_down, can_right, can_left] == \
                    [high_up, high_down, high_right, high_left]:
                # print(i,j)
                # for row in topograph:
                #     print(row)
                # print('')
                basin_size = search_basin(topograph, i, j, 0, item[0])
                # print('Basin size: {}'.format(basin_size))
                # print(top_basins)
                if basin_size >= top_basins[0]:
                    top_basins[2] = top_basins[1]
                    top_basins[1] = top_basins[0]
                    top_basins[0] = basin_size
                elif basin_size >= top_basins[1]:
                    top_basins[2] = top_basins[1]
                    top_basins[1] = basin_size
                elif basin_size >= top_basins[0]:
                    top_basins[0] = basin_size
                # print(top_basins)
    product = 1
    for basin in top_basins:
        product *= basin

    print(top_basins)
    return product


# TESTING
if test:
    topograph = get_input(input_path_test)
    start_time = timer()
    sol_1 = solve_part_one(topograph)
    sol_2 = solve_part_two(topograph)
else:
    # REAL PROBLEM
    topograph = get_input(input_path_problem)
    start_time = timer()
    sol_1 = solve_part_one(topograph)
    sol_2 = solve_part_two(topograph)

print('The solution to Day 1 Problem 1 is {}'.format(sol_1))
print('The solution to Day 1 Problem 2 is {}'.format(sol_2))
elapsed_time = timer() - start_time
print('The total elapsed time was {:.2f} ms'.format((elapsed_time*1000)))
