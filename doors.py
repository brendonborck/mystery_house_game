import pygame
import constants
from utils import Utils
import os
from objects import InteractiveObjetcs


class Door(InteractiveObjetcs): 
    """
        Classe que define os parametros básicos para as portas da sala
    """
    def __init__(self, x, y, position_mode):
        self.closed_door_image = os.path.join(constants.IMAGES_DIR, 'door closed.png')
        self.open_door_image = os.path.join(constants.IMAGES_DIR, 'door opened 2.png')
        super().__init__(self.closed_door_image, x, y, position_mode, (85,130))
        self.puzzle_completed = False

    def after_interaction(self):
        pass

    def define_mask(self):
        mask_width = self.width
        mask_height = self.height*1.2
        mask = pygame.mask.Mask((mask_width, mask_height), False)
        rect_width = 0.2*mask_width
        rect_height = mask_height
        position = ((mask_width - rect_width)/2, 0)
        rect = pygame.mask.Mask((rect_width, rect_height), True)
        mask.draw(rect, position)
        return mask


class Door1(Door):
    """
        Classe que define a porta da sala 1
    """
    def interaction(self, player):        
        self.print_pop_up()

        in_pop_up = True
        password_input = ''
        password = 'laubert'
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
                        if password_input.lower() == password:
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

        h = 0.26*constants.HEIGHT
        w = 0.58*constants.WIDTH
        if self.puzzle_completed and user_returned:
            self.image = pygame.image.load(self.open_door_image).convert_alpha()
            self.image = pygame.transform.scale(self.image, (105, 130))
            constants.SCREEN.blit(self.image, self.rect)
            player.draw_player()
            parameters = {'message': 'A porta se abre', 'wait_time': 1.4,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
            player.passed_room = True
        elif user_returned:
            parameters = {'message': 'Nada ocorre...', 'wait_time': 0.8,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
    
    
    def print_pop_up(self):
        options = {'centralized', 'text_offset'}
        parameters = {'message': 'Porta trancada', 'font_size': 40,
            'width': 0.58*constants.WIDTH, 'height': 0.26*constants.HEIGHT,
            'x_text': 0.29*constants.WIDTH, 'y_text': 0.04*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        options = {}
        parameters = {'message': 'Há um cadeado na porta, escrito "Mais Novo"', 'font_size': 20,
            'width': 0.56*constants.WIDTH, 'height': 0.03*constants.HEIGHT,
            'x_pop_up': 0.5*constants.WIDTH, 'y_pop_up': 0.48*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        options = {}
        parameters = {'message': 'Insira a senha:', 'font_size': 16,
            'width': 0.56*constants.WIDTH, 'height': 0.03*constants.HEIGHT,
            'x_pop_up': 0.5*constants.WIDTH, 'y_pop_up': 0.54*constants.HEIGHT
        }
        Utils().print_message(options, parameters)
        self.print_password('')


    def print_password(self, password_input):
        options = {'colors'}
        parameters = {'message': password_input, 'font_size': 16,
            'width': 0.4*constants.WIDTH, 'height': 0.03*constants.HEIGHT,
            'x_pop_up': 0.5*constants.WIDTH, 'y_pop_up': 0.59*constants.HEIGHT,
            'text_color': constants.BLACK, 'pop_up_color': constants.WHITE
        }
        Utils().print_message(options, parameters)


class Door2(Door):
    """
        Classe que define a porta da sala 2
    """
    def __init__(self, x, y, position_mode):
        super().__init__(x, y, position_mode)
        self.closed_door_image = os.path.join(constants.IMAGES_DIR, 'door closed.png')
        self.open_door_image = os.path.join(constants.IMAGES_DIR, 'door stairs.png')
        self.puzzle_completed = False
    
    def interaction(self, player):        
        player.stop_acting()
        if 'key_room_2' in player.pocket:
            if 'key_room_2' in player.pocket:
                player.pocket.remove('key_room_2')
            self.puzzle_completed = True
        elif 'key_room_return_3' in player.pocket:
            self.puzzle_completed = True
        else:
            self.print_pop_up()

        h = 0.2*constants.HEIGHT
        w = 0.5*constants.WIDTH
        if self.puzzle_completed:
            self.image = pygame.image.load(self.open_door_image).convert_alpha()
            self.image = pygame.transform.scale(self.image, (105, 130))
            constants.SCREEN.blit(self.image, self.rect)
            player.draw_player()
            parameters = {'message': 'Usou a Chave', 'wait_time': 1.4,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
            player.passed_room = True


    def print_pop_up(self):
        options = {'centralized', 'persistent'}
        parameters = {'message': 'Nada ocorre...', 'font_size': 40, 'wait_time': 0.8,
            'width': 0.5*constants.WIDTH, 'height': 0.23*constants.HEIGHT
        }
        Utils().print_message(options, parameters)


class Door2to3(Door):
    """
        Classe que define a porta vindo da sala 3
    """
    def __init__(self, x, y, position_mode):
        super().__init__(x, y, position_mode)
        self.closed_door_image = os.path.join(constants.IMAGES_DIR, 'door closed.png')
        self.open_door_image = os.path.join(constants.IMAGES_DIR, 'door opened 2.png')
        self.image = pygame.image.load(self.closed_door_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (85, 130))

    def interaction(self, player):        
        player.stop_acting()
        self.print_pop_up()

    def print_pop_up(self):
        options = {'centralized', 'persistent'}
        parameters = {'message': 'Sem maçaneta.', 'font_size': 40, 'wait_time': 0.8,
            'width': 0.5*constants.WIDTH, 'height': 0.23*constants.HEIGHT
        }
        Utils().print_message(options, parameters)


class Door2to3Rem(Door):
    """
        Classe que define a porta vindo da sala 3 na fase de lembrança
    """
    def __init__(self, x, y, position_mode):
        super().__init__(x, y, position_mode)
        self.closed_door_image = os.path.join(constants.IMAGES_DIR, 'door closed.png')
        self.open_door_image = os.path.join(constants.IMAGES_DIR, 'door opened 2.png')
        self.image = pygame.image.load(self.open_door_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (105, 130))

    def interaction(self, player):        
        player.stop_acting()
        self.print_pop_up()

    def print_pop_up(self):
        options = {'centralized', 'persistent'}
        parameters = {'message': 'Você não consegue mais subir por aqui.', 'font_size': 30, 'wait_time': 1.4,
            'width': 0.72*constants.WIDTH, 'height': 0.18*constants.HEIGHT,
        }
        Utils().print_message(options, parameters)


class Door3(Door):
    """
        Classe que define a porta da sala 3
    """
    def __init__(self, x, y, position_mode):
        super().__init__(x, y, position_mode)
        self.closed_door_image = os.path.join(constants.IMAGES_DIR, 'dark door closed.png')
        self.open_door_image = os.path.join(constants.IMAGES_DIR, 'dark door opened.png')
        self.image = pygame.image.load(self.closed_door_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (85, 130))
        self.puzzle_completed = False

    def interaction(self, player):        
        player.stop_acting()
        if 'key_room_3' in player.pocket:
            player.pocket.remove('key_room_3')
            self.puzzle_completed = True
        else:
            self.print_pop_up()

        h = 0.2*constants.HEIGHT
        w = 0.5*constants.WIDTH
        if self.puzzle_completed:
            self.image = pygame.image.load(self.open_door_image).convert_alpha()
            self.image = pygame.transform.scale(self.image, (105, 130))
            constants.SCREEN.blit(self.image, self.rect)
            player.draw_player()
            parameters = {'message': 'Usou a Chave', 'wait_time': 1.4,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
            player.passed_room = True


    def print_pop_up(self):
        options = {'centralized', 'persistent'}
        parameters = {'message': 'Nada ocorre...', 'font_size': 40, 'wait_time': 0.8,
            'width': 0.5*constants.WIDTH, 'height': 0.23*constants.HEIGHT
        }
        Utils().print_message(options, parameters)


class Door3to2(Door):
    """
        Classe que define a porta da sala 3 que volta para sala 2
    """
    def __init__(self, x, y, position_mode):
        super().__init__(x, y, position_mode)
        self.closed_door_image = os.path.join(constants.IMAGES_DIR, 'door closed.png')
        self.open_door_image = os.path.join(constants.IMAGES_DIR, 'door opened 2.png')
        self.image = pygame.image.load(self.closed_door_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (85, 130))
        self.puzzle_completed = False

    def interaction(self, player):        
        player.stop_acting()
        if 'key_room_return_2' in player.pocket and 'key_room_return_3' not in player.pocket:
            self.puzzle_completed = True
        else:
            self.print_pop_up()

        h = 0.2*constants.HEIGHT
        w = 0.5*constants.WIDTH
        if self.puzzle_completed:
            self.image = pygame.image.load(self.open_door_image).convert_alpha()
            self.image = pygame.transform.scale(self.image, (105, 130))
            constants.SCREEN.blit(self.image, self.rect)
            player.draw_player()
            parameters = {'message': 'Usou a Chave', 'wait_time': 1.4,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
            player.passed_room = True


    def print_pop_up(self):
        options = {'centralized', 'persistent'}
        parameters = {'message': 'Você não consegue passar por aqui.', 'font_size': 30, 'wait_time': 1.2,
            'width': 0.65*constants.WIDTH, 'height': 0.23*constants.HEIGHT
        }
        Utils().print_message(options, parameters)


class Door4(Door):
    """
        Classe que define a porta da sala 4
    """
    def __init__(self, x, y, position_mode):
        super().__init__(x, y, position_mode)
        self.closed_door_image = os.path.join(constants.IMAGES_DIR, 'dark door closed.png')
        self.open_door_image = os.path.join(constants.IMAGES_DIR, 'dark door.png')
        self.image = pygame.image.load(self.closed_door_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (85, 130))
        self.puzzle_completed = False

    def interaction(self, player):        
        self.print_pop_up()

        in_pop_up = True
        password_input = ''
        password = '28'
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
                        if password_input.lower() == password:
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

        h = 0.26*constants.HEIGHT
        w = 0.58*constants.WIDTH
        if self.puzzle_completed and user_returned:
            self.image = pygame.image.load(self.open_door_image).convert_alpha()
            self.image = pygame.transform.scale(self.image, (85, 130))
            constants.SCREEN.blit(self.image, self.rect)
            player.draw_player()
            parameters = {'message': 'A porta se abre', 'wait_time': 1.4,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
            player.passed_room = True
        elif user_returned:
            parameters = {'message': 'Nada ocorre...', 'wait_time': 0.8,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
    
    
    def print_pop_up(self):
        options = {'centralized', 'text_offset'}
        parameters = {'message': 'Porta trancada', 'font_size': 40,
            'width': 0.58*constants.WIDTH, 'height': 0.26*constants.HEIGHT,
            'x_text': 0.29*constants.WIDTH, 'y_text': 0.04*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        options = {}
        parameters = {'message': 'Insira a senha:', 'font_size': 16,
            'width': 0.56*constants.WIDTH, 'height': 0.03*constants.HEIGHT,
            'x_pop_up': 0.5*constants.WIDTH, 'y_pop_up': 0.54*constants.HEIGHT
        }
        Utils().print_message(options, parameters)
        self.print_password('')


    def print_password(self, password_input):
        options = {'colors'}
        parameters = {'message': password_input, 'font_size': 16,
            'width': 0.4*constants.WIDTH, 'height': 0.03*constants.HEIGHT,
            'x_pop_up': 0.5*constants.WIDTH, 'y_pop_up': 0.59*constants.HEIGHT,
            'text_color': constants.BLACK, 'pop_up_color': constants.WHITE
        }
        Utils().print_message(options, parameters)


class Door5(Door):
    """
        Classe que define a porta da sala 5
    """
    def __init__(self, x, y, position_mode):
        super().__init__(x, y, position_mode)
        self.closed_door_image = os.path.join(constants.IMAGES_DIR, 'door closed.png')
        self.open_door_image = os.path.join(constants.IMAGES_DIR, 'door.png')
        self.image = pygame.image.load(self.closed_door_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (85, 130))
        self.puzzle_completed = False

    def interaction(self, player):        
        self.print_pop_up()

        in_pop_up = True
        password_input = ''
        password = 'nome'
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
                        if password_input.lower() == password:
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

        h = 0.26*constants.HEIGHT
        w = 0.58*constants.WIDTH
        if self.puzzle_completed and user_returned:
            self.image = pygame.image.load(self.open_door_image).convert_alpha()
            self.image = pygame.transform.scale(self.image, (85, 130))
            constants.SCREEN.blit(self.image, self.rect)
            player.draw_player()
            parameters = {'message': 'A porta se abre', 'wait_time': 1.4,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
            player.passed_room = True
        elif user_returned:
            parameters = {'message': 'Nada ocorre...', 'wait_time': 0.8,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
    
    
    def print_pop_up(self):
        options = {'centralized', 'text_offset'}
        parameters = {'message': 'Porta trancada', 'font_size': 40,
            'width': 0.58*constants.WIDTH, 'height': 0.26*constants.HEIGHT,
            'x_text': 0.29*constants.WIDTH, 'y_text': 0.04*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        options = {}
        parameters = {'message': 'Porta de saída.', 'font_size': 20,
            'width': 0.56*constants.WIDTH, 'height': 0.03*constants.HEIGHT,
            'x_pop_up': 0.5*constants.WIDTH, 'y_pop_up': 0.48*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        options = {}
        parameters = {'message': 'Insira a senha:', 'font_size': 16,
            'width': 0.56*constants.WIDTH, 'height': 0.03*constants.HEIGHT,
            'x_pop_up': 0.5*constants.WIDTH, 'y_pop_up': 0.54*constants.HEIGHT
        }
        Utils().print_message(options, parameters)
        self.print_password('')


    def print_password(self, password_input):
        options = {'colors'}
        parameters = {'message': password_input, 'font_size': 16,
            'width': 0.4*constants.WIDTH, 'height': 0.03*constants.HEIGHT,
            'x_pop_up': 0.5*constants.WIDTH, 'y_pop_up': 0.59*constants.HEIGHT,
            'text_color': constants.BLACK, 'pop_up_color': constants.WHITE
        }
        Utils().print_message(options, parameters)