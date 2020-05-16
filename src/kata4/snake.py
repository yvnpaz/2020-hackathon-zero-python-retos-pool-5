import pygame, sys, time, random
from pygame.locals import *

# pygame.init()
# play_surface = pygame.display.set_mode((500, 500))
# fps = pygame.time.Clock()
game_over = False
game_close = False
dis_width = 500
dis_height = 500
dis = pygame.display.set_mode((dis_width, dis_height))
snake_block = 10
snake_speed = 15
black = (0, 0, 0)

class Snake():
    position = [100,50]
    body = [[100,50],[90,50],[80,50]]
    direction = "RIGHT"
    change = direction

    x1_change = 0       
    y1_change = 0

    snake_List = []

    # Manejo del pressed [KEYDOWN] de las teclas [K_RIGHT - K_LEFT - K_UP -K_DOWN ]
    def controller(self, event, pygame):
        global game_over, dis_width, dis_height
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
    
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change

    # Controla el cambio de  las direcciones
    # Orientaciones
    # Vertical      -> Movimientos [RIGHT - LEFT]
    # Horizontal    -> Movimientos [UP - DOWN]
    # Incremento del movimiento 
    def changeDirection(self):
        global black
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
        self.body.insert(0, list(self.position))

class Game():
    run = True
    food_pos = 0
    score = 0
    length_of_snake = 0    

    def __init__(self):
        self.food_spawn()

    # función de salida
    def exit(self, event, pygame):
        global game_close
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
    
    # Posición aleatorio entre el ranto [0,49] * 10  
    def food_spawn(self):
        self.food_pos = random.randInt(0,49) * 10

    # Si colisionas con una fruta, sumas 1
    # Sino decrementas en 1 el body del snake
    def eat(self, snake):
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

    # Mensajes de salida cuando el snake muere
    # Posición snake[0] >= 500 ó snake[0] <= 0                  -> Muere
    # Posición snake[1] >= 500 ó snake[1] <= 0                  -> Muere
    # Posición del snake choca con sigo mismo menos la cabeza   -> Muere 
    def dead(self, snake):
        if snake.position[0] >= 500 or snake.position[0] <= 0:
            game_close = True
        elif snake.position[1] >= 500 or snake[1] <= 0:
            game_close = True
        else:
            for posBody in snake.position:
                if snake.body == posBody:
                    game_close = True

    #Entry Point
    def main():
    # Descomentar para lanzar el juego en local
    # Comentar para validar con el oráculo
        pygame.init()
        play_surface = pygame.display.set_mode((500, 500))
        fps = pygame.time.Clock()

        snake = Snake()
        game = Game()

        # Bucle principal
        while game.run:
            for event in pygame.event.get():
                game.exit(event, pygame)
                snake.controller(event, pygame)
        
            snake.changeDirection()

            game.eat(snake)

            # Dibujar Snake
            play_surface.fill((0,0,0))
            for pos in snake.body:
                pygame.draw.rect(play_surface, (200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))

            pygame.draw.rect(play_surface, (255,160,60), pygame.Rect(game.food_pos[0], game.food_pos[1], 10, 10))

            game.dead(snake)

            pygame.display.flip()
            fps.tick(60)

        
# Comienza la aventura!!!!
# Descomentar para lanzar el juego en local
# Comentar para validar con el oráculo
#main()
#pygame.quit()
