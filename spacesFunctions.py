#!/usr/bin/env python3

def start_left_hor_with_spaces(board, x, y, boardSize, c, o):
    i = spaces = nb = bLong = longTmp = bLongTmp = a = 0
    xStock = x
    end = False

    while x >= 0 and i <= 4 and spaces < 4 and end == False:
        if board[y][x] != c and board[y][x] != o:
            spaces+=1
            if longTmp > bLong:
                bLong = longTmp
            if spaces == 1:
                bLongTmp = longTmp
            longTmp = 0
            a = 0
        elif board[y][x] == o:
            end = True
            if spaces == 0:
                bLongTmp = longTmp
            longTmp = 0
            a = 0
        else:
            nb+=1
            longTmp+=1
            a = 1
        x-=1
        i+=1
    i = 0
    x = xStock + 1
    end = False
    if a != 1:
        longTmp = bLongTmp
    while x <= (boardSize - 1) and i <= 4 and spaces < 4 and end == False:
        if board[y][x] != c and board[y][x] != o:
            spaces+=1
            if longTmp > bLong:
                bLong = longTmp
            longTmp = 0
        elif board[y][x] == o:
            end = True
            if spaces == 0:
                bLongTmp = longTmp
            longTmp = 0
        else:
            nb+=1
            longTmp+=1
        x+=1
        i+=1
    if longTmp > bLong:
        bLong = longTmp
    return (nb, spaces, bLong)

def start_right_hor_with_spaces(board, x, y, boardSize, c, o):
    i = a = spaces = nb = bLong = longTmp = bLongTmp = 0
    xStock = x
    end = False

    while x <= (boardSize - 1) and i <= 4 and spaces < 4 and end == False:
        if board[y][x] != c and board[y][x] != o:
            spaces+=1
            if longTmp > bLong:
                bLong = longTmp
            if spaces == 1:
                bLongTmp = longTmp
            longTmp = 0
            a = 0
        elif board[y][x] == o:
            end = True
            if spaces == 0:
                bLongTmp = longTmp
            longTmp = 0
            a = 0
        else:
            nb+=1
            longTmp+=1
            a = 1
        x+=1
        i+=1
    i = 0
    x = xStock - 1
    end = False
    if a != 1:
        longTmp = bLongTmp
    while x >= 0 and i <= 4 and spaces < 4 and end == False:
        if board[y][x] != c and board[y][x] != o:
            spaces+=1
            if longTmp > bLong:
                bLong = longTmp
            longTmp = 0
        elif board[y][x] == o:
            end = True
        else:
            nb+=1
            longTmp+=1
        x-=1
        i+=1
    if longTmp > bLong:
        bLong = longTmp
    return (nb, spaces, bLong)

def start_left_ver_with_spaces(board, x, y, boardSize, c, o):
    i = a = spaces = nb = bLong = longTmp = bLongTmp = 0
    yStock = y
    end = False

    while y >= 0 and i <= 4 and spaces < 4 and end == False:
        if board[y][x] != c and board[y][x] != o:
            spaces+=1
            if longTmp > bLong:
                bLong = longTmp
            if spaces == 1:
                bLongTmp = longTmp
            longTmp = 0
            a = 0
        elif board[y][x] == o:
            end = True
            if spaces == 0:
                bLongTmp = longTmp
            longTmp = 0
            a = 0
        else:
            nb+=1
            longTmp+=1
            a = 1
        y-=1
        i+=1
    i = 0
    y = yStock + 1
    end = False
    if a != 1:
        longTmp = bLongTmp
    while y <= (boardSize - 1) and i <= 4 and spaces < 4 and end == False:
        if board[y][x] != c and board[y][x] != o:
            spaces+=1
            if longTmp > bLong:
                bLong = longTmp
            longTmp = 0
        elif board[y][x] == o:
            end = True
        else:
            nb+=1
            longTmp+=1
        y+=1
        i+=1
    if longTmp > bLong:
        bLong = longTmp
    return (nb, spaces, bLong)

def start_right_ver_with_spaces(board, x, y, boardSize, c, o):
    yStock = y
    end = False
    i = a = spaces = nb = bLong = longTmp = bLongTmp = 0

    while y <= (boardSize - 1) and i <= 4 and spaces < 4 and end == False:
        if board[y][x] != c and board[y][x] != o:
            spaces+=1
            if longTmp > bLong:
                bLong = longTmp
            if spaces == 1:
                bLongTmp = longTmp
            longTmp = 0
            a = 0
        elif board[y][x] == o:
            end = True
            if spaces == 0:
                bLongTmp = longTmp
            longTmp = 0
            a = 0
        else:
            nb+=1
            longTmp+=1
            a = 1
        y+=1
        i+=1
    i = 0
    y = yStock - 1
    end = False
    if a != 1:
        longTmp = bLongTmp
    while y >= 0 and i <= 4 and spaces < 4 and end == False:
        if board[y][x] != c and board[y][x] != o:
            spaces+=1
            if longTmp > bLong:
                bLong = longTmp
            longTmp = 0
        elif board[y][x] == o:
            end = True
        else:
            nb+=1
            longTmp+=1
        y-=1
        i+=1
    if longTmp > bLong:
        bLong = longTmp
    return (nb, spaces, bLong)

def start_right_bot_diag_with_spaces(board, x, y, boardSize, c, o):
    yStock = y
    xStock = x
    end = False
    i = a = spaces = nb = bLong = longTmp = bLongTmp = 0

    while y <= (boardSize - 1) and x <= (boardSize - 1) and i <= 4 and spaces < 4 and end == False:
        if board[y][x] != c and board[y][x] != o:
            spaces+=1
            if longTmp > bLong:
                bLong = longTmp
            if spaces == 1:
                bLongTmp = longTmp
            longTmp = 0
            a = 0
        elif board[y][x] == o:
            end = True
            if spaces == 0:
                bLongTmp = longTmp
            longTmp = 0
            a = 0
        else:
            nb+=1
            longTmp+=1
            a = 1
        y+=1
        x+=1
        i+=1
    i = 0
    y = yStock - 1
    x = xStock - 1
    end = False
    if a != 1:
        longTmp = bLongTmp
    while y >= 0 and x >= 0 and i <= 4 and spaces < 4 and end == False:
        if board[y][x] != c and board[y][x] != o:
            spaces+=1
            if longTmp > bLong:
                bLong = longTmp
            longTmp = 0
        elif board[y][x] == o:
            end = True
        else:
            nb+=1
            longTmp+=1
        y-=1
        x-=1
        i-=1
    if longTmp > bLong:
        bLong = longTmp
    return (nb, spaces, bLong)

def start_left_bot_diag_with_spaces(board, x, y, boardSize, c, o):
    i = spaces = nb = a = bLong = longTmp = bLongTmp = 0
    yStock = y
    xStock = x
    end = False

    while y >= 0 and x >= 0 and i <= 4 and spaces < 4 and end == False:
        if board[y][x] != c and board[y][x] != o:
            spaces+=1
            if longTmp > bLong:
                bLong = longTmp
            if spaces == 1:
                bLongTmp = longTmp
            longTmp = 0
            a = 0
        elif board[y][x] == o:
            end = True
            if spaces == 0:
                bLongTmp = longTmp
            longTmp = 0
            a = 0
        else:
            nb+=1
            longTmp+=1
            a = 1
        y-=1
        x-=1
        i+=1
    i = 0
    y = yStock + 1
    x = xStock + 1
    end = False
    if a != 1:
        longTmp = bLongTmp
    while y <= (boardSize - 1) and x <= (boardSize - 1) and i <= 4 and spaces < 4 and end == False:
        if board[y][x] != c and board[y][x] != o:
            spaces+=1
            if longTmp > bLong:
                bLong = longTmp
            longTmp = 0
        elif board[y][x] == o:
            end = True
        else:
            nb+=1
            longTmp+=1
        y+=1
        x+=1
        i+=1
    if longTmp > bLong:
        bLong = longTmp
    return (nb, spaces, bLong)


def start_left_top_diag_with_spaces(board, x, y, boardSize, c, o):
    yStock = y
    xStock = x
    end = False
    i = a = spaces = nb = bLong = longTmp = bLongTmp = 0

    while y <= (boardSize - 1) and x >= 0 and i <= 4 and spaces < 4 and end == False:
        if board[y][x] != c and board[y][x] != o:
            spaces+=1
            if longTmp > bLong:
                bLong = longTmp
            if spaces == 1:
                bLongTmp = longTmp
            longTmp = 0
            a = 0
        elif board[y][x] == o:
            end = True
            if spaces == 0:
                bLongTmp = longTmp
            longTmp = 0
            a = 0
        else:
            nb+=1
            longTmp+=1
            a = 1
        y+=1
        x-=1
        i+=1
    i = 0
    y = yStock - 1
    x = xStock + 1
    end = False
    if a != 1:
        longTmp = bLongTmp
    while y >= 0 and x <= (boardSize - 1) and i <= 4 and spaces < 4 and end == False:
        if board[y][x] != c and board[y][x] != o:
            spaces+=1
            if longTmp > bLong:
                bLong = longTmp
            longTmp = 0
        elif board[y][x] == o:
            end = True
        else:
            nb+=1
            longTmp+=1
        y-=1
        x+=1
        i-=1
    if longTmp > bLong:
        bLong = longTmp
    return (nb, spaces, bLong)

def start_right_top_diag_with_spaces(board, x, y, boardSize, c, o):
    yStock = y
    xStock = x
    end = False
    i = a = spaces = nb = bLong = longTmp = bLongTmp = 0

    while y >= 0 and x <= (boardSize - 1) and i <= 4 and spaces < 4 and end == False:
        if board[y][x] != c and board[y][x] != o:
            spaces+=1
            if longTmp > bLong:
                bLong = longTmp
            if spaces == 1:
                bLongTmp = longTmp
            longTmp = 0
            a = 0
        elif board[y][x] == o:
            end = True
            if spaces == 0:
                bLongTmp = longTmp
            longTmp = 0
            a = 0
        else:
            nb+=1
            longTmp+=1
            a = 1
        y-=1
        x+=1
        i+=1
    i = 0
    y = yStock + 1
    x = xStock - 1
    end = False
    if a != 1:
        longTmp = bLongTmp
    while y <= (boardSize - 1) and x >= 0 and i <= 4 and spaces < 4 and end == False:
        if board[y][x] != c and board[y][x] != o:
            spaces+=1
            if longTmp > bLong:
                bLong = longTmp
            longTmp = 0
        elif board[y][x] == o:
            end = True
        else:
            nb+=1
            longTmp+=1
        y+=1
        x-=1
        i-=1
    if longTmp > bLong:
        bLong = longTmp
    return (nb, spaces, bLong)
