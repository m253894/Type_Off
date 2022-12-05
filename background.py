import pygame
from pygame.sprite import Sprite

# Blakeley Cremer helped me pick and insert a background.
# background class
class Background(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/menu_background.jfif')
        self.rect = self.image.get_rect()