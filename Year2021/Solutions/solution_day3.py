##### ADVENT OF CODE DAY 3 #####

# Link to problem: https://adventofcode.com/2021/day/3

##### ADVENT OF CODE DAY 3 #####

import os
import time
from timeit import default_timer as timer

dirname = os.path.dirname(__file__)
input_path = os.path.join(dirname,'../Inputs/input_day3.txt')

with open(input_path) as input_file:
    diag_report = [i.strip() for i in input_file]

def solve_part_one() -> int:
    gamma = 0
    epsilon = 0
    one_counter = 0
    zero_counter = 0

    for i in range(len(diag_report[0])):
        for diag in diag_report:
            if int(diag[i]) == 1:
                one_counter += 1
            else:
                zero_counter += 1
        if max(one_counter,zero_counter) == one_counter:
            gamma = (gamma << 1) | 1
            epsilon = (epsilon << 1) | 0
        else:
            gamma = (gamma << 1) | 0
            epsilon = (epsilon << 1) | 1
        one_counter = 0
        zero_counter = 0
        

    return gamma * epsilon


def solve_part_two() -> int:


    clean_report = diag_report[:]
    
    o2 = []
    co2 = []
    lcv = 0
    mcv = 0

    for i in range(len(clean_report[0])):
        mcv, lcv = find_common(clean_report, i)
        o2 = trim_report(clean_report, mcv, lcv, True, i)
        if len(o2) == 1:
            break
    
    clean_report = diag_report[:]

    for i in range(len(clean_report[0])):
        mcv, lcv = find_common(clean_report, i)
        co2 = trim_report(clean_report, mcv, lcv, False, i)
        if len(co2) == 1:
            break

    o2 = int(o2[0],2)

    co2 = int(co2[0],2)

    return o2 * co2
    
def find_common(report, index) -> tuple:
    ones = 0
    zeros = 0

    for diag in report:
        if int(diag[index]) == 1:
            ones += 1
        else:
            zeros += 1

    if max(ones,zeros) == ones:
        return (1,0)
    else:
        return (0,1)

def trim_report(report, mcv, lcv, use_mcv, index): # mcv = most common value
    i = 0
    while i < len(report):
        if use_mcv:
            if int(report[i][index]) != mcv:
                report.pop(i)
            else:
                i += 1
        else:
            if int(report[i][index]) != lcv:
                report.pop(i)
            else:
                i += 1

    return report


start_time = timer()
sol_1 = solve_part_one()
sol_2 = solve_part_two()
print('The solution to Day 1 Problem 1 is {}'.format(sol_1))
print('The solution to Day 1 Problem 2 is {}'.format(sol_2))
elapsed_time = timer() - start_time
print('The total elapsed time was {:.2f} ms'.format((elapsed_time*1000)))