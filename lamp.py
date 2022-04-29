import pygame
import constants
from utils import Utils
import os
from objects import InteractiveObjetcs


class Lamp(InteractiveObjetcs):
    """
        Classe que define os parametros básicos de uma lampada que estão nas salas
    """
    def __init__(self, x, y, position_mode):
        self.lamp_image = os.path.join(constants.IMAGES_DIR, 'lamp 1.png')
        super().__init__(self.lamp_image, x, y, position_mode, (69, 60))

    def after_interaction(self):
        pass


    def define_mask(self):
        mask_width = self.width*1.2
        mask_height = self.height*1.2
        mask = pygame.mask.Mask((mask_width, mask_height), False)
        rect_width = 0.8*mask_width
        rect_height = 0.8*mask_height
        position = ((mask_width - rect_width)/2, (mask_height - rect_height)/2)
        rect = pygame.mask.Mask((rect_width, rect_height), True)
        mask.draw(rect, position)
        return mask


class DecorationLamp(Lamp):
    """
        Classe que define uma lampada de decoração do tipo 1
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
        
        message = "Não há nada aqui."

        options = {'centralized'}
        parameters = {'message': message, 'font_size': 20,
            'width': 0.72*constants.WIDTH, 'height': 0.1*constants.HEIGHT,
        }
        Utils().print_message(options, parameters)


class DecorationLamp2(Lamp):
    """
        Classe que define uma lampada de decoração do tipo 2
    """
    def __init__(self, x, y, position_mode):
        self.lamp_image = os.path.join(constants.IMAGES_DIR, 'lamp 2.png')
        super().__init__(self.lamp_image, x, y, position_mode, (69, 60))

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

        message = "Um abajur aceso."

        options = {'centralized'}
        parameters = {'message': message, 'font_size': 20,
            'width': 0.72*constants.WIDTH, 'height': 0.1*constants.HEIGHT,
        }
        Utils().print_message(options, parameters)
