import pygame
import constants
from utils import Utils
import os
from objects import InteractiveObjetcs


class Painting(InteractiveObjetcs):
    """
        Classe que define as funcionalidades básicas para todos os quadros
    """
    def __init__(self, x, y, position_mode):
        self.painting_image = os.path.join(constants.IMAGES_DIR, 'painting.png')
        super().__init__(self.painting_image, x, y, position_mode, (69, 74))


    def after_interaction(self):
        pass


    def define_mask(self):
        mask_width = self.width
        mask_height = constants.Y_SUPERIOR_WALL - self.rect.top
        mask = pygame.mask.Mask((mask_width, mask_height), False)
        rect_width = 0.1*self.width
        rect_height = mask_height
        position = ((mask_width - rect_width)/2, 0)
        rect = pygame.mask.Mask((rect_width, rect_height), True)
        mask.draw(rect, position)
        return mask


class Painting1(Painting):
    """
        Classe que define o quadro do tipo 1
    """
    def interaction(self, player):
        self.print_pop_up()        
        in_pop_up = True
        while in_pop_up:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #TODO
                    pass
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        in_pop_up = False
                    elif event.key == pygame.K_ESCAPE:
                        in_pop_up = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_e:
                        player.stop_acting()


    def print_pop_up(self):
        message = 'Um homem sentado em uma cadeira antiga, Laubert o mais novo'
        options = {'centralized'}
        parameters = {'message': message, 'font_size': 18,
            'width': 0.72*constants.WIDTH, 'height': 0.1*constants.HEIGHT,
        }
        Utils().print_message(options, parameters)