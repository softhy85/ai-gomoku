#!/usr/bin/env python3

from infoGames import set_info
from aboutBot import print_bot_info

def check_number(nbr):
    if nbr.isnumeric() == False:
        return(False)
    if int(nbr) <= 0:
        return (False)
    return (True)

def get_start():
    inputValue = input("")

    if inputValue == "END":
        return(True, -2)
    try:
        inputValue = inputValue.split(" ")
        if inputValue[0] == "ABOUT" and len(inputValue) == 1:
            print_bot_info()
            return (False, -3)
        if inputValue[0] == "INFO" and len(inputValue) == 3:
            set_info(inputValue)
            return (False, -3)
        if len(inputValue) == 1 and inputValue[0] == "START":
            #create_new_board_file(20)
            return(True, 20)
        if len(inputValue) != 2:
            return (False, -1)
        if inputValue[0] == "START" and check_number(inputValue[1]) == True:
            #create_new_board_file(int(inputValue[1]))
            return(True, int(inputValue[1]))
        else:
            return (False, -1)
    except ValueError:
        return (False, -1)

def game_start():
    gameStarted = False
    boardSize = 0

    while gameStarted != True:
        gameStarted, boardSize = get_start()
        if gameStarted == False and boardSize != -3:
            print("ERROR message - unsupported size or other error")
        elif boardSize != -2 and boardSize != -3:
            print("OK - everything is good")
    return (boardSize)
