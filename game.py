from GUI import GUI
from boards.board import Board
from player import Player
import pygame
import sys
import pickle
from saving import Save_data

if __name__ == '__main__':
    pygame.init()

    board  = Board()
    whites = Player('w', board)
    blacks = Player('b', board)

    GUI(board, whites, blacks)

    pygame.quit()
    sys.exit()
