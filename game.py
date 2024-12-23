import pygame
import sys
from turn_manager import TurnManager
from entities.player import Player
from entities.enemy import Enemy

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
pygame.display.set_caption("D&D PvP Game")

# Load font
font = pygame.font.Font(None, 36)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def game():
    clock = pygame.time.Clock()
    turn_manager = TurnManager()
    
    # Create player and enemy entities
    player = Player("Player", 100, 10)
    enemy = Enemy("Enemy", 100, 10)
    
    turn_manager.add_entity(player)
    turn_manager.add_entity(enemy)
    
    running = True
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Game logic
        turn_manager.update()
        
        # Drawing
        draw_text(f"Player HP: {player.hp}", font, BLACK, screen, 20, 20)
        draw_text(f"Enemy HP: {enemy.hp}", font, BLACK, screen, 20, 60)
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    game()
