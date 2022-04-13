import pygame
import constants
from utils import Utils
import os
from objects import InteractiveObjetcs


class Door(InteractiveObjetcs):
    
    def __init__(self, x, y, position_mode):
        self.closed_door_image = os.path.join(constants.IMAGES_DIR, 'closed_door.png')
        self.open_door_image = os.path.join(constants.IMAGES_DIR, 'open_door.png')
        super().__init__(self.closed_door_image, x, y, position_mode)
        self.puzzle_completed = False


    def after_interaction(self):
        pass


    def define_mask(self):
        mask = pygame.mask.from_surface(self.image)
        mask.clear()
        mask_width = 0.2*self.width
        mask_height = self.height
        position = ((self.width - mask_width)/2, self.height - mask_height)
        rect = pygame.mask.Mask((mask_width, mask_height), True)
        mask.draw(rect, position)
        return mask


class Door1(Door):

    def interaction(self, player):        
        self.print_pop_up()

        in_pop_up = True
        password_input = ''
        password = 'senha'
        user_returned = False
        while in_pop_up:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #TODO
                    pass
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        in_pop_up = False
                        player.stop_acting()
                    elif event.key == pygame.K_RETURN:
                        in_pop_up = False
                        user_returned = True
                        player.stop_acting()
                        if password_input == password:
                            self.puzzle_completed = True
                        else:
                            self.puzzle_completed = False
                    elif event.key == pygame.K_BACKSPACE:
                        password_input = password_input[:-1]
                        self.print_password(password_input)
                    elif event.key == pygame.K_SPACE:
                        password_input += event.unicode
                        self.print_password(password_input)
                    elif event.unicode:
                        password_input += event.unicode
                        self.print_password(password_input)

        h = 0.2*constants.HEIGHT
        w = 0.5*constants.WIDTH
        if self.puzzle_completed and user_returned:
            self.image = pygame.image.load(self.open_door_image).convert_alpha()
            constants.SCREEN.blit(self.image, self.rect)
            player.draw_player()
            parameters = {'message': 'Senha correta!', 'wait_time': 1.4,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
            player.passed_room = True
        elif user_returned:
            parameters = {'message': 'Senha incorreta', 'wait_time': 0.8,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
    
    
    def print_pop_up(self):
        options = {'centralized', 'text_offset'}
        parameters = {'message': 'Porta trancada', 'font_size': 40,
            'width': 0.5*constants.WIDTH, 'height': 0.23*constants.HEIGHT,
            'x_text': 0.25*constants.WIDTH, 'y_text': 0.06*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        options = {}
        parameters = {'message': 'Insira a senha:', 'font_size': 20,
            'width': 0.5*constants.WIDTH, 'height': 0.03*constants.HEIGHT,
            'x_pop_up': 0.5*constants.WIDTH, 'y_pop_up': 0.51*constants.HEIGHT
        }
        Utils().print_message(options, parameters)
        self.print_password('')


    def print_password(self, password_input):
        options = {'colors'}
        parameters = {'message': password_input, 'font_size': 16,
            'width': 0.4*constants.WIDTH, 'height': 0.03*constants.HEIGHT,
            'x_pop_up': 0.5*constants.WIDTH, 'y_pop_up': 0.57*constants.HEIGHT,
            'text_color': constants.BLACK, 'pop_up_color': constants.WHITE
        }
        Utils().print_message(options, parameters)



class Door2(Door):

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
        message = 'Melhor não voltar para lá.'
        options = {'centralized'}
        parameters = {'message': message, 'font_size': 20,
            'width': 0.4*constants.WIDTH, 'height': 0.2*constants.HEIGHT,
        }
        Utils().print_message(options, parameters)