from chessPieces.chessPiece import ChessPiece
from boards.board import Board
from boards.place import Place
from player import Player
from chessPieces.king import King
from chessPieces.queen import Queen
from chessPieces.rook import Rook
from chessPieces.knight import Knight
from chessPieces.bishop import Bishop
from chessPieces.pawn import Pawn

def move(start: tuple[int,int], end: tuple[int,int], playboard: list[list[Place]], enemy: Player, movementRight: bool):
    x = start[0]
    y = start[1]
    startingPlace: Place = playboard[x][y]
    endingPlace: Place = playboard[end[0]][end[1]]
    if endingPlace.currentPiece != None:
        enemy.pieces.remove(endingPlace.currentPiece)
    endingPlace.currentPiece = startingPlace.currentPiece
    startingPlace.currentPiece = None
    match endingPlace.currentPiece:
        case King():
            endingPlace.currentPiece.moved = True
            if checkIfCastling(start, end):
                match end:
                    case(6, 7):
                        move((7, 7), (5, 7), playboard, enemy, movementRight)
                    case(1, 7):
                        move((0, 7), (2, 7), playboard, enemy, movementRight)
                    case(1, 0):
                        move((0, 0), (2, 0), playboard, enemy, movementRight)
                    case(6, 0):
                        move((7, 0), (5, 0), playboard, enemy, movementRight)
        case Rook():
            endingPlace.currentPiece.moved = True
    return movementRight

def checkIfCastling(start: tuple[int,int], end: tuple[int,int]):
    return abs(start[0] - end[0]) > 1

def possibleMoves(coordinates: tuple[int,int], playboard: list[list[Place]], lastMove: tuple[tuple]):
    print(f'Coordinates: {coordinates}')
    place = playboard[coordinates[0]][coordinates[1]]
    piece = place.currentPiece
    match piece:
        case None:
            return []
        case King():
            return kingMoves(coordinates, playboard)
        case Queen():
            return queenMoves(coordinates, playboard)
        case Rook():
            return rookMoves(coordinates, playboard)
        case Knight():
            return knightMoves(coordinates, playboard)
        case Bishop():
            return bishopMoves(coordinates, playboard)
        case Pawn():
            print('Please dont hurt me!')
            return pawnMoves(coordinates, playboard, lastMove)
        case _:
            raise ValueError('What am I? I cannot move')

def presentPossible(all: tuple, coordinates: tuple[int,int], playboard: list[list[Place]]):
    toReturn: list = []
    x = coordinates[0]
    y = coordinates[1]
    currentPiece = playboard[x][y].currentPiece

    for one in all:
        try:
            current = playboard[x + one[0]][y + one[1]]
            if current.currentPiece == None or current.currentPiece.isWhite != currentPiece.isWhite:
                toReturn.append((x  + one[0], y + one[1]))
        except:
            pass
    
    return toReturn

def intoDirection(direction: tuple, coordinates: tuple[int,int], playboard: list[list[Place]]):
    x = coordinates[0]
    y = coordinates[1]
    toReturn: list = []
    currentPiece = playboard[x][y].currentPiece
    i = 1
    direction1 = True
    direction2 = True
    direction3 = True
    direction4 = True

    match direction:
        case (0, _):
            while i < 8:
                try:
                    current = playboard[x][y + i]
                    if direction1 and (current.currentPiece == None or current.currentPiece.isWhite != currentPiece.isWhite):
                        toReturn.append((x, y + i))
                        if current.currentPiece != None:
                            direction1 = False
                    else:
                        direction1 = False
                except:
                    pass
                try:
                    current = playboard[x][y - i]
                    if direction2 and (current.currentPiece == None or current.currentPiece.isWhite != currentPiece.isWhite):
                        toReturn.append((x, y - i))
                        if current.currentPiece != None:
                            direction2 = False
                    else:
                        direction2 = False
                except:
                    pass
                i += 1
        case (_, 0):
            while i < 8:
                try:
                    current = playboard[x + i][y]
                    if direction1 and (current.currentPiece == None or current.currentPiece.isWhite != currentPiece.isWhite):
                        toReturn.append((x + i, y))
                        if current.currentPiece != None:
                            direction1 = False
                    else:
                        direction1 = False
                except:
                    pass
                try:
                    current = playboard[x - i][y]
                    if direction2 and (current.currentPiece == None or current.currentPiece.isWhite != currentPiece.isWhite):
                        toReturn.append((x - i, y))
                        if current.currentPiece != None:
                            direction2 = False
                    else:
                        direction2 = False
                except:
                    pass
                i += 1
        case (_, _):
            while i < 8:
                try:
                    current = playboard[x + i][y + i]
                    if direction1 and (current.currentPiece == None or current.currentPiece.isWhite != currentPiece.isWhite):
                        toReturn.append((x + i, y + i))
                        if current.currentPiece != None:
                            direction1 = False
                    else:
                        direction1 = False
                except:
                    pass
                try:
                    current = playboard[x - i][y + i]
                    if direction2 and (current.currentPiece == None or current.currentPiece.isWhite != currentPiece.isWhite):
                        toReturn.append((x - i, y + i))
                        if current.currentPiece != None:
                            direction2 = False
                    else:
                        direction2 = False
                except:
                    pass
                try:
                    current = playboard[x + i][y - i]
                    if direction3 and (current.currentPiece == None or current.currentPiece.isWhite != currentPiece.isWhite):
                        toReturn.append((x + i, y - i))
                        if current.currentPiece != None:
                            direction3 = False
                    else:
                        direction3 = False
                except:
                    pass
                try:
                    current = playboard[x - i][y - i]
                    if direction4 and (current.currentPiece == None or current.currentPiece.isWhite != currentPiece.isWhite):
                        toReturn.append((x - i, y - i))
                        if current.currentPiece != None:
                            direction4 = False
                    else:
                        direction4 = False
                except:
                    pass
                i += 1
    return toReturn


def kingMoves(coordinates: tuple[int,int], playboard: list[list[Place]]):
    allMoves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    currentPiece = playboard[coordinates[0]][coordinates[1]].currentPiece
    if not currentPiece.moved:
        if currentPiece.isWhite:
            try:
                if not playboard[0][7].currentPiece.moved:
                    if len(presentPossible([(-1, 0), (-2, 0)], coordinates, playboard)) == 2:
                        allMoves.append((-3, 0))
            except:
                print('failed to jump')
            try:
                if not playboard[7][7].currentPiece.moved:
                    if len(presentPossible([(1, 0)], coordinates, playboard)) == 1:
                        allMoves.append((2, 0))
            except ValueError:
                print('failed to jump')
                pass
        else:
            try:
                if not playboard[0][0].currentPiece.moved:
                    if int(len(presentPossible([(-1, 0), (-2, 0)], coordinates, playboard))) == 2:
                        allMoves.append((-3, 0))
            except:
                print('failed to jump')
                pass
            try:
                if not playboard[7][0].currentPiece.moved:
                    if int(len(presentPossible([(1, 0)], coordinates, playboard))) == 1:
                        allMoves.append((2, 0))
            except:
                print('failed to jump')
                pass
    return presentPossible(allMoves, coordinates, playboard)

def queenMoves(coordinates: tuple[int, int], playboard: list[list[Place]]):
    return rookMoves(coordinates, playboard) + bishopMoves(coordinates, playboard)


def rookMoves(coordinates: tuple[int, int], playboard: list[list[Place]]):
    return intoDirection((0, 1), coordinates, playboard) + intoDirection((1, 0), coordinates, playboard)

def knightMoves(coordinates: tuple[int,int], playboard: list[list[Place]]):
    allMoves = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
    return presentPossible(allMoves, coordinates, playboard)

def bishopMoves(coordinates: tuple[int,int], playboard: list[list[Place]]):
    return intoDirection((1, 1), coordinates, playboard)

def pawnMoves(coordinates: tuple[int,int], playboard: list[list[Place]], lastMove: tuple[tuple]):
    toReturn: list = []
    x = coordinates[0]
    y = coordinates[1]
    pawn = playboard[x][y].currentPiece

    if pawn.isWhite:
        try:
            current = playboard[x][y - 1]
            if current.currentPiece == None:
                toReturn.append((x, y - 1))
                if y == 6 and playboard[x][y - 2].currentPiece == None:
                    toReturn.append((x, y - 2))
            print((abs(lastMove[1][0] - x) == 1 and isinstance(playboard[lastMove[1][0]][lastMove[1][1]].currentPiece, Pawn) and abs(lastMove[1][1] - lastMove[0][1]) == 2))
            if playboard[x + 1][y - 1].currentPiece != None and not playboard[x + 1][y - 1].currentPiece.isWhite or (abs(lastMove[1][0] - x) == 1 and isinstance(playboard[lastMove[1][0]][lastMove[1][1]].currentPiece, Pawn) and abs(lastMove[1][1] - lastMove[0][1]) == 2):
                toReturn.append((x + 1, y - 1))
            if playboard[x - 1][y - 1].currentPiece != None and not playboard[x - 1][y - 1].currentPiece.isWhite or (abs(lastMove[1][0] - x) == 1 and isinstance(playboard[lastMove[1][0]][lastMove[1][1]].currentPiece, Pawn) and abs(lastMove[1][1] - lastMove[0][1]) == 2):
                toReturn.append((x - 1, y - 1))
        except:
            pass
    else:
        try:
            current = playboard[x][y + 1]
            if current.currentPiece == None:
                toReturn.append((x, y + 1))
                if y == 1 and playboard[x][y + 2].currentPiece == None:
                    toReturn.append((x, y + 2))
        except:
            pass
        try:
            if playboard[x + 1][y + 1].currentPiece.isWhite or (abs(lastMove[1][0] - x) == 1 and isinstance(playboard[lastMove[1][0]][lastMove[1][1]].currentPiece, Pawn) and abs(lastMove[1][1] - lastMove[0][1]) == 2):
                toReturn.append((x + 1, y + 1))
        except:
            pass
        try:
            if playboard[x - 1][y + 1].currentPiece.isWhite:
                toReturn.append((x - 1, y + 1))
        except:
            pass

    return toReturn