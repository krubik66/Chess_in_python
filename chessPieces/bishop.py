from chessPieces.chessPiece import ChessPiece

class Bishop(ChessPiece):

    def __init__(self, isWhite: bool) -> None:
        if isWhite:
            im = 'images/wBishop.png'
        else:
            im = 'images/bBishop.png'
        super().__init__('bishop', 3, isWhite, im)