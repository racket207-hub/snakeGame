import pygame
from costants import WINDOW_WIDTH, WINDOW_HEIGHT, PIXELS
from colors import BLUE
class Snake:

    #initializes the color and the spawn of the snake
    def __init__(self):
        self.color = BLUE
        self.spawn()
        self.state = "STOP"
        self.apple_eaten = 2

    #spawns the snake in the middle of the screen
    def spawn(self):
        self.posX = WINDOW_WIDTH / 2 - PIXELS
        self.posY = WINDOW_HEIGHT / 2

    #draws the snake on the screen
    def draw(self, surface):
        self.rect = pygame.draw.rect(surface, self.color, (self.posX, self.posY, PIXELS, PIXELS * self.apple_eaten))

    #changes the position of the snake depending on the key pressed
    def movement(self, state):
        match state:
            case "UP":
                self.posY -= PIXELS
            case "DOWN":
                self.posY += PIXELS
            case "LEFT":
                self.posX -= PIXELS
            case "RIGHT":
                self.posX += PIXELS

