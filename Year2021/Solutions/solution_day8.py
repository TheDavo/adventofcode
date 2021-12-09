##### ADVENT OF CODE DAY 8 #####

# Link to problem: https://adventofcode.com/2021/day/8

##### ADVENT OF CODE DAY 8 #####

import os
from timeit import default_timer as timer

dirname = os.path.dirname(__file__)
input_path_problem = os.path.join(dirname,'../Inputs/input_day8.txt')
input_path_test = os.path.join(dirname, '../TestInputs/test_input_day8.txt')

test = False

def get_sev_seg_notes(input_path) -> list:
    sev_seg = []
    with open(input_path) as input_file:
        for line in input_file:
            sev_seg.append([x.split() for x in line.split(' | ')])

    return sev_seg


def solve_part_one(sev_seg_notes) -> int:
    num_unique = 0

    for note in sev_seg_notes:
        for output_note in note[1]:
            if len(output_note) in [2,3,4,7]:
                num_unique += 1

    return num_unique

def solve_part_two(sev_seg_notes) -> int:
    result = 0
    for note in sev_seg_notes:
        attempts = note[0]
        dig_out = note[1]
        print(dig_out)
        curr_out_str = ''
        signals = {}
        # Get unique signals for 1, 4, 7, 8

        for attempt in attempts:
            len_tempt = len(attempt)
            if len_tempt == 2:
                signals[1] = attempt
            elif len_tempt == 3:
                signals[7] = attempt
            elif len_tempt == 4:
                signals[4] = attempt
            elif len_tempt == 7:
                signals[8] = attempt
        

        # Use facts and logic to compare uniques to output signals

        for i, dig in enumerate(dig_out):
            curr_out = 0
            len_dig = len(dig)
            if len_dig not in signals.values():
                common_four = find_commons(dig,signals[4])
                common_one = find_commons(dig,signals[1])

            if len_dig == 2: # must be a '1'
                curr_out += 1
            elif len_dig == 4: # must be a '4'
                curr_out += 4
            elif len_dig == 3: # must be a '7'
                curr_out += 7
            elif len_dig == 7: # must be a '8'
                curr_out += 8
            elif len_dig == 5: # can be '2', '3', '5' depending on  commons
                if common_four == 2 and common_one == 1:
                    curr_out += 2
                elif common_four == 3 and common_one == 2:
                    curr_out += 3
                else:
                    curr_out += 5
            elif len_dig == 6: # can be a '9', '6', or '0' depending on commons
                if common_four == 4 and common_one == 2:
                    curr_out += 9
                elif common_four == 3 and common_one == 1:
                    curr_out += 6
                else:
                    curr_out += 0

            curr_out = curr_out * pow(10,(len(dig_out)- i - 1))
            result += curr_out
    return result
        
def find_commons(signal_one, known_signal) -> int:
    signal_one = [x for x in signal_one]
    known_signal = [x for x in known_signal]

    num_common = 0
    for sig in signal_one:
        if sig in known_signal:
            num_common += 1

    return num_common

# TESTING
if test:
    notes = get_sev_seg_notes(input_path_test)
    start_time = timer()
    sol_1 = solve_part_one(notes)
    sol_2 = solve_part_two(notes)
else:
# REAL PROBLEM
    notes = get_sev_seg_notes(input_path_problem)
    start_time = timer()
    sol_1 = solve_part_one(notes)
    sol_2 = solve_part_two(notes)

print('The solution to Day 1 Problem 1 is {}'.format(sol_1))
print('The solution to Day 1 Problem 2 is {}'.format(sol_2))
elapsed_time = timer() - start_time
print('The total elapsed time was {:.2f} ms'.format((elapsed_time*1000)))