##### ADVENT OF CODE DAY 4 #####

# Link to problem: https://adventofcode.com/2021/day/4

##### ADVENT OF CODE DAY 4 #####

import os
import time
from timeit import default_timer as timer

dirname = os.path.dirname(__file__)
input_path = os.path.join(dirname,'../Inputs/input_day4.txt')
#input_path = os.path.join(dirname, '../TestInputs/test_input_day4.txt')

# Parse the text file
# First line is all the numbers which will be drawn, then a newline
# After new line, five lines which are the boards, newline, then repeat

with open(input_path) as input_file:
    bingo_calls = [int(x) for x in input_file.readline().strip().split(',')] # get first line and change to int
    input_file.readline() # get rid of first '\n' after the first line is read
    # each board is separated by a '\n' characters
    boards = []
    board = []
    board_size = 5
    for line in input_file:
        if line != '\n':
            board.append([(int(x), False) for x in line.split()]) #use int(x), False to help indicate marked value
            if len(board) == 5:
                boards.append(board)
                board = []

def solve_part_one() -> int:
    for draw in bingo_calls:
        for i,board in enumerate(boards):
            for j,row in enumerate(board):
                for k,mark in enumerate(row):
                    if mark[0] == draw:
                        board[j][k] = (draw, True) # set my 'marked' values
            if bingod(board):
                board_score = get_score(board, draw)
                for row in board:
                    print(row)
                print('')
                return board_score
    
    return None

def solve_part_two() -> int:
    board_scores = []
    num_won = 0

    for draw in bingo_calls:
        for i,board in enumerate(boards):
            if not bingod(board): # only continue if board is not solved yet
                for j,row in enumerate(board):
                    for k,mark in enumerate(row):
                        if mark[0] == draw:
                            board[j][k] = (draw, True) # set my 'marked' values
                            if bingod(board) and num_won < len(boards):
                                num_won += 1
                                board_scores.append(get_score(board,draw))
    return board_scores[-1]

def bingod(board) -> bool:
    # check horizontal success
    horizontal_bingo = False
    for row in board:
        if all(draw[1] for draw in row):
            horizontal_bingo = True
            break
    

    vertical_bingo = False
    num_true = -1
    for column in range(len(board)):
        for row in range(len(board)):
            if board[row][column][1] == True:
                num_true += 1
        if num_true == 5:
            vertical_bingo = True
        else:
            num_true = 0

    return vertical_bingo or horizontal_bingo

def get_score(board, current_draw) -> int:
    score = 0
    for row in board:
        for mark in row:
            if mark[1] == False:
                score += mark[0]
    print('Score {} calculated by {} * {}'.format((score * current_draw),score, current_draw))
    return score * current_draw



start_time = timer()
#sol_1 = solve_part_one()
sol_2 = solve_part_two()
#print('The solution to Day 1 Problem 1 is {}'.format(sol_1))
print('The solution to Day 1 Problem 2 is {}'.format(sol_2))
elapsed_time = timer() - start_time
print('The total elapsed time was {:.2f} ms'.format((elapsed_time*1000)))