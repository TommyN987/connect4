import sys
import math
import pygame
from modules.board import Board
from modules.player import Player
from constants import ROWS, WIDTH, SQUARESIZE, RADIUS, FONT, RED, YELLOW, BLACK

pygame.init()


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.player1 = Player(1, "Jony", RED)
        self.player2 = Player(2, "Lianka", YELLOW)
        self.active_player = self.player1
        self.game_over = False
        self.board.draw(self.player1, self.player2)

    def drop_piece(self, row: int, col: int) -> None:
        self.board.state[row][col] = self.active_player.number
        self.board.draw(self.player1, self.player2)

    def is_valid_location(self, col: int) -> bool:
        return self.board.state[ROWS - 1][col] == 0

    def get_next_open_row(self, col: int) -> int:
        for r in range(ROWS):
            if self.board.state[r][col] == 0:
                return r

    def change_turns(self):
        if self.active_player == self.player1:
            self.active_player = self.player2
        else:
            self.active_player = self.player1

    def is_winning_move(self, row: int, col: int) -> bool:
        directions = [
            (1, 0),
            (0, 1),
            (1, 1),
            (1, -1)
        ]

        for dx, dy in directions:
            count = 1
            for direction in [-1, 1]:
                for step in range(1, 4):
                    x, y = col + step * direction * dx, row + step * direction * dy

                    if not (0 <= x < len(self.board.state[0]) and 0 <= y < len(self.board.state)):
                        break

                    if self.board.state[y][x] == self.active_player.number:
                        count += 1
                    else:
                        break

                    if count == 4:
                        return True

        return False

    def play(self):
        while not self.game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.board.screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                    posx = event.pos[0]
                    pygame.draw.circle(self.board.screen, self.active_player.color, (posx, int(SQUARESIZE/2)), RADIUS)

                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.board.screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if self.is_valid_location(col):
                        row = self.get_next_open_row(col)
                        self.drop_piece(row, col)

                        if self.is_winning_move(row, col):
                            label = FONT.render("{} wins!".format(self.active_player.name), 1, self.active_player.color)
                            self.board.screen.blit(label, (40, 10))
                            self.game_over = True

                    self.board.draw(self.player1, self.player2)
                    self.change_turns()

                    if self.game_over:
                        pygame.time.wait(3000)
