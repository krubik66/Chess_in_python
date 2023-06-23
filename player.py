from boards.board import Board
from chessPieces.chessPiece import ChessPiece
from chessPieces.king import King
from chessPieces.queen import Queen
from chessPieces.rook import Rook
from chessPieces.knight import Knight
from chessPieces.bishop import Bishop
from chessPieces.pawn import Pawn

class Player():

    def __init__(self, colour: str, board: Board) -> None:
        self.pieces: list[ChessPiece] = []
        self.isWhite: bool = True
        match colour[0].capitalize():
            case 'W':
                self.isWhite = True
            case 'B':
                self.isWhite = False

        self.fillMyPieces()
        self.fillBoard(board)


    def fillMyPieces(self):
        self.pieces.append(King(self.isWhite))
        self.pieces.append(Queen(self.isWhite))
        for i in range(2):
            self.pieces.append(Rook(self.isWhite))
        for i in range(2):
            self.pieces.append(Knight(self.isWhite))
        for i in range(2):
            self.pieces.append(Bishop(self.isWhite))
        for i in range(8):
            self.pieces.append(Pawn(self.isWhite))

    def fillBoard(self, board: Board):
        if not self.isWhite:
            frontline: int = 1
            backline: int = 0
            board.map[4][backline].currentPiece = self.pieces[0]
            board.map[3][backline].currentPiece = self.pieces[1]
            
        else:
            frontline: int = 6
            backline: int = 7
            board.map[3][backline].currentPiece = self.pieces[1]
            board.map[4][backline].currentPiece = self.pieces[0]

        board.map[0][backline].currentPiece, board.map[7][backline].currentPiece = self.pieces[2], self.pieces[3]
        board.map[1][backline].currentPiece, board.map[6][backline].currentPiece = self.pieces[4], self.pieces[5]
        board.map[2][backline].currentPiece, board.map[5][backline].currentPiece = self.pieces[6], self.pieces[7]


        for i in range(8, 16):
            board.map[i - 8][frontline].currentPiece = self.pieces[i]