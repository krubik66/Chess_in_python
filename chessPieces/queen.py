from chessPieces.chessPiece import ChessPiece

class Queen(ChessPiece):

    def __init__(self, isWhite: bool) -> None:
        if isWhite:
            im = 'images/wQueen.png'
        else:
            im = 'images/bQueen.png'
        super().__init__('queen', 9, isWhite, im)