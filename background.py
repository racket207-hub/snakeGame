import pygame
from costants import PIXELS, SQUARE
from colors import BACKGROUND_COLOR_1, BACKGROUND_COLOR_2

class Background:
    
    #draws the checkered surface
    def draw(self, surface):
        surface.fill(BACKGROUND_COLOR_1)
        i = 0
        for row in range(SQUARE):
            for col in range(SQUARE):
                if i % 2 == 0:
                    pygame.draw.rect(surface, BACKGROUND_COLOR_2, (col * PIXELS, row * PIXELS, PIXELS, PIXELS))
                if col != SQUARE - 1:
                    i += 1

