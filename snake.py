import pygame
from costants import WINDOW_WIDTH, WINDOW_HEIGHT, PIXELS
from colors import BLUE

class Snake:

    #initializes the color and the spawn of the snake
    def __init__(self):
        self.color = BLUE
        self.spawn()
        self.state = "STOP"
        self.bodies = [pygame.Rect(self.posX, self.posY, PIXELS, PIXELS)]  # Start with the head
        self.grow = False  # Growth flag

        #self.bodies_rect = []
    #spawns the snake in the middle of the screen
    def spawn(self):
        self.posX = WINDOW_WIDTH / 2 - PIXELS
        self.posY = WINDOW_HEIGHT / 2

    
    #draws the rest of the body of the snake
    def drawBody(self, surface):
        for segment in self.bodies:
            pygame.draw.rect(surface, self.color, segment)
              
        return True

    #changes the position of the snake depending on the key pressed
    def movement(self, state):
        head = self.bodies[0].copy()
        if head.y <= 640 and head.y >= 0 and head.x <= 640 and head.x >= 0:
            match state:
                case "UP":
                    head.y -= PIXELS
                case "DOWN":
                    head.y += PIXELS
                case "LEFT":
                    head.x -= PIXELS
                case "RIGHT":
                    head.x += PIXELS

        else:
            self.__init__()
            return False
        
        self.bodies.insert(0, head)

        if not self.grow:
            self.bodies.pop()
        else:
            self.grow = False

    def check_self_collision(self):
        head = self.bodies[0]
        for segment in self.bodies[1:]:
            if head.colliderect(segment):
                self.__init__()
                return False
        return True
                    




    

