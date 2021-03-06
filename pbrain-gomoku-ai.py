#!/usr/bin/env python3

##
## PENSER A LIRE CE QUE LE JOUEUR MET EN INPUT POUR CHANGER EN TEMPS REEL (MEME PDT QUE LE BOT CALCULE) LES VALEURS POUR REFLECHIR ETC
##

import sys
import signal

from startOfTheGame import game_start
from infoGames import set_info
from aboutBot import print_bot_info
from manageBoard import turn_engine, board_engine, create_new_board, print_board
from ai import brain_engine

def check_nb_arguments(inputValue, nb):
    if len(inputValue.split(" ")) != nb:
        raise(Exception("Expected answer:\ntwo numbers separated by comma - coordinates of the brain's move"))

def check_turn(inputValue, boardSize, board):
    check_nb_arguments(inputValue, 2)
    board = turn_engine(inputValue, boardSize, board)
    board = brain_engine(boardSize, board)
    return (board)

def check_begin(inputValue, boardSize, board):
    check_nb_arguments(inputValue, 1)
    board = brain_engine(boardSize, board)
    return (board)

def check_board(inputValue, boardSize, board):
    check_nb_arguments(inputValue, 1)
    board = board_engine(boardSize, board)
    board = brain_engine(boardSize, board)
    return (board)

def check_info(inputValue):
    check_nb_arguments(inputValue, 3)
    set_info(inputValue)

def check_about(inputValue):
    check_nb_arguments(inputValue, 1)
    print_bot_info()

def redirect_to_function(inputValue, boardSize, board):
    firstArgument = inputValue.split(" ")[0]

    try:
        if firstArgument == "TURN":
            board = check_turn(inputValue, boardSize, board)
        elif firstArgument == "BEGIN":
            board = check_begin(inputValue, boardSize, board)
        elif firstArgument == "BOARD":
            board = check_board(inputValue, boardSize, board)
        elif firstArgument == "INFO":
            check_info(inputValue)
        elif firstArgument == "ABOUT":
            check_about(inputValue)
        elif firstArgument == "END":
            return (board)
        else:
            raise(Exception("Expected answer:\ntwo numbers separated by comma - coordinates of the brain's move"))
    except Exception as e:
        print(e)
    return(board)

def engine():
    inputValue = ""
    gameEnded = False
    boardSize = game_start()
    board = create_new_board(boardSize)

    while inputValue != "END" and gameEnded != True and boardSize > 0:
        inputValue = input("")
        board = redirect_to_function(inputValue, boardSize, board)
        #print_board(board)

def signal_handler(signal, frame):
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    engine()
    sys.exit(0)

sys.setrecursionlimit(10**6)
main()
