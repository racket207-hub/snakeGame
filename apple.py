import pygame
from costants import WINDOW_WIDTH, PIXELS
from colors import RED
import random

class Apple:

    #initializes the color and the spawn of the apple
    def __init__(self):
        self.color = RED
        self.spawn()

    #spawns the apple randomically
    def spawn(self):
        self.posX = random.randrange(0, WINDOW_WIDTH, PIXELS)
        self.posY = random.randrange(0, WINDOW_WIDTH, PIXELS)
    
    #draws the apple
    def draw(self, surface):
       self.rect = pygame.draw.rect(surface, self.color, (self.posX, self.posY, PIXELS, PIXELS))


