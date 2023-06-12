from chessPieces.chessPiece import ChessPiece

class Knight(ChessPiece):

    def __init__(self, isWhite: bool) -> None:
        super().__init__('knight', 3, isWhite, 'images/3.png')