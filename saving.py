import pickle
from boards.board import Board
from player import Player

class Save_data():
    def __init__(self, board, white, black, movementRight, movesHistory, lastMove) -> None:
        self.board: Board = board
        self.white: Player = white
        self.black: Player = black

        self.movementRight: bool = movementRight
        self.movesHistory: list[tuple[tuple]] = movesHistory
        self.lastMove:tuple[tuple] = lastMove