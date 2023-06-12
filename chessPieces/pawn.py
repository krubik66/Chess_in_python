from chessPieces.chessPiece import ChessPiece

class Pawn(ChessPiece):

    def __init__(self, isWhite: bool) -> None:
        super().__init__('pawn', 1, isWhite, 'images/1.png')