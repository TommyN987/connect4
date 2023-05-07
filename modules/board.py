import pygame
import numpy as np
from modules.player import Player
from constants import SIZE, HEIGHT, ROWS, COLUMNS, SQUARESIZE, RADIUS, BLACK, BLUE

pygame.init()


class Board:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode(SIZE)
        self.state = np.zeros((ROWS, COLUMNS))

    def draw(self, player1: Player, player2: Player):
        for c in range(COLUMNS):
            for r in range(ROWS):
                pygame.draw.rect(self.screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(self.screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

        for c in range(COLUMNS):
            for r in range(ROWS):
                if self.state[r][c] == 1:
                    pygame.draw.circle(self.screen, player1.color, (int(c*SQUARESIZE+SQUARESIZE/2), HEIGHT-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif self.state[r][c] == 2:
                    pygame.draw.circle(self.screen, player2.color, (int(c*SQUARESIZE+SQUARESIZE/2), HEIGHT-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)

        pygame.display.update()
