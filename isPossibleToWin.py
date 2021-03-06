#!/usr/bin/env python3

def is_possible_to_win_hor(board, x, y, c, o, boardSize, nbHor):
    spaces = 0
    xStock = x
    end = False

    while (x >= 0 and end == False and spaces < (5 - nbHor)):
        if board[y][x] == o:
            end = True
        elif board[y][x] == '.':
            spaces+=1
        x-=1
    end = False
    x = xStock + 1
    while (x <= (boardSize - 1) and end == False and spaces < (5 - nbHor)):
        if board[y][x] == o:
            end = True
        elif board[y][x] == '.':
            spaces+=1
        x+=1
    if ((5 - nbHor) == spaces):
        return (True)
    return (False)

def is_possible_to_win_ver(board, x, y, c, o, boardSize, nbHor):
    spaces = 0
    yStock = y
    end = False

    while (y >= 0 and end == False and spaces < (5 - nbHor)):
        if board[y][x] == o:
            end = True
        elif board[y][x] == '.':
            spaces+=1
        y-=1
    end = False
    y = yStock + 1
    while (y <= (boardSize - 1) and end == False and spaces < (5 - nbHor)):
        if board[y][x] == o:
            end = True
        elif board[y][x] == '.':
            spaces+=1
        y+=1
    if ((5 - nbHor) == spaces):
        return (True)
    return (False)

def is_possible_to_win_diag_top_to_bot(board, x, y, c, o, boardSize, nbDiag):
    print("v")
    spaces = 0
    xStock = x
    yStock = y
    end = False

    while y <= (boardSize - 1) and x <= (boardSize - 1) and end == False and spaces < (5 - nbDiag):
        if board[y][x] == o:
            end = True
        elif board[y][x] == '.':
            spaces+=1
        y-=1
        x-=1
    end = False
    x = xStock + 1
    y = yStock + 1
    while y <= (boardSize - 1) and x <= (boardSize - 1) and end == False and spaces < (5 - nbDiag):
        if board[y][x] == o:
            end = True
        elif board[y][x] == '.':
            spaces+=1
        y+=1
        x+=1
    if ((5 - nbDiag) == spaces):
        print("can win")
        return (True)
    print("cant win")
    return (False)

def is_possible_to_win_diag_bot_to_top(board, x, y, c, o, boardSize, nbDiag):
    print("f")
    spaces = 0
    xStock = x
    yStock = y
    end = False

    while y <= (boardSize - 1) and x <= (boardSize - 1) and end == False and spaces < (5 - nbDiag):
        if board[y][x] == o:
            end = True
        elif board[y][x] == '.':
            spaces+=1
        y+=1
        x-=1
    end = False
    x = xStock + 1
    y = yStock - 1
    while y <= (boardSize - 1) and x <= (boardSize - 1) and end == False and spaces < (5 - nbDiag):
        if board[y][x] == o:
            end = True
        elif board[y][x] == '.':
            spaces+=1
        y-=1
        x+=1
    if ((5 - nbDiag) == spaces):
        return (True)
    return (False)
