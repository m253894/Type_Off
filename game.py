import sys
import pygame
from bubble import Bubble
from time import sleep
from play import Button
from background import Background
import operations
from random import randint
import keydown

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
        self.bubs = Bubble(self, operations.lvl2)
        self.create_bubbles()
        self.bubs.check_collision(self.bubbles)
        self.jam = pygame.mixer.music.load('images/Jellyfish Jam.mp3')

    def create_bubbles(self):
        # prints each bubble with its own image
        for pic in self.bubs.pics:
            self.bubs = Bubble(self, operations.lvl2)
            self.bubs.image = pic
            self.bubbles.add(self.bubs)

    def pop(self):
        key_list = keydown.keydown()
        # loop through each bubble in the group
        for bubble in self.bubbles:
            for key in self.bubs.kills:
                # if the bubbles assigned kill key is in the kills list and the key pressed list, remove it.
                if key in key_list:
                    self.bubbles.remove(bubble)
                    key_list.remove(key)
                else:
                    pass

    def run_game(self): # Game Loop
        while True:
            pygame.mixer.music.play(2)
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
            pygame.mixer.music.play(2)
            # check for mouse click on either button to start its respective game mode.
            self.screen.fill(self.player_screen)
            self.pop()
            self.bubbles.draw(self.screen)
            pygame.display.flip()


if __name__ == '__main__':
    to = TypeOff()
    to.run_game()
