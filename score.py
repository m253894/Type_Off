import pygame
import game

# Main way to print text to the screen
class Scoreboard:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont('verdana', 48)
    # renders text
    def create_score(self, score):
        self.score_txt = self.font.render(score, True, self.text_color)
    # prints text
    def draw_score(self, score, rect):
        self.create_score(score)
        self.screen.blit(self.score_txt, rect)
