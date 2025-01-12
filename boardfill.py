import pygame
pygame.init
class Board:
    def __init__(self, screen):
        self.screen = screen
    def draw(self, row_height, column_width, level): 
        for i in range(len(level)):
            for j in range(len(level[i])):
                if level[i][j] == 1:
                    pygame.draw.circle(self.screen, (255,255,255), (j * column_width + (0.5 * column_width), i * row_height + (0.5 * row_height)), 4)
                if level[i][j] == 2:
                    pygame.draw.circle(self.screen, (255,255,255), (j * column_width + (0.5 * column_width), i * row_height + (0.5 * row_height)), 8)
                    