import pygame.font
# initialize play button
class Button:
    def __init__(self, ai_game, msg):
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.single_msg(msg)
        self.multi_msg(msg)

    def single_msg(self, msg):

        self.player_screen1 = (0, 0, 230)
        self.player_screen2 = (230, 0, 0)
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.x = 200
        self.msg_image_rect.y = 200
        self.screen.fill(self.player_screen1)

    def multi_msg(self, msg):

        self.player_screen1 = (0, 0, 230)
        self.player_screen2 = (230, 0, 0)
        self.mssg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.mssg_image_rect = self.mssg_image.get_rect()
        self.msg_image_rect.x = 800
        self.msg_image_rect.y = 200
        self.screen.fill(self.player_screen2)

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

