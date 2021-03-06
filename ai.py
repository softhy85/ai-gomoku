#!/usr/bin/env python3

from random import randrange

from manageBoard import open_board_file, check_values, add_move_to_board, print_board

from copy import copy, deepcopy

from find234s import find_with_three_spaces_max as calcule_value

def check(board, x, y, boardSize, minOrMax):

    if (minOrMax):
        board[y][x] = 'X'
#        print("")
#        print_board(board)
        board[y][x] = 'x'
        value = calcule_value(board, x, y, boardSize, 'x', 'o')
    else:
        board[y][x] = 'O'
#        print("")
#        print_board(board)
        board[y][x] = 'o'
        value = -1 * calcule_value(board, x, y, boardSize, 'o', 'x')

    board[y][x] = '.'
    return (value)

def is_an_ok_move(board, boardSize, x, y):
    if ((board[y][x] == 'o' or board[y][x] == 'x')): #and board[y][x] != '.'):
        return (False)

    x_temp = 0
    y_temp = 0
    if (y > 0):
        y_temp = y - 1
    else:
        y_temp = y
    if (x > 0):
        x_temp = x - 1
        x_temptemp = x_temp
    else:
        x_temp = x
        x_temptemp = x_temp

    while (y_temp <= (y + 1) and y_temp < boardSize):
        while (x_temp <= (x + 1) and x_temp < boardSize):
            if (board[y_temp][x_temp] == 'o' or board[y_temp][x_temp] == 'x'):
                return (True)
            x_temp += 1
        x_temp = x_temptemp
        y_temp += 1
    return (False)

def recursive_fun(boardTemp, boardSize, x, y, end, iteration):
    board = deepcopy(boardTemp)
    iteration += 1
    minOrMax = (iteration % 2 == 0)
    value = 0
    end -= 1

    if (minOrMax):
        valueEnd = -100
        board[y][x] = 'o'
    else:
        valueEnd = 100
        board[y][x] = 'x'

    for y in range(boardSize):
        for x in range(boardSize):
            if (is_an_ok_move(board, boardSize, x, y)):
                value = check(board, x, y, boardSize, minOrMax)
                if (end > 0):
                    value = recursive_fun(board, boardSize, x, y, end, iteration)
#                print(end=" ")
#                for i in range(iteration):
#                    print("-", end="")
#                print(' ', x, y, value, "max" if minOrMax else "min", end=" ")
                if (minOrMax and value > valueEnd):
                    valueEnd = value
                elif  (not minOrMax and value < valueEnd):
                    valueEnd = value
#                print(valueEnd)
    return (valueEnd)

def brain_engine(boardSize, board):
    end = 1
    xFinal = yFinal = value = 0
    valueEnd = -100

    for y in range(boardSize):
        for x in range(boardSize):
            if (is_an_ok_move(board, boardSize, x, y)):
                value = check(board, x, y, boardSize, True)
                if (end > 0):
                    value = recursive_fun(board, boardSize, x, y, end, 0)
#                print(" ", x, y, value, "max", end=" ")
                if (value > valueEnd):
                    valueEnd = value
                    xFinal = x
                    yFinal = y
#                print(valueEnd)
#                print("______________________________________________________")

#    print("Final Value : ", valueEnd)
    # Choisir le bon emplacement
    board[yFinal][xFinal] = 'x'
#    print_board(board)
    print(xFinal, yFinal, sep=',')
    return (board)
