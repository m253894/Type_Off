import sys
import pygame
from bubble import Bubble
from time import sleep


class TypeOff:
    # Initialize game
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.player_screen1 = (0, 0, 230)
        self.player_screen2 = (230, 0, 0)
        pygame.display.set_caption("Type Off!")
        self.bubble = Bubble(self)

    def run_game(self):  # Game Loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.player_screen1)
            self.bubble.draw2()
            pygame.display.flip()
            sleep(0.5)


if __name__ == '__main__':
    to = TypeOff()
    to.run_game()
