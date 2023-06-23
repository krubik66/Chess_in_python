import pygame
from boards.board import Board
from boards.place import Place
from player import Player
import boards.moves as moves
import pickle
import os
from saving import Save_data


class GUI():
    
    def __init__(self, board: Board, white: Player, black: Player) -> None:
        
        screenWidth, screenHeight = 1090, 820
        screen = pygame.display.set_mode((screenWidth, screenHeight))
        pygame.display.set_caption("Chess")
        
        playboard: list[list[Place]] = board.map
        toMakeRed: list[tuple] = []
        cod: tuple = ()
        movementRight = True
        movesHistory: list[tuple[tuple]] = []
        lastMove:tuple[tuple] = ((0, 0), (0, 0))
        
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (150, 0, 0)
        BROWN = (139, 69, 19)
        GRAY = (100, 100, 100)

        font = pygame.font.Font(None, 30)

        self.buttonWidth, self.buttonHeight = 80, 80
        self.buttonSpacing = 20

        buttons = []
        saveButton = {
            "text": f'Save',
            "x": 830,
            "y": 700
        }
        loadButton = {
            "text": f'Load',
            "x": 890,
            "y": 700
        }
        
        buttons = self.renewButtons(playboard)
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    print(f'mousePos: {mousePos}')
                    if (saveButton["x"] <= mousePos[0] <= saveButton["x"] + self.buttonWidth
                            and saveButton["y"] <= mousePos[1] <= saveButton["y"] + self.buttonHeight):
                        self.save(board, white, black, movementRight, movesHistory, lastMove)
                    if (loadButton["x"] <= mousePos[0] <= loadButton["x"] + self.buttonWidth
                        and loadButton["y"] <= mousePos[1] <= loadButton["y"] + self.buttonHeight):
                        try:
                            with open('save.pkl', 'rb') as file:
                                loadedSave: Save_data = pickle.load(file)

                            playboard = loadedSave.board.map
                            board.map = playboard
                            white = loadedSave.white
                            black = loadedSave.black
                            buttons = self.renewButtons(playboard)
                            movementRight = loadedSave.movementRight
                            movesHistory = loadedSave.movesHistory
                            lastMove = loadedSave.lastMove
                            #print(f'w: {loadedSave.white}\nb: {loadedSave.black}\nb: {loadedSave.board}')
                            print('loaded')
                        except:
                            pass

                    for button in buttons:
                        if (button["x"] <= mousePos[0] <= button["x"] + self.buttonWidth
                            and button["y"] <= mousePos[1] <= button["y"] + self.buttonHeight):
                            if button['place'].possibleMove and playboard[cod[0]][cod[1]].currentPiece.isWhite == movementRight:
                                if movementRight:
                                    enemy = black
                                else:
                                    enemy = white
                                movementRight =  moves.move(cod, button['coordinates'], playboard, enemy, not movementRight)
                                lastMove = ((cod[0], cod[1]), (button['coordinates'][0], button['coordinates'][1]))
                                movesHistory.append(lastMove)
                                self.clearMoves(toMakeRed, playboard)
                                toMakeRed = []
                                if moves.isThisTheEnd(playboard, lastMove, movementRight):
                                    running = self.gameEnded(screen, not movementRight, (screenWidth // 2 - 200, screenHeight // 2 - 100), playboard)
                            else:
                                cod = button['coordinates']
                                self.clearMoves(toMakeRed, playboard)
                                toMakeRed = moves.getMoves(cod, playboard, lastMove)
                            
            screen.fill(BROWN)

            labels = [
            {'text': f'Playing: {self.whoIsPlaying(movementRight)}'},
            {'text': f'Previous moves:\n{self.showPreviousMoves(movesHistory)}'}
            ]

            i = 0
            for label in labels:
                i += 1
                rendered = font.render(label['text'], True, color=BLACK)
                screen.blit(rendered, (830, self.buttonSpacing * i))

            i = 0
            counter = 1

            for button in buttons:
                if i % 2 == 1:
                    colour = BLACK
                    text = WHITE
                    i += 1
                else:
                    colour = WHITE
                    text = BLACK
                    i -= 1
                if counter % 8 == 0:
                    i += 1
                counter += 1
                if toMakeRed.__len__() > 0 and button['coordinates'] in toMakeRed:
                    button['place'].possibleMove = True
                    pygame.draw.rect(screen, RED, (button["x"], button["y"], self.buttonWidth, self.buttonHeight))
                else:
                    pygame.draw.rect(screen, colour, (button["x"], button["y"], self.buttonWidth, self.buttonHeight))
                buttonSurface = font.render(button["text"], True, text)
                buttonRect = buttonSurface.get_rect(center=(button["x"] + self.buttonWidth // 2, button["y"] + self.buttonHeight // 2))
                
                currentPlace: Place = button['place']
                try:
                    picture = pygame.image.load(currentPlace.currentPiece.link)
                    picture = pygame.transform.scale(picture, (self.buttonWidth - 20, self.buttonHeight - 20))
                    pictureRect = (buttonRect.centerx - picture.get_width() // 2, buttonRect.centery - picture.get_height() // 2)
                    screen.blit(picture, pictureRect)
                except:
                    screen.blit(buttonSurface, buttonRect)

            rendered = font.render(saveButton['text'], True, color=pygame.Color('yellow'))
            pygame.draw.rect(screen, GRAY, (saveButton["x"], saveButton["y"], self.buttonWidth * 2, self.buttonHeight // 2))
            screen.blit(rendered, (saveButton['x'] + self.buttonSpacing // 2, saveButton['y'] + self.buttonSpacing // 2))

            rendered = font.render(loadButton['text'], True, color=pygame.Color('yellow'))
            screen.blit(rendered, (loadButton['x'] + self.buttonSpacing // 2, loadButton['y'] + self.buttonSpacing // 2))

            pygame.display.flip()

    def clearMoves(self, possible, playground):
        for cod in possible:
            playground[cod[0]][cod[1]].possibleMove = False

    def whoIsPlaying(self, movementRight: bool):
        if movementRight:
            return 'White'
        else:
            return 'Black'
        
    def showPreviousMoves(self, previousMoves: list[tuple[tuple]]):
        toReturn = ''
        boardLetters: str = 'abcdefgh'
        i = 0
        if previousMoves.__len__() % 2 == 0:
            numberToShow = previousMoves.__len__() - 10
        else:
            numberToShow = previousMoves.__len__() - 9
        for j in range(max(numberToShow, 0), previousMoves.__len__()):
            move = previousMoves[j]
            i += 1
            if i % 2 == 0:
                toReturn += f' {boardLetters[move[0][0]]}{abs(move[0][1] - 8)} -> {boardLetters[move[1][0]]}{abs(move[1][1] - 8)}\n'
            else:
                toReturn += f'{boardLetters[move[0][0]]}{abs(move[0][1] - 8)} -> {boardLetters[move[1][0]]}{abs(move[1][1] - 8)} |'
        return toReturn
    
    def gameEnded(self, screen, whoWon: bool, middle: tuple, playboard: list[list[Place]]):
        running = True
        while running:   
            font = pygame.font.Font(None, 100)

            quitButton = {
                    "text": f'Quit',
                    "x": (middle[0]),
                    "y": (middle[1] + 100)
                }
            
            buttonWidth = 200
            buttonHeight = 80

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    if (quitButton["x"] <= mousePos[0] <= quitButton["x"] + buttonWidth
                        and quitButton["y"] <= mousePos[1] <= quitButton["y"] + buttonHeight):
                        running = False
            

            RED = (150, 0, 0)
            GRAY = (100, 100, 100)
            WHITE = (255, 255, 255)

            screen.fill(GRAY)

            pygame.draw.rect(screen, WHITE, (quitButton["x"], quitButton["y"], buttonWidth, buttonHeight))

            buttonSurface = font.render(quitButton["text"], True, color=RED)
            buttonRect = buttonSurface.get_rect(center=(quitButton["x"] + buttonWidth // 2, quitButton["y"] + buttonHeight // 2))

            screen.blit(buttonSurface, buttonRect)
            
            if moves.check(playboard, not whoWon):
                rendered = font.render(f'{self.whoIsPlaying(whoWon)} win!', True, color=RED)
                screen.blit(rendered, middle)
            else:
                rendered = font.render(f'Draw', True, color=RED)
                screen.blit(rendered, middle)

            pygame.display.flip()
        
        return False

    def renewButtons(self, playboard):
        buttons = []
        for i in range(0, 8):
            for j in range(0, 8):
                current = {
                    'coordinates':(i, j),
                    'place': playboard[i][j],
                    "text": f'',
                    "picture": playboard[i][j].pictures(),
                    "x": (self.buttonSpacing + (self.buttonWidth + self.buttonSpacing) * i),
                    "y": (self.buttonSpacing + (self.buttonHeight + self.buttonSpacing) * j)
                }
                buttons.append(current)
                playboard[i][j].coordinates = (i, j)

        return buttons
        
    
    def save(self, board: Board, whites: Player, blacks: Player, movementRight, movesHistory, lastMove):

        saveData = Save_data(board, whites, blacks, movementRight, movesHistory, lastMove)

        savePath = 'save.pkl'

        print(board)

        if not os.path.exists(savePath):
            print()

        with open(savePath, 'wb') as file:
            pickle.dump(saveData, file)