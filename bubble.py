from random import randint
import pygame
from operations import bubbles, lvl1, lvl2


class Bubble:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = 'string does not match bubble[7]'
        self.rect = "does not match"

    def draw1(self):
        for bubble in bubbles:
            if str(lvl1) in bubble[7]:
                self.image = pygame.image.load(bubble)
        # Generate bubble at random
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 1200)
        self.rect.y = randint(0, 800)
        if self.rect.right >= 1200:
            self.rect.right = 1200
        if self.rect.bottom >= 800:
            self.rect.bottom = 800
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def draw2(self):
        # For level 2, match an image in list(bubbles) to each letter in the randomly generated three-letter word.
        for bubble in bubbles:
            if bubble[7] not in lvl2:
                pass
            if bubble[7] in lvl2:
                print(bubble[7])
                self.image = pygame.image.load(bubble)
            # Get rectangle for each bubble
            self.rect = self.image.get_rect()
            self.rect.x = randint(0, 1200)
            self.rect.y = randint(0, 800)
            if self.rect.right >= 1200:
                self.rect.right = 1200
            if self.rect.bottom >= 800:
                self.rect.bottom = 800
            self.screen.blit(self.image, (self.rect.x, self.rect.y))
