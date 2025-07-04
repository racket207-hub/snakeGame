import pygame
from sys import exit
from snake import Snake
from background import Background
from apple import Apple
from costants import WINDOW_WIDTH, WINDOW_HEIGHT


#collision method that checks if the snake rectangle
#collides with the apple rectangle, if the condition is true it will
#draw the snake longer and spawn another apple
def collision(snake, apple, screen):
    if snake.bodies[0].colliderect(apple.rect):
        snake.grow = True
        snake.apple_eaten += 1
        snake.drawBody(screen)
        apple.spawn()
        apple.draw(screen)


def main():
    
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    game_active = False
    test_font = pygame.font.Font(None, 50)
    game_message = test_font.render('Press space to start the game', False, (111, 196, 169))
    game_message_rect = game_message.get_rect(center = (320, 320))

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
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: game_active = True
                        
        if game_active:
            #draw calls
            background.draw(screen)
            apple.draw(screen)
            snake.drawBody(screen)
        

            pygame.time.delay(120)
            snake.movement(snake.state)

            collision(snake, apple, screen) 

        else:
           background.draw(screen)
           screen.blit(game_message, game_message_rect) 

        pygame.display.update()
        clock.tick(60)
    
main()
