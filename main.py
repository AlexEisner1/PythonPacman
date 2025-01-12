import pygame
from pacman import Pacman
from directions import Directions
from boardfill import Board
from board import boards

pygame.init()
screen_width=800
screen_height=600
screen = pygame.display.set_mode((screen_width, screen_height))
clock=pygame.time.Clock()
pacman = Pacman(400, 300, 15, 15, screen_height, 0, screen_width, 0, Directions.RIGHT, 5)
board = Board(screen)
running = True
go_right = False
go_left = False
go_up = False
go_down = False
while running==True:
    board.draw (screen_height //32, screen_width // 32, boards)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys [pygame.K_UP]:
        pacman.set_direction(Directions.UP)
    if keys [pygame.K_DOWN]: 
        pacman.set_direction(Directions.DOWN)
    if keys [pygame.K_LEFT]:
        pacman.set_direction(Directions.LEFT)
    if keys [pygame.K_RIGHT]:
        pacman.set_direction(Directions.RIGHT)
    screen.fill((0,0,0))
    pacman.update()
    pygame.draw.circle(screen, (255, 255, 0), (pacman.x, pacman.y), pacman.height)
    pygame.display.flip()
    clock.tick(60)