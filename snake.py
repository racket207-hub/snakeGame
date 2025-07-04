import pygame
from costants import WINDOW_WIDTH, WINDOW_HEIGHT, PIXELS
from colors import BLUE

class Snake:

    #initializes the color and the spawn of the snake
    def __init__(self):
        self.color = BLUE
        self.spawn()
        self.state = "STOP"
        self.apple_eaten = 1
        self.bodies = [pygame.Rect(self.posX, self.posY, PIXELS, PIXELS)]  # Start with the head
        self.grow = False  # Growth flag

        #self.bodies_rect = []
    #spawns the snake in the middle of the screen
    def spawn(self):
        self.posX = WINDOW_WIDTH / 2 - PIXELS
        self.posY = WINDOW_HEIGHT / 2

    #draws the head of the snake on the screen
    #def drawHead(self, surface):
        #self.rect = pygame.draw.rect(surface, self.color, (self.posX, self.posY, PIXELS, PIXELS ))
        #calls directly for the method to draw the rest of the body
        #self.drawBody(surface)

    #draws the rest of the body of the snake
    def drawBody(self, surface):
        for segment in self.bodies:
            pygame.draw.rect(surface, self.color, segment)
        #self.bodies = [pygame.draw.rect(surface, self.color, (self.posX, self.posY, PIXELS, PIXELS * self.apple_eaten))]
        #self.bodies_rect = (pygame.draw.rect(surface, self.color, (self.posX, self.posY, PIXELS, PIXELS * self.apple_eaten))) 
        #self. getRect()

    #def getRect(self):
        #for rect in range(len(self.bodies)):
            #self.bodies_rect = pygame.draw.rect(self.bodies[rect])

    #changes the position of the snake depending on the key pressed
    def movement(self, state):
        head = self.bodies[0].copy()
        match state:
            case "UP":
                head.y -= PIXELS
            case "DOWN":
                head.y += PIXELS
            case "LEFT":
                head.x -= PIXELS
            case "RIGHT":
                head.x += PIXELS

        self.bodies.insert(0, head)

        if not self.grow:
            self.bodies.pop()
        else:
            self.grow = False
