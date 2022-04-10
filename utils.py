import pygame
import constants

class Utils:

    def __init__(self):
        pass

    @staticmethod
    def draw_text(screen, message, font_size, color, x, y):
        #Exibe um text na screen do jogo
        font_name = pygame.font.match_font(constants.FONT)
        font = pygame.font.Font(font_name, font_size)
        text = font.render(message, True, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        screen.blit(text, text_rect)


class Text(pygame.sprite.Sprite):

    def __init__(self, message, font_size, x_pop_up, y_pop_up, x_text, y_text, width, height, text_color, pop_up_color = constants.BLACK):
        super().__init__()
        font_name = pygame.font.match_font(constants.FONT)
        font = pygame.font.Font(font_name, font_size)
        text = font.render(message, True, text_color)
        
        self.image = pygame.Surface([width, height])
        self.image.fill(pop_up_color)
        self.rect = self.image.get_rect()
        self.rect.center = (x_pop_up ,y_pop_up)

        text_rect = text.get_rect()
        x = x_text - text_rect.w/2
        y = y_text - text_rect.h/2
        self.image.blit(text, (x, y))