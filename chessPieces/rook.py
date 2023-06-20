from chessPieces.chessPiece import ChessPiece

class Rook(ChessPiece):

    def __init__(self, isWhite: bool) -> None:
        if isWhite:
            im = 'images/wRook.png'
        else:
            im = 'images/bRook.png'
        super().__init__('rook', 5, isWhite, im)
        self.moved = False