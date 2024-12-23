from pygame import font as pygame_font
import random

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# draw text with default font
def draw_text_default_font(text, surface, x, y):
    font = pygame_font.Font(None, 74)
    color = (0, 0, 0)
    draw_text(text, font, color, surface, x, y)