import pygame
import constants
from utils import Utils
import os
from objects import InteractiveObjetcs


class Wardrobe(InteractiveObjetcs):
    """Classe que define os parametros básicos para o armário"""
    def __init__(self, x, y, position_mode):
        self.Wardrobe = os.path.join(constants.IMAGES_DIR, 'wardrobe.png')
        super().__init__(self.Wardrobe, x, y, position_mode, (103, 184))
        self.puzzle_completed = False


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


class Wardrobe1(Wardrobe):
    """Classe que define armário da sala 1"""
    def interaction(self, player):        
        self.print_pop_up()
        in_pop_up = True
        password_input = ''
        password = 'Albert'
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
                            player.key=True
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
            parameters = {'message': 'Há uma Chave', 'wait_time': 1.4,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
        elif user_returned:
            parameters = {'message': 'Nada Ocorre...', 'wait_time': 0.8,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
    
    
    def print_pop_up(self):
        options = {'centralized', 'text_offset'}
        parameters = {'message': 'Gaveta Trancada', 'font_size': 40,
            'width': 0.5*constants.WIDTH, 'height': 0.23*constants.HEIGHT,
            'x_text': 0.25*constants.WIDTH, 'y_text': 0.06*constants.HEIGHT
        }
        Utils().print_message(options, parameters)


    def print_password(self, password_input):
        options = {'colors'}
        parameters = {'message': password_input, 'font_size': 16,
            'width': 0.4*constants.WIDTH, 'height': 0.03*constants.HEIGHT,
            'x_pop_up': 0.5*constants.WIDTH, 'y_pop_up': 0.57*constants.HEIGHT,
            'text_color': constants.BLACK, 'pop_up_color': constants.WHITE
        }
        Utils().print_message(options, parameters)


class Wardrobe3(Wardrobe):
    """Classe que define armário da sala 3"""
    def interaction(self, player):        
        self.print_pop_up()
        in_pop_up = True
        password_input = ''
        password = 'Albert'
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
                            player.key=True
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
            parameters = {'message': 'Há uma Chave', 'wait_time': 1.4,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
        elif user_returned:
            parameters = {'message': 'Nada Ocorre...', 'wait_time': 0.8,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
    
    
    def print_pop_up(self):
        options = {'centralized', 'text_offset'}
        parameters = {'message': 'Gaveta Trancada', 'font_size': 40,
            'width': 0.5*constants.WIDTH, 'height': 0.23*constants.HEIGHT,
            'x_text': 0.25*constants.WIDTH, 'y_text': 0.06*constants.HEIGHT
        }
        Utils().print_message(options, parameters)


    def print_password(self, password_input):
        options = {'colors'}
        parameters = {'message': password_input, 'font_size': 16,
            'width': 0.4*constants.WIDTH, 'height': 0.03*constants.HEIGHT,
            'x_pop_up': 0.5*constants.WIDTH, 'y_pop_up': 0.57*constants.HEIGHT,
            'text_color': constants.BLACK, 'pop_up_color': constants.WHITE
        }
        Utils().print_message(options, parameters)


class Wardrobe4(Wardrobe):
    """Classe que define armário da sala 4"""
    def interaction(self, player):        
        self.print_pop_up()
        in_pop_up = True
        password_input = ''
        password = 'Albert'
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
                            player.key=True
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
            parameters = {'message': 'Há uma Chave', 'wait_time': 1.4,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
        elif user_returned:
            parameters = {'message': 'Nada Ocorre...', 'wait_time': 0.8,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
    
    
    def print_pop_up(self):
        options = {'centralized', 'text_offset'}
        parameters = {'message': 'Gaveta Trancada', 'font_size': 40,
            'width': 0.5*constants.WIDTH, 'height': 0.23*constants.HEIGHT,
            'x_text': 0.25*constants.WIDTH, 'y_text': 0.06*constants.HEIGHT
        }
        Utils().print_message(options, parameters)


    def print_password(self, password_input):
        options = {'colors'}
        parameters = {'message': password_input, 'font_size': 16,
            'width': 0.4*constants.WIDTH, 'height': 0.03*constants.HEIGHT,
            'x_pop_up': 0.5*constants.WIDTH, 'y_pop_up': 0.57*constants.HEIGHT,
            'text_color': constants.BLACK, 'pop_up_color': constants.WHITE
        }
        Utils().print_message(options, parameters)