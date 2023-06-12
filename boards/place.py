from chessPieces.chessPiece import ChessPiece

class Place():

    def __init__(self) -> None:
        self.possibleMove: bool = False
        self.currentPiece: ChessPiece | None = None

    def __str__(self) -> str:
        match self.currentPiece:
            case None:
                return '   '
            case ChessPiece:
                return self.currentPiece.__str__()
            
    def pictures(self):
        match self.currentPiece:
            case None:
                return '   '
            case ChessPiece:
                return self.currentPiece.returnPicture()