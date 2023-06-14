import pygame
from boards.board import Board
from boards.place import Place
from player import Player
import boards.moves as moves


class GUI():
    
    def __init__(self, board: Board, white: Player, black: Player) -> None:
        
        screen_width, screen_height = 1090, 820
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Chess")
        
        playboard: list[list[Place]] = board.map
        toMakeRed: list[tuple] = []
        cod: tuple = ()
        movementRight = True
        lastMove:tuple[tuple] = ((0, 0), (0, 0))
        
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (150, 0, 0)
        BROWN = (139, 69, 19)

        # Define fonts
        font = pygame.font.Font(None, 30)

        
        button_width, button_height = 80, 80
        button_spacing = 20

        buttons = []

        for i in range(0, 8):
            for j in range(0, 8):
                current = {
                    'coordinates':(i, j),
                    'place': playboard[i][j],
                    "text": f'',
                    "picture": playboard[i][j].pictures(),
                    "x": (button_spacing + (button_width + button_spacing) * i),
                    "y": (button_spacing + (button_height + button_spacing) * j)
                }
                buttons.append(current)
                playboard[i][j].coordinates = (i, j)
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for button in buttons:
                        if (button["x"] <= mouse_pos[0] <= button["x"] + button_width
                            and button["y"] <= mouse_pos[1] <= button["y"] + button_height):
                            if button['place'].possibleMove and playboard[cod[0]][cod[1]].currentPiece.isWhite == movementRight:
                                if movementRight:
                                    enemy = black
                                else:
                                    enemy = white
                                movementRight =  moves.move(cod, button['coordinates'], playboard, enemy, not movementRight)
                                lastMove = ((cod[0], cod[1]), (button['coordinates'][0], button['coordinates'][1]))
                                self.clearMoves(toMakeRed, playboard)
                                toMakeRed = []
                            else:
                                cod = button['coordinates']
                                self.clearMoves(toMakeRed, playboard)
                                toMakeRed = moves.getMoves(cod, playboard, lastMove)
                            
            screen.fill(BROWN)

            i = 0
            counter = 1

            for button in buttons:
                if i % 2 == 0:
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
                    pygame.draw.rect(screen, RED, (button["x"], button["y"], button_width, button_height))
                else:
                    pygame.draw.rect(screen, colour, (button["x"], button["y"], button_width, button_height))
                button_surface = font.render(button["text"], True, text)
                button_rect = button_surface.get_rect(center=(button["x"] + button_width // 2, button["y"] + button_height // 2))
                
                currentPlace: Place = button['place']
                try:
                    picture = pygame.image.load(currentPlace.currentPiece.link)
                    picture = pygame.transform.scale(picture, (button_width - 20, button_height - 20))
                    picture_rect = (button_rect.centerx - picture.get_width() // 2, button_rect.centery - picture.get_height() // 2)
                    screen.blit(picture, picture_rect)
                except:
                    screen.blit(button_surface, button_rect)

            pygame.display.flip()

    def clearMoves(self, possible, playground):
        for cod in possible:
            playground[cod[0]][cod[1]].possibleMove = False