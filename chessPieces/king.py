from chessPieces.chessPiece import ChessPiece

class King(ChessPiece):

    def __init__(self, isWhite: bool) -> None:
        super().__init__('king', 99, isWhite, 'images/6.png')
        self.moved = False