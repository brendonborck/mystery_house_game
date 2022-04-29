import pygame
import constants
from utils import Utils
import os
from objects import InteractiveObjetcs


class Writing_Desk(InteractiveObjetcs):
    """
        Classe que define os parametros básicos de uma mesa de escrever
    """
    def __init__(self, x, y, position_mode):
        self.writingdesk = os.path.join(constants.IMAGES_DIR, 'writingdesk.png')
        super().__init__(self.writingdesk, x, y, position_mode, (103, 184))


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


class Writing_Desk1(Writing_Desk):
    """
        Classe que define uma mesa de escrever da sala 1
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
        message = 'Um papel, com um nome escrito "Lady Constock a impiedosa"'
        options = {'centralized'}
        parameters = {'message': message, 'font_size': 20,
            'width': 0.72*constants.WIDTH, 'height': 0.1*constants.HEIGHT,
        }
        Utils().print_message(options, parameters)


class Writing_Desk2(Writing_Desk):
    """
        Classe que define uma mesa de escrever da sala 2
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
        message = "Na Gaveta há uma foto de uma criança junto de sua mãe que lhe traz lembranças..."
        options = {'centralized'}
        parameters = {'message': message, 'font_size': 18,
            'width': 0.85*constants.WIDTH, 'height': 0.1*constants.HEIGHT,
        }
        Utils().print_message(options, parameters)

class Writing_Desk4(Writing_Desk):
    """
        Classe que define uma mesa de escrever da sala 4
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
        width = 0.94*constants.WIDTH
        x_pop_up = 0.5*constants.WIDTH

        message1 = "Dentro há uma carta escrita com letras graciosas de uma mulher..."
        message2 = "Meu filho, estou preocupada com o que você vai fazer com o seu irmão de menor IDADE, "
        message3 = "eu sei que ele fez uma coisa errada, mas isso não justifica essa tortura sobre ele,..."

        options = {}
        parameters = {'message': message1, 'font_size': 18,
            'width': width, 'height': 0.06*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.48*constants.HEIGHT
        }
        Utils().print_message(options, parameters)
        
        parameters = {'message': message2, 'font_size': 18,
            'width': width, 'height': 0.06*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.52*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        parameters = {'message': message3, 'font_size': 18,
            'width': width, 'height': 0.06*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.56*constants.HEIGHT
        }
        Utils().print_message(options, parameters)