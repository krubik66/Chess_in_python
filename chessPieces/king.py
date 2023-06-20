from chessPieces.chessPiece import ChessPiece

class King(ChessPiece):

    def __init__(self, isWhite: bool) -> None:
        if isWhite:
            im = 'images/wKing.png'
        else:
            im = 'images/bKing.png'
        super().__init__('king', 99, isWhite, im)
        self.moved = False