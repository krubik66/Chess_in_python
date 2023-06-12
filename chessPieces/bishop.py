from chessPieces.chessPiece import ChessPiece

class Bishop(ChessPiece):

    def __init__(self, isWhite: bool) -> None:
        super().__init__('bishop', 3, isWhite, 'images/2.png')