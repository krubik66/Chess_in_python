from boards.place import Place

class Board():
    map: list[list[Place]] = []
    def __init__(self) -> None:
        
        for i in range(8):
            self.map.append([])
            for j in range(8):
                self.map[i].append(Place())
    
    def __str__(self) -> str:
        toReturn: str = ''
        for i in range(8):
            for j in range(8):
                toReturn += self.map[i][j].__str__()
                if j != 7:
                    toReturn += '|'
            if i != 7:
                toReturn += '\n'
                for o in range(7):
                    toReturn += '---+'
                toReturn += '---\n'
        return toReturn


if __name__ == '__main__':
    test = Board()
    print(test)