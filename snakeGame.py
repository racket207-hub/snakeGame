import pygame
import random
from sys import exit

#COSTANTS
WINDOW_HEIGHT = 640
WINDOW_WIDTH = 640
PIXELS = 32
SQUARE = int(WINDOW_WIDTH/PIXELS)

#COLORS
BACKGROUND_COLOR_1 = (156, 210, 54)
BACKGROUND_COLOR_2 = (147,203, 57)
RED = (255, 0 ,0)
BLUE = (0, 0, 255)

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


#collision method that checks if the snake rectangle
#collides with the apple rectangle, if the condition is true it will
#draw the snake longer and spawn another apple
def collision(snake, apple, screen):
    if snake.rect.colliderect(apple.rect):
        snake.apple_eaten += 1
        snake.draw(screen)
        apple.spawn()
        apple.draw(screen)


def main():
    
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    game_active = True

    #OBEJECTS
    background = Background()
    apple = Apple()
    snake = Snake()

    #gameloop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if game_active:
                if event.type == pygame.KEYDOWN:
                    #match case to check the pressed keys and assigning a string value to snake.state
                    match event.key:
                        case pygame.K_w | pygame.K_UP:
                            snake.state = "UP"
                        case pygame.K_s | pygame.K_DOWN:
                            snake.state = "DOWN"
                        case pygame.K_a | pygame.K_LEFT:
                            snake.state = "LEFT"
                        case pygame.K_d | pygame.K_RIGHT:
                            snake.state = "RIGHT"


        #draw calls
        background.draw(screen)
        apple.draw(screen)
        snake.draw(screen)
        

        pygame.time.delay(120)
        snake.movement(snake.state)

        collision(snake, apple, screen) 

        pygame.display.update()
        clock.tick(60)
    
main()
