import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("D&D PvP Game - Main Menu")

# Load font
font = pygame.font.Font(None, 74)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    click = False
    while True:
        screen.fill(WHITE)
        
        draw_text('Main Menu', font, BLACK, screen, 300, 100)
        
        mx, my = pygame.mouse.get_pos()
        
        button_1 = pygame.Rect(300, 250, 200, 50)
        button_2 = pygame.Rect(300, 350, 200, 50)
        
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        
        pygame.draw.rect(screen, BLACK, button_1)
        pygame.draw.rect(screen, BLACK, button_2)
        
        draw_text('Start Game', font, WHITE, screen, 310, 260)
        draw_text('Options', font, WHITE, screen, 310, 360)
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()

def game():
    # Placeholder for the game function
    pass

def options():
    # Placeholder for the options function
    pass

if __name__ == "__main__":
    main_menu()
