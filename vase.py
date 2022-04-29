import pygame
import constants
from utils import Utils
import os
from objects import InteractiveObjetcs


class Vase(InteractiveObjetcs):
    
    def __init__(self, x, y, position_mode):
        self.vase_image = os.path.join(constants.IMAGES_DIR, 'vase 1.png')
        super().__init__(self.vase_image, x, y, position_mode, (69, 60))


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


class DecorationVase1(Vase):

    def __init__(self, x, y, position_mode):
        self.vase_image = os.path.join(constants.IMAGES_DIR, 'vase 1.png')
        super().__init__(self.vase_image, x, y, position_mode, (69, 60))

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
        width = 0.9*constants.WIDTH

        message = "Nada acontece."

        options = {'centralized', 'text_offset'}
        parameters = {'message': message, 'font_size': 18,
            'width': width, 'height': 0.40*constants.HEIGHT,
            'x_text': 0.5*width, 'y_text': 0.2*0.24*constants.HEIGHT
        }
        Utils().print_message(options, parameters)


class DecorationVase2(Vase):

    def __init__(self, x, y, position_mode):
        self.vase_image = os.path.join(constants.IMAGES_DIR, 'vase 2.png')
        super().__init__(self.vase_image, x, y, position_mode, (69, 60))

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
        width = 0.9*constants.WIDTH

        message = "Vaso vazio."

        options = {'centralized', 'text_offset'}
        parameters = {'message': message, 'font_size': 18,
            'width': width, 'height': 0.40*constants.HEIGHT,
            'x_text': 0.5*width, 'y_text': 0.2*0.24*constants.HEIGHT
        }
        Utils().print_message(options, parameters)


class DecorationVaseStar(Vase):

    def __init__(self, x, y, position_mode):
        self.vase_image = os.path.join(constants.IMAGES_DIR, 'vase star.png')
        super().__init__(self.vase_image, x, y, position_mode, (69, 60))

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
        width = 0.9*constants.WIDTH

        message = "Nada há nada além de uma estrela no vaso."

        options = {'centralized', 'text_offset'}
        parameters = {'message': message, 'font_size': 18,
            'width': width, 'height': 0.40*constants.HEIGHT,
            'x_text': 0.5*width, 'y_text': 0.2*0.24*constants.HEIGHT
        }
        Utils().print_message(options, parameters)
