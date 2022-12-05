import pygame
from time import sleep


class Dynamic_Text:
    def __init__(self):
        # initializing all parameters, colors, and fonts
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('verdana', 70)
        self.sec = 1000
        self.black = (255, 255, 255)

    def create_text(self):
        self.img3 = self.font.render('3', True, self.black)
        self.img2 = self.font.render('2', True, self.black)
        self.img1 = self.font.render('1', True, self.black)
    # Draws text dynamically
    def draw(self):
        self.create_text()
        self.screen.blit(self.img3, (200, 200))
        pygame.display.flip()
        sleep(1)
        self.screen.blit(self.img2, (400, 200))
        pygame.display.flip()
        sleep(1)
        self.screen.blit(self.img1, (600, 200))
        pygame.display.flip()
        sleep(1)
