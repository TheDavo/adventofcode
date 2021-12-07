##### ADVENT OF CODE DAY 6 #####

# Link to problem: https://adventofcode.com/2021/day/6

##### ADVENT OF CODE DAY 6 #####

import os
from timeit import default_timer as timer

dirname = os.path.dirname(__file__)
input_path_problem = os.path.join(dirname,'../Inputs/input_day6.txt')
input_path_test = os.path.join(dirname, '../TestInputs/test_input_day6.txt')

test = False

def get_init_fish(input_path):
    
    with open(input_path) as input_file:
        lanternfish = [int(x) for x in input_file.readline().split(',')]

    return lanternfish

def solve_part_one(input_path) -> int:
    """
        The school of lanternfish have a -respawn_rate- of 7 days. Newly born fish can spawn offspring in 9 days.

        Every passing day, the counter to a new fish spawning drops, until the spawn time is 0.


    """
    lanternfish_spawn_time = get_init_fish(input_path)
    num_days = 80

    for day in range(num_days):
        for i, fish_spawn_time in enumerate(lanternfish_spawn_time):
            if fish_spawn_time == 0:
                lanternfish_spawn_time[i] = 6
                lanternfish_spawn_time.append(9) 
            else:
                lanternfish_spawn_time[i] -= 1


    return len(lanternfish_spawn_time)
                

def solve_part_two(input_path):
    """
        The school of lanternfish have a -respawn_rate- of 7 days. Newly born fish can spawn offspring in 9 days.

        Every passing day, the counter to a new fish spawning drops, until the spawn time is 0.

        This problem has num_days = 256, which breaks PC.

        Storing how many of the fish spawn rates in dictionary/list as a fish counter will ease up memory limits.
    """
    lanternfish_spawn_time = get_init_fish(input_path)
    num_days = 256

    # Generate fish dictionary and populate:
    # cooked_fish = dict.fromkeys(range(9),0)
    cooked_fish = [0] * 9

    for fish_spawn in lanternfish_spawn_time:
        cooked_fish[fish_spawn] += 1

    print(cooked_fish)

    for _ in range(num_days):
        new_fish = cooked_fish[0]
        cooked_fish = cooked_fish[1:] + cooked_fish[:1]
        cooked_fish[6] += new_fish
        # print(cooked_fish)
        # print('')

    return sum(cooked_fish)

    # for day in range(num_days):
    #     for fish_spawn in range(1,9):
    #         cooked_fish[fish_spawn-1] = cooked_fish[fish_spawn]
        
    #     cooked_fish[6] += cooked_fish[0]
    #     cooked_fish[8] = cooked_fish[0]

    #     for key,value in cooked_fish.items():
    #         print('Day {} with {} key, {} value'.format(day,key,value))
    #     print('\n')
        

    #return sum(cooked_fish.values())


# TESTING
if test:
    start_time = timer()
    sol_1 = solve_part_one(input_path_test)
    sol_2 = solve_part_two(input_path_test)
else:
# REAL PROBLEM
    start_time = timer()
    sol_1 = solve_part_one(input_path_problem)
    sol_2 = solve_part_two(input_path_problem)

print('The solution to Day 1 Problem 1 is {}'.format(sol_1))
print('The solution to Day 1 Problem 2 is {}'.format(sol_2))
elapsed_time = timer() - start_time
print('The total elapsed time was {:.2f} ms'.format((elapsed_time*1000)))
