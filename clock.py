import pygame
import constants
from utils import Utils
import os
from objects import InteractiveObjetcs


class Clock(InteractiveObjetcs):
    """
        Classe que define os parametros básicos dos relógios do código
    """
    def __init__(self, x, y, position_mode):
        self.clock_image = os.path.join(constants.IMAGES_DIR, 'clock.png')
        super().__init__(self.clock_image, x, y, position_mode, (69, 60))


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


class Clock1(Clock):
    """
        Classe que define o relógio da sala 1
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
        message = 'Um Simples relógio, nada a mais'
        options = {'centralized'}
        parameters = {'message': message, 'font_size': 20,
            'width': 0.72*constants.WIDTH, 'height': 0.1*constants.HEIGHT,
        }
        Utils().print_message(options, parameters)


class Clock2(Clock):
    """
        Classe que define o relógio da sala 2
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
        width = 0.9*constants.WIDTH
        x_pop_up = 0.5*constants.WIDTH

        message1 = "Atras do Relógio há um papel com uma inscrição:"
        message2 = "A mãe luta"
        message3 = "Luta pois ama"
        message4 = "Brinca pois ama."
        message5 = "E mãe luta"
        message6 = "Reluta, mas continua"
        message7 = "Tanto que no final vence...."

        options = {'centralized', 'text_offset'}
        parameters = {'message': message1, 'font_size': 18,
            'width': width, 'height': 0.35*constants.HEIGHT,
            'x_text': 0.5*width, 'y_text': 0.2*0.24*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        options = {}
        parameters = {'message': message2, 'font_size': 18,
            'width': width, 'height': 0.04*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.42*constants.HEIGHT
        }
        Utils().print_message(options, parameters)
        
        parameters = {'message': message3, 'font_size': 18,
            'width': width, 'height': 0.04*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.46*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        parameters = {'message': message4, 'font_size': 18,
            'width': width, 'height': 0.04*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.50*constants.HEIGHT
        }
        Utils().print_message(options, parameters)


        parameters = {'message': message5, 'font_size': 18,
            'width': width, 'height': 0.04*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.54*constants.HEIGHT
        }
        Utils().print_message(options, parameters)
        

        parameters = {'message': message6, 'font_size': 18,
            'width': width, 'height': 0.04*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.58*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        parameters = {'message': message7, 'font_size': 18,
            'width': width, 'height': 0.04*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.62*constants.HEIGHT
        }
        Utils().print_message(options, parameters)
