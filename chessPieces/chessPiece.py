import abc
from PIL import Image

class ChessPiece(abc.ABC):

    def __init__(self, name: str, points: int, isWhite: bool, picture: str) -> None:
        self.name: str = name
        self.points: int = points
        self.isWhite: bool = isWhite
        self.picture = self.getPicture(picture)
        self.link = picture

    def getPicture(self, file: str):
        return Image.open(file)
    
    def returnPicture(self):
        return self.picture

    def __str__(self) -> str:
        if self.isWhite:
            colour = 'W'
        else:
            colour = 'B'
        return f' {self.name} ({colour})'