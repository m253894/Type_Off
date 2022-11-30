from random import randint
import pygame
from pygame.sprite import Sprite
import operations


class Bubble(Sprite):
    def __init__(self, ai_game, lvl):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        word = lvl
        for letter in word:
            # correspond each letter in a word with an image in the bubbles list
            bubble = operations.letters.index(letter.upper())
            self.image = pygame.image.load(operations.bubbles[bubble])
            print(word)
            print(bubble)
            # each bubble's position is random
            self.rect = self.image.get_rect()
            self.rect.x = randint(0, 1200)
            self.rect.y = randint(0, 800)
            # make sure the bubble is drawn in the borders
            if self.rect.right >= 1200:
                self.rect.right = 1200
            if self.rect.bottom >= 800:
                self.rect.bottom = 800



