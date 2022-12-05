import pygame.font
# initialize play button


class Button:
    def __init__(self, ai_game, x, y, w, h):
        # initializing all parameters, colors, and fonts
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = w, h
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('verdana', 70)
        self.rect = pygame.Rect(int(x), int(y), self.width, self.height)

    def create_text(self, msg):
        # rendering text
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)

    def draw_button(self, msg):
        # drawing button with text on top
        self.create_text(msg)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.rect)
