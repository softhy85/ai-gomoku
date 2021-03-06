import os

def create_new_board(boardSize):
    board = [[0 for k in range(boardSize)] for z in range(boardSize)]
    for y in range(boardSize):
        for x in range(boardSize):
            board[y][x] = '.'
    return (board)

def open_board_file():
    filename = "board.txt"
    try:
        with open(filename) as r:
            returnValue = r.read()
    except IOError:
        raise(Exception("Failed to open board.txt"))
    return (returnValue)

# def change_board(board):
#     if os.path.exists('board.txt'):
#         os.remove('board.txt')
#     file = open('board.txt', 'w+')

#     for line in board:
#         lh = len(line) - 1
#         for i in range(lh):
#             file.write(line[i])
#             file.write(" ")
#         file.write(line[lh])
#         file.write("\n")
#     return (board)

def add_move_to_board(x, y, boardSize, board, player):
    try:
        if player == 1:
            c = 'o'
        else:
            c = 'x'
        if (board[y][x] == '.'):
            board[y][x] = c
        else:
            raise(Exception("Expected answer:\ntwo numbers separated by comma - coordinates of the brain's move"))
    except Exception as e:
        print(e)
    return (board)

def check_values(values, boardSize):
    if values == "DONE":
        return (True, 0, 0, 0)
    (x, y, player) = values.split(",")
    if (x.isnumeric() and y.isnumeric() and player.isnumeric()):
        x = int(x)
        y = int(y)
        player = int(player)
        if (x >= 0 and x < boardSize or y >= 0 and y < boardSize and (player == 1 or player == 2)):
            return (False, x, y, player)
    else:
        return (True, x, y, player)

def print_board(board):
    for line in board:
        print(" ", end='')
        for i in range(len(line)):
            if i != len(line) - 1:
                print(line[i], " ", sep = "", end="")
            else:
                print(line[i])
    print("")
    return (0)

def turn_engine(inputValue, boardSize, board):
    args = inputValue.split(" ")[1]
    args = args.split(",")
    if len(args) != 2:
        raise(Exception("Expected answer:\ntwo numbers separated by comma - coordinates of the brain's move"))
    try:
        x = int(args[0])
        y = int(args[1])
    except ValueError:
        raise(Exception("Expected answer:\ntwo numbers separated by comma - coordinates of the brain's move"))
    if x > boardSize or x < 0 or y > boardSize or y < 0 or board[y][x] != '.':
        raise(Exception("Expected answer:\ntwo numbers separated by comma - coordinates of the brain's move"))
    board = add_move_to_board(x, y, boardSize, board, 1)
    return (board)

def board_engine(boardSize, board):
    value = input()

    while value != "DONE":
        try:
            error, x, y, player = check_values(value, boardSize)
            if not error and board[y][x] == '.' and player == 1:
                board[y][x] = 'o'
            elif not error and board[y][x] == '.' and player == 2:
                board[y][x] = 'x'
            else:
                raise(Exception("Expected answer:\nthree numbers separated by comma - moves of players"))
        except Exception as e:
            print(e)
#        print_board(board)
        value = input()
    return (board)
