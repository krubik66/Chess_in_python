from chessPieces.chessPiece import ChessPiece

class Knight(ChessPiece):

    def __init__(self, isWhite: bool) -> None:
        if isWhite:
            im = 'images/wKnight.png'
        else:
            im = 'images/bKnight.png'
        super().__init__('knight', 3, isWhite, im)