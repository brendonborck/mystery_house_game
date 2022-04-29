import pygame
import constants
from utils import Utils
import os
from objects import InteractiveObjetcs


class Bed(InteractiveObjetcs):
    """
        Classe que determina os métodos básicos das camas de cada sala
    """
    def __init__(self, x, y, position_mode):
        self.bed_image = os.path.join(constants.IMAGES_DIR, 'bed.png')
        super().__init__(self.bed_image, x, y, position_mode, (100, 150))


    def after_interaction(self):
        pass


    def define_mask(self):
<<<<<<< HEAD
        mask_width = self.width*1.8
        mask_height = self.height*1.8
=======
        mask_width = self.width
        mask_height = self.height
>>>>>>> 587c94e080113df5ea91b6cb361dbacf38e0431e
        mask = pygame.mask.Mask((mask_width, mask_height), False)
        rect_width = mask_width
        rect_height = mask_height
        position = ((self.width - rect_width)/2, (self.height - rect_height)/2)
        rect = pygame.mask.Mask((rect_width, rect_height), True)
        mask.draw(rect, position)
        return mask


class Bed1(Bed):
    """
        Classe da cama da sala 1
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
        message = 'Uma Cama normal com uma inscrição: Laurent o Pacificador'
        options = {'centralized'}
        parameters = {'message': message, 'font_size': 20,
            'width': 0.72*constants.WIDTH, 'height': 0.1*constants.HEIGHT,
        }
        Utils().print_message(options, parameters)


class Bed2(Bed):
    """
        Classe da cama da sala 2
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
        message = 'Nada de mais...'
        options = {'centralized'}
        parameters = {'message': message, 'font_size': 20,
            'width': 0.72*constants.WIDTH, 'height': 0.1*constants.HEIGHT,
        }
        Utils().print_message(options, parameters)

class Bed3(Bed):
    """
        Classe da cama da sala 3
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

        message1 = "Embaixo da cama há uma foto de uma mulher e um homem, com uma inscrição:"
        message2 = "Sua Majestade Albert e  Rainha Isabella Constock"

        options = {}
        parameters = {'message': message1, 'font_size': 16,
            'width': width, 'height': 0.06*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.48*constants.HEIGHT
        }
        Utils().print_message(options, parameters)
        
        parameters = {'message': message2, 'font_size': 18,
            'width': width, 'height': 0.06*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.52*constants.HEIGHT
        }
        Utils().print_message(options, parameters)


class Bed4(Bed):
    """
        Classe da cama da sala 4
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
        message = "Simples cama."
        options = {'centralized'}
        parameters = {'message': message, 'font_size': 20,
            'width': 0.72*constants.WIDTH, 'height': 0.1*constants.HEIGHT,
        }
        Utils().print_message(options, parameters)