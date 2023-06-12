import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Button with Image Example")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define button properties
button_width, button_height = 200, 100

# Load the image
image = pygame.image.load("button_image.png")

# Resize the image to fit the button
image = pygame.transform.scale(image, (button_width, button_height))
# GUI loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw the button rectangle
    button_rect = pygame.Rect((screen_width - button_width) // 2, (screen_height - button_height) // 2, button_width, button_height)
    pygame.draw.rect(screen, BLACK, button_rect)

    # Blit the image onto the button
    screen.blit(image, button_rect)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
