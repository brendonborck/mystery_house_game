import pygame
import constants
from utils import Utils
import os
from objects import InteractiveObjetcs


class Safe(InteractiveObjetcs):
    """
        Classe que define os parametros básicos do cofre
    """
    def __init__(self, x, y, position_mode):
        self.safe_image = os.path.join(constants.IMAGES_DIR, 'safebox.png')
        super().__init__(self.safe_image, x, y, position_mode, (80, 100))
        self.puzzle_completed = False


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


class Safebox3(Safe):
    """
        Classe que define os parametros básicos de um cofre
    """
    def interaction(self, player):
        if 'key_room_return_3' in player.pocket:
            options = {'centralized', 'persistent'}
            parameters = {'message': 'Você usou duas chaves e ganhou outra.', 'font_size': 26,
                'width': 0.9*constants.WIDTH, 'height': 0.23*constants.HEIGHT,
                'wait_time': 1.4
            }
            Utils().print_message(options, parameters)
            player.pocket.remove('key_room_return_2')
            player.pocket.remove('key_room_return_3')
            player.pocket.append('key_room_3')
            player.stop_acting()
        else:
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

        message = "O passado nos molda..."

        options = {'centralized'}
        parameters = {'message': message, 'font_size': 20,
            'width': 0.72*constants.WIDTH, 'height': 0.1*constants.HEIGHT,
        }
        Utils().print_message(options, parameters)
