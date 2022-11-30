import sys
import pygame
from bubble import Bubble
from time import sleep
from play import Button
import operations
from random import randint


class TypeOff:
    # Initialize game
    def __init__(self):
        pygame.init()
        # Initialize screen for player one and two
        self.screen = pygame.display.set_mode((1200, 800))
        self.player_screen1 = (0, 0, 230)
        self.player_screen2 = (230, 0, 0)
        pygame.display.set_caption("Type Off!")
        self.bubbles = pygame.sprite.Group()
        self.create_bubbles()
        # instances of play buttons
        self.single_button = Button(self, "SINGLE")
        self.multi_button = Button(self, "MULTI")

    def create_bubbles(self):
        bubs = Bubble(self, operations.lvl2)
        self.bubbles.add(bubs)

    def run_game(self):  # Game Loop
        single = True
        multi = True
        while True:
            # check for mouse click on either button to start its respective game mode.
            self.bubbles.draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.single_button.rect.collidepoint(mouse_pos):
                        multi = False
                    if self.multi_button.rect.collidepoint(mouse_pos):
                        single = False
                if event.type == pygame.QUIT:
                    sys.exit()
                self.screen.fill(self.player_screen1)
            if multi != True:
                self.single_button.draw_button()
                single = False
            if single !=  True:
                self.multi_button.draw_button()
                multi = False
            pygame.display.flip()
            sleep(3)


if __name__ == '__main__':
    to = TypeOff()
    to.run_game()
