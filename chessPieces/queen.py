from chessPieces.chessPiece import ChessPiece

class Queen(ChessPiece):

    def __init__(self, isWhite: bool) -> None:
        super().__init__('queen', 9, isWhite, 'images/5.png')