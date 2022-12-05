import sys
import pygame
from bubble import Bubble
from time import sleep
from play import Button
from background import Background
import operations
from random import randint
import keydown
from text import Dynamic_Text
import random
from score import Scoreboard


class TypeOff:
    # Initialize game
    def __init__(self):
        pygame.init()
        # Initialize screen for player
        self.screen = pygame.display.set_mode((1200, 800))
        self.player_screen = (0, 0, 230)
        pygame.display.set_caption("Type Off!")
        # making bubble group
        self.bubbles = pygame.sprite.Group()
        # Blakeley Cremer helped me with button positioning my buttons
        # making instances of each button on menu screen
        self.single = Button(self, 1200/4-100, 800/2, 275, 100)
        self.multi = Button(self, 1200*2/3, 800/2, 225, 100)
        self.title = Button(self, 1200/2-150, 800/8, 325, 100)
        # making instance of dynamic text
        self.dynamic_text = Dynamic_Text()
        # making instance of background
        self.menu_back = Background()
        self.menu = True
        self.multiplayer = False
        self.singleplayer = False
        self.mouse_pos = pygame.mouse.get_pos()
        # instance of bubble
        self.bubs = Bubble(self, operations.lvl2)
        self.create_bubbles()
        self.bubs.check_collision(self.bubbles)
        # instance of scoreboard and score
        self.score = 0
        self.scoreboard = Scoreboard(self)
        self.game_time = 0
        self.turn = 0
        # load background music
        self.jam = pygame.mixer.music.load('images/Jellyfish Jam.mp3')
        self.end_time = [59997, 59998, 59999, 60000, 600001, 600002, 60003, 60004]

    def create_bubbles(self):
        # prints each bubble with its own image
        for pic in self.bubs.pics:
            self.bubs = Bubble(self, operations.lvl2)
            self.bubs.image = pic
            self.bubbles.add(self.bubs)

    def create_more(self):
        if len(self.bubbles) == 0:
            # calls another random word to display
            operations.lvl2 = random.choice(operations.words2)
            self.bubs = Bubble(self, operations)
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
                    self.score += 10
    # Timer
    def get_time(self):
        self.timer = pygame.time.get_ticks()

    def run_game(self): # Game Loop
        while True:
            pygame.mixer.music.play(2)
            # main menu loop
            while self.menu:
                # Helped by Blakeley Cremer helped me with drawing my buttons
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
                # for a mouse click on either button 3, 2, 1 will be displayed on the screen
                # checks for bools to start either game mode loop
                if self.single.rect.collidepoint(self.mouse_pos):
                    self.screen.fill(self.player_screen)
                    self.dynamic_text.draw()
                    self.singleplayer = True
                    self.menu = False
                if self.multi.rect.collidepoint(self.mouse_pos):
                    self.screen.fill(self.player_screen)
                    self.dynamic_text.draw()
                    self.multiplayer = True
                    self.menu = False
            while self.multiplayer:
                self.get_time()
                pygame.mixer.music.play(2)
                self.screen.fill(self.player_screen)
                self.pop()
                self.bubbles.draw(self.screen)
                self.create_more()
                self.scoreboard.draw_score(str(self.score), (550, 30))
                self.scoreboard.draw_score(str(int(self.timer / 1000)), (1100, 30))
                pygame.display.flip()
                if self.timer > 60000:
                    self.screen.fill(self.player_screen)
                    self.scoreboard.draw_score(str(self.score), (600, 400))
                    self.scoreboard.draw_score('PLAYER 1', (470, 30))
                    pygame.display.flip()
                    sleep(3)
                    self.screen.fill(self.player_screen)
                    self.dynamic_text.draw()
                    self.turn += 1
                    self.score = 0
                    pass
                if self.timer > 60000 and self.turn > 1:
                    self.screen.fill(self.player_screen)
                    self.screen.fill(self.player_screen)
                    self.scoreboard.draw_score(str(self.score), (600, 400))
                    self.scoreboard.draw_score('PLAYER 2', (470, 30))
                    self.scoreboard.draw_score('Game Over', (470, 200))
                    pygame.display.flip()
                    sleep(3)
                    pygame.quit()
            while self.singleplayer:
                self.get_time()
                pygame.mixer.music.play(2)
                # check for mouse click on either button to start its respective game mode.
                self.screen.fill(self.player_screen)
                self.pop()
                self.bubbles.draw(self.screen)
                self.create_more()
                self.scoreboard.draw_score(str(self.score), (550, 30))
                self.scoreboard.draw_score(str(int(self.timer / 1000)), (1100, 30))
                pygame.display.flip()
                if self.timer > 60000:
                    self.screen.fill(self.player_screen)
                    self.scoreboard.draw_score(str(self.score), (600, 400))
                    self.scoreboard.draw_score('Game Over!', (470, 30))
                    pygame.display.flip()
                    sleep(3)
                    pygame.quit()


if __name__ == '__main__':
    to = TypeOff()
    to.run_game()
