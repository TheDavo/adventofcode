##### ADVENT OF CODE DAY 1 #####

# Link to problem: https://adventofcode.com/2021/day/1

##### ADVENT OF CODE DAY 1 #####

import os
from timeit import default_timer as timer

dirname = os.path.dirname(__file__)
input_path = os.path.join(dirname, '../Inputs/input_day1.txt')

with open(input_path) as input_file:
    nums = [int(i) for i in input_file]


def solve_part_one() -> int:
    count = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            count += 1

    return count


def solve_part_two() -> int:
    count = 0
    for i in range(len(nums)-3):
        if sum(nums[i:i+3]) < sum(nums[i+1:i+1+3]):
            count += 1
    return count


start_time = timer()
sol_1 = solve_part_one()
sol_2 = solve_part_two()
print('The solution to Day 1 Problem 1 is {}.'.format(sol_1))
print('The solution to Day 1 Problem 2 is {}.'.format(sol_2))
elapsed_time = timer() - start_time
print('The total elapsed time was {:.2f} ms'.format((elapsed_time*1000)))
