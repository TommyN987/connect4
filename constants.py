import pygame

pygame.init()


BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


FONT = pygame.font.SysFont("monospace", 75)


ROWS = 6
COLUMNS = 7


SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)

WIDTH = COLUMNS * SQUARESIZE
HEIGHT = (ROWS + 1) * SQUARESIZE
SIZE = (WIDTH, HEIGHT)
