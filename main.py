import pygame
from pacman import Pacman


pygame.init()
screen_width=800
screen_height=600
screen = pygame.display.set_mode((screen_width, screen_height))
clock=pygame.time.Clock()
pacman = Pacman(400, 300, 15, 15, 5)
running = True
while running==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys [pygame.K_UP]:
        if pacman.y > 0:
            pacman.move("up")
    if keys [pygame.K_DOWN]: 
        if pacman.y < 600:
            pacman.move("down")
    if keys [pygame.K_LEFT]:
        if pacman.x > 0:
            pacman.move("left")
    if keys [pygame.K_RIGHT]:
        if pacman.x < 800:
            pacman.move("right")
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255, 255, 0), (pacman.x, pacman.y), pacman.height)
    pygame.display.flip()
    clock.tick(60)