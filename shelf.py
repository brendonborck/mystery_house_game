import pygame
import constants
from utils import Utils
import os
from objects import InteractiveObjetcs


class Shelf(InteractiveObjetcs):
    """
        Classe que define o métodos básicos de uma estante
    """
    def __init__(self, x, y, position_mode):
        self.shelf_image = os.path.join(constants.IMAGES_DIR, 'shelf.png')
        super().__init__(self.shelf_image, x, y, position_mode, (69, 60))

    def after_interaction(self):
        pass

    def define_mask(self):
        mask_width = self.width*1.2
        mask_height = self.height*1.2
        mask = pygame.mask.Mask((mask_width, mask_height), False)
        rect_width = 0.8*mask_width
        rect_height = 0.8*mask_height
        position = ((mask_width - rect_width)/2, (mask_height - rect_width)/2)
        rect = pygame.mask.Mask((rect_width, rect_height), True)
        mask.draw(rect, position)
        return mask


class DecorationShelfBooks(Shelf):
    """
        Classe que define uma estante de livros decorativa
    """
    def __init__(self, x, y, position_mode):
        self.shelf_image = os.path.join(constants.IMAGES_DIR, 'shelf - books.png')
        super().__init__(self.shelf_image, x, y, position_mode, (69, 60))

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

        message = "Livros e mais livros..."

        options = {'centralized', 'text_offset'}
        parameters = {'message': message, 'font_size': 18,
            'width': width, 'height': 0.40*constants.HEIGHT,
            'x_text': 0.5*width, 'y_text': 0.2*0.24*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

class DecorationEmptyWardrobe(Shelf):
    """
        Classe que define uma estante vazia
    """
    def __init__(self, x, y, position_mode):
        self.shelf_image = os.path.join(constants.IMAGES_DIR, 'wardrobe - empty.png')
        super().__init__(self.shelf_image, x, y, position_mode, (69, 60))

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

        message = "Não há nada dentro."

        options = {'centralized', 'text_offset'}
        parameters = {'message': message, 'font_size': 18,
            'width': width, 'height': 0.40*constants.HEIGHT,
            'x_text': 0.5*width, 'y_text': 0.2*0.24*constants.HEIGHT
        }
        Utils().print_message(options, parameters)