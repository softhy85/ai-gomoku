#!/usr/bin/env python3

import sys
from spacesFunctions import *

def find_best_case(arr, nbStop):
    bestNb = 0
    bestSpace = 0
    bestStraight = 0
    bestScore = 0
    i = 0

#    print("arr", arr)
    for i in range(0, nbStop):
        if (arr[i][2] == 4 and arr[i][1] > 0):
            bestNb = arr[i][0]
            bestSpace = arr[i][1]
            bestStraight = arr[i][2]
            bestScore = 18
            continue
        if (arr[i][2] == 5):
            bestNb = arr[i][0]
            bestSpace = arr[i][1]
            bestStraight = arr[i][2]
            bestScore = 20
            continue
        if int(arr[i][0]) + int(arr[i][1]) < 5:
            continue
        if ((int(arr[i][0]) * int(arr[i][1])) + int(arr[i][2])) > bestScore:
            bestNb = arr[i][0]
            bestSpace = arr[i][1]
            bestStraight = arr[i][2]
            bestScore = ((int(arr[i][0]) * int(arr[i][1])) + int(arr[i][2]))

    return (bestNb, bestSpace, bestStraight, bestScore)

def find_hor_with_spaces(board, x, y, boardSize, c, o):
    nb = []
    arr = []

    nbTmp, spacesTmp, bLong = start_left_hor_with_spaces(board, x, y, boardSize, c, o)
    nb.append(nbTmp)
    nb.append(spacesTmp)
    nb.append(bLong)
    arr.append(nb)
    nbTmp, spacesTmp, bLong = start_right_hor_with_spaces(board, x, y, boardSize, c, o)
    nb = []
    nb.append(nbTmp)
    nb.append(spacesTmp)
    nb.append(bLong)
    arr.append(nb)
    return (find_best_case(arr, 2))

def find_ver_with_spaces(board, x, y, boardSize, c, o):
    nb = []
    arr = []

    nbTmp, spacesTmp, bLong = start_left_ver_with_spaces(board, x, y, boardSize, c, o)
    nb.append(nbTmp)
    nb.append(spacesTmp)
    nb.append(bLong)
    arr.append(nb)
    nb = []
    nbTmp, spacesTmp, bLong = start_right_ver_with_spaces(board, x, y, boardSize, c, o)
    nb.append(nbTmp)
    nb.append(spacesTmp)
    nb.append(bLong)
    arr.append(nb)
    return (find_best_case(arr, 2))

def find_diag_with_spaces(board, x, y, boardSize, c, o):
    nb = []
    arr = []

    nbTmp, spacesTmp, bLong = start_left_bot_diag_with_spaces(board, x, y, boardSize, c, o)
    nb.append(nbTmp)
    nb.append(spacesTmp)
    nb.append(bLong)
    arr.append(nb)
    nb = []
    nbTmp, spacesTmp, bLong = start_right_bot_diag_with_spaces(board, x, y, boardSize, c, o)
    nb.append(nbTmp)
    nb.append(spacesTmp)
    nb.append(bLong)
    arr.append(nb)
    nb = []
    nbTmp, spacesTmp, bLong = start_left_top_diag_with_spaces(board, x, y, boardSize, c, o)
    nb.append(nbTmp)
    nb.append(spacesTmp)
    nb.append(bLong)
    arr.append(nb)
    nb = []
    nbTmp, spacesTmp, bLong = start_right_top_diag_with_spaces(board, x, y, boardSize, c, o)
    nb.append(nbTmp)
    nb.append(spacesTmp)
    nb.append(bLong)
    arr.append(nb)
    return (find_best_case(arr, 4))

def find_with_three_spaces_max(board, x, y, boardSize, c, o):
    arr = []
    nb = []

#    board[y][x] = c

    nbStock, spacesStock, straight, tmp = find_hor_with_spaces(board, x, y, boardSize, c, o)
    nb.append(nbStock)
    nb.append(spacesStock)
    nb.append(straight)
    arr.append(nb)
    nb = []
    nbStock, spacesStock, straight, tmp = find_ver_with_spaces(board, x, y, boardSize, c, o)
    nb.append(nbStock)
    nb.append(spacesStock)
    nb.append(straight)
    arr.append(nb)
    nb = []
    nbStock, spacesStock, straight, tmp = find_diag_with_spaces(board, x, y, boardSize, c, o)
    nb.append(nbStock)
    nb.append(spacesStock)
    nb.append(straight)
    arr.append(nb)
    nb, spaces, straight, bestScore = find_best_case(arr, 3)
#    print(nb, spaces, straight, bestScore)
    return (bestScore)

# def main():
#     board = [[0 for x in range(5)] for y in range(5)]
#     yF = 3
#     xF = 3

#     for h in range(5):
#         for v in range(5):
#             board[h][v] = '.'
#     board[0][0] = 'x'
#     board[0][1] = 'x'
#     board[1][1] = 'x'
#     board[0][2] = 'o'
#     board[1][2] = 'o'
#     board[2][2] = 'o'
#     board[3][2] = 'o'
#     board[4][2] = 'x'
#     board[yF][xF] = 'o'

#     y = yF
#     x = xF
#     boardSize = 5
#     c = 'o'
#     o = 'x'
#     for key in board:
#         for mo in key:
#             print(mo, end="")
#         print("")
#     bestscore = find_with_three_spaces_max(board, x, y, boardSize, c, o)

# main()
