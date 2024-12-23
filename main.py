import pygame
import sys
from scenes.menu import main_menu

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("D&D PvP Game")

def main():
    while True:
        main_menu()

if __name__ == "__main__":
    main()
