import sys
import pygame
from bubble import Bubble
from time import sleep
from play import Button
from background import Background
import operations
from random import randint


class TypeOff:
    # Initialize game
    def __init__(self):
        pygame.init()
        # Initialize screen for player one and two
        self.screen = pygame.display.set_mode((1200, 800))
        self.player_screen = (0, 0, 230)
        pygame.display.set_caption("Type Off!")
        # making bubble group
        self.bubbles = pygame.sprite.Group()
        # making instances of each button on menu screen
        self.single = Button(self, 1200/4-100, 800/2, 275, 100)
        self.multi = Button(self, 1200*2/3, 800/2, 225, 100)
        self.title = Button(self, 1200/2-150, 800/8, 325, 100)
        # making instance of background
        self.menu_back = Background()
        self.menu = True
        self.mouse_pos = pygame.mouse.get_pos()
        # instance of bubble
        self.create_bubbles()

    def create_bubbles(self):
        bubs = Bubble(self, operations.lvl2)
        for letter in operations.lvl2:
            self.bubbles.add(bubs)

    def run_game(self):  # Game Loop
        while True:
            # main menu loop
            while self.menu:
                # drawing all components of main menu screen
                self.screen.fill(self.player_screen)
                self.screen.blit(self.menu_back.image, self.menu_back.rect)
                self.single.draw_button('SINGLE')
                self.multi.draw_button('MULTI')
                self.title.draw_button('Type Off!')
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    # checking for mouse click on the mode buttons
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.mouse_pos = pygame.mouse.get_pos()
                    if self.single.rect.collidepoint(self.mouse_pos) or self.multi.rect.collidepoint(self.mouse_pos):
                        self.menu = False
            # check for mouse click on either button to start its respective game mode.
            self.screen.fill(self.player_screen)
            self.bubbles.draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            sleep(3)

if __name__ == '__main__':
    to = TypeOff()
    to.run_game()
