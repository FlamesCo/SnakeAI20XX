import pygame
import sys
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_pos = [[100, 100], [120, 100], [140, 100]]
food_pos = [random.randrange(1, (WIDTH//CELL_SIZE)) * CELL_SIZE, random.randrange(1, (HEIGHT//CELL_SIZE)) * CELL_SIZE]
food_spawn = True
direction = 'LEFT'
change_to = direction


def game_over():
    pygame.quit()
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] - CELL_SIZE])
    if direction == 'DOWN':
        snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] + CELL_SIZE])
    if direction == 'LEFT':
        snake_pos.insert(0, [snake_pos[0][0] - CELL_SIZE, snake_pos[0][1]])
    if direction == 'RIGHT':
        snake_pos.insert(0, [snake_pos[0][0] + CELL_SIZE, snake_pos[0][1]])

    if snake_pos[0] == food_pos:
        food_spawn = False
    else:
        snake_pos.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//CELL_SIZE)) * CELL_SIZE, random.randrange(1, (HEIGHT//CELL_SIZE)) * CELL_SIZE]
    food_spawn = True

    screen.fill((0, 0, 0))
    for pos in snake_pos:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

    if snake_pos[0][0] < 0 or snake_pos[0][0] > WIDTH-CELL_SIZE or snake_pos[0][1] < 0 or snake_pos[0][1] > HEIGHT-CELL_SIZE:
        game_over()
    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            game_over()

    pygame.display.flip()
    clock.tick(10)