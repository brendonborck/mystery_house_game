import pygame
import constants
from utils import Utils
import os
from objects import InteractiveObjetcs


class Wardrobe(InteractiveObjetcs):
    """
        Classe que define os parametros básicos para o armário
    """
    def __init__(self, x, y, position_mode, scale = None):
        super().__init__(self.link_image, x, y, position_mode, scale)
        self.puzzle_completed = False


    def after_interaction(self):
        pass


    def define_mask(self):
        mask_width = self.width
        mask_height = self.height*1.2
        mask = pygame.mask.Mask((mask_width, mask_height), False)
        rect_width = mask_width
        rect_height = mask_height
        position = ((self.width - rect_width)/2, (self.height - rect_height)/2)
        rect = pygame.mask.Mask((rect_width, rect_height), True)
        mask.draw(rect, position)
        return mask


class Wardrobe2(Wardrobe):

    """
        Classe que define armário da sala 2
    """
    def __init__(self, x, y, position_mode):
        self.link_image = os.path.join(constants.IMAGES_DIR, 'wardrobe.png')
        super().__init__(x, y, position_mode, (105, 185))

    def interaction(self, player):
        if 'key_room_2' in player.pocket:
            options = {'centralized', 'persistent'}
            parameters = {'message': 'Não há mais nada aqui', 'font_size': 40,
                'width': 0.56*constants.WIDTH, 'height': 0.23*constants.HEIGHT,
                'wait_time': 1.0
            }
            Utils().print_message(options, parameters)
            player.stop_acting()
        else:    
            self.print_pop_up()
            in_pop_up = True
            password_input = ''
            password = 'albert'
            user_returned = False
            while in_pop_up:
                constants.clock.tick(constants.FPS)
                if constants.countdown:
                    constants.time_left -= constants.clock.get_time()/1000
                    Utils().print_time()
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
                            if password_input.lower() == password:
                                self.puzzle_completed = True
                                player.pocket.append('key_room_2')
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

                h = 0.23*constants.HEIGHT
                w = 0.5*constants.WIDTH
                if self.puzzle_completed and user_returned:
                    w = 0.56*constants.WIDTH
                    parameters = {'message': 'Você pegou uma chave!', 'wait_time': 1.4,
                        'font_size': 40, 'width': w, 'height': h
                    }
                    Utils().print_message({'centralized', 'persistent'}, parameters)
                elif user_returned:
                    w = 0.5*constants.WIDTH
                    parameters = {'message': 'Nada ocorre...', 'wait_time': 0.8,
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

        options = {}
        parameters = {'message': 'Insira a senha:', 'font_size': 16,
            'width': 0.5*constants.WIDTH, 'height': 0.03*constants.HEIGHT,
            'x_pop_up': 0.5*constants.WIDTH, 'y_pop_up': 0.52*constants.HEIGHT
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


class Wardrobe2Rem(Wardrobe):

    """
        Classe que define armário da sala 3
    """
    def __init__(self, x, y, position_mode):
        self.link_image = os.path.join(constants.IMAGES_DIR, 'wardrobe.png')
        super().__init__(x, y, position_mode, (105, 185))

    def interaction(self, player):
        self.print_pop_up()        
        player.stop_acting()


    def print_pop_up(self):
        message = "Não há mais nada aqui."
        options = {'centralized', 'persistent'}
        parameters = {'message': message, 'font_size': 20, 'wait_time': 1.0,
            'width': 0.72*constants.WIDTH, 'height': 0.1*constants.HEIGHT,
        }
        Utils().print_message(options, parameters)


class Wardrobe3(Wardrobe):

    """
        Classe que define armário da sala 3
    """
    def __init__(self, x, y, position_mode):
        self.link_image = os.path.join(constants.IMAGES_DIR, 'shelf 2.png')
        super().__init__(x, y, position_mode, (130, 200))

    def interaction(self, player):
        self.print_pop_up()        
        player.stop_acting()


    def print_pop_up(self):
        message = "Não há nada"
        options = {'centralized', 'persistent'}
        parameters = {'message': message, 'font_size': 20, 'wait_time': 1,
            'width': 0.72*constants.WIDTH, 'height': 0.1*constants.HEIGHT,
        }
        Utils().print_message(options, parameters)


class Wardrobe4(Wardrobe):

    """
        Classe que define armário da sala 4
    """
    def __init__(self, x, y, position_mode):
        self.link_image = os.path.join(constants.IMAGES_DIR, 'wine wardrobe.png')
        super().__init__(x, y, position_mode, (85, 160))

    def interaction(self, player):
        self.print_pop_up()        
        in_pop_up = True
        while in_pop_up:
            constants.clock.tick(constants.FPS)
            if constants.countdown:
                constants.time_left -= constants.clock.get_time()/1000
                Utils().print_time()
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

        message1 = "O PASSADO nos diz muita coisa"
        message2 = "Por vezes, as CHAVES de nossa vida tornam nossa vida complicada"
        message3 = "Mas com o tempo tudo vai se tornando normal..."

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