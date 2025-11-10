import pygame
import time
import random

# Initialize pygame
pygame.init()

# Game window size, this size seems to work well
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (213, 50, 80)
white = (255, 255, 255)

# Snake and food block size
block_size = 20
snake_speed = 15

# Font
font = pygame.font.SysFont("bahnschrift", 25)

# Score function
def show_score(score):
    value = font.render("Score: " + str(score), True, white)
    win.blit(value, [0, 0])

# Snake drawing
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, green, [x[0], x[1], snake_block, snake_block])

# Game loop
def gameLoop():
    game_over = False
    game_close = False

    x = width // 2
    y = height // 2

    x_change = 0
    y_change = 0

    snake = []
    length = 1

    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            win.fill(black)
            msg = font.render("You lost! Press Q to Quit or C to Play Again", True, red)
            win.blit(msg, [width / 6, height / 3])
            show_score(length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        win.fill(black)
        pygame.draw.rect(win, red, [food_x, food_y, block_size, block_size])
        snake_head = [x, y]
        snake.append(snake_head)

        if len(snake) > length:
            del snake[0]

        for segment in snake[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(block_size, snake)
        show_score(length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
