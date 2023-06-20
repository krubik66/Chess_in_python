from chessPieces.chessPiece import ChessPiece

class Pawn(ChessPiece):
    
    def __init__(self, isWhite: bool) -> None:
        if isWhite:
            im = 'images/wPawn.png'
        else:
            im = 'images/bPawn.png'
        super().__init__('pawn', 1, isWhite, im)