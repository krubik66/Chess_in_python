from chessPieces.chessPiece import ChessPiece

class Rook(ChessPiece):

    def __init__(self, isWhite: bool) -> None:
        super().__init__('rook', 5, isWhite, 'images/4.png')
        self.moved = False