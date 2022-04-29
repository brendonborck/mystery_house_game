from cgitb import text
from multiprocessing.connection import wait
from tkinter import font
import pygame
import constants
import time

class Utils:

    def __init__(self):
        pass

    @staticmethod
    def draw_text(message, font_size, color, x, y):
        font_name = pygame.font.match_font(constants.FONT)
        font = pygame.font.Font(font_name, font_size)
        text = font.render(message, True, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        constants.SCREEN.blit(text, text_rect)

    @staticmethod
    def print_time():
        minutes = int(constants.time_left / 60)
        seconds = int(constants.time_left - 60 * minutes)
        parameters = {
            'message': f"{minutes:02d}" + ':' + f"{seconds:02d}", 
            'x_pop_up': int(0.94*constants.WIDTH), 'y_pop_up': int(0.05*constants.HEIGHT),
            'pop_up_color': constants.WHITE, 'text_color': constants.BLACK, 'width': 0.08*constants.WIDTH,
            'height': 0.04*constants.HEIGHT, 'font_size': 14
        }
        Utils().print_message({'colors'}, parameters)

    @staticmethod
    def print_message(options, parameters):
        
        if 'centralized' in options:
            x_pop_up = constants.WIDTH/2
            y_pop_up = constants.HEIGHT/2
        else:
            x_pop_up = parameters['x_pop_up']
            y_pop_up = parameters['y_pop_up']
        
        if 'full' in options:
            w = constants.WIDTH
            h = constants.HEIGHT
            font_size = 60
        else:
            w = parameters['width']
            h = parameters['height']
            font_size = parameters['font_size']

        if 'text_offset' in options:  
            x_text = parameters['x_text']
            y_text = parameters['y_text']
        else:
            x_text = 0.5*w
            y_text = 0.5*h

        if 'colors' in options:
            text_color = parameters['text_color']
            pop_up_color = parameters['pop_up_color']
        else:
            text_color = constants.WHITE
            pop_up_color = constants.BLACK
    
        message = parameters['message']
    
        text = Text(message, font_size, x_pop_up, y_pop_up, x_text, y_text, w, h, text_color, pop_up_color)
        text_group = pygame.sprite.Group()
        text_group.add(text)
        text_group.draw(constants.SCREEN)
        pygame.display.update()
        
        if 'persistent' in options:
            wait_time = parameters['wait_time']
            time.sleep(wait_time)
            for event in pygame.event.get():
                pass


class Text(pygame.sprite.Sprite):

    def __init__(self, message, font_size, x_pop_up, y_pop_up, x_text, y_text, w, h, text_color, pop_up_color = constants.BLACK):
        super().__init__()
        font_name = pygame.font.match_font(constants.FONT)
        font = pygame.font.Font(font_name, font_size)
        text = font.render(message, True, text_color)
        
        self.image = pygame.Surface([w, h])
        self.image.fill(pop_up_color)
        self.rect = self.image.get_rect()
        self.rect.center = (x_pop_up ,y_pop_up)

        text_rect = text.get_rect()
        x = x_text - text_rect.w/2
        y = y_text - text_rect.h/2
        self.image.blit(text, (x, y))