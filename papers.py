import pygame
import constants
from utils import Utils
import os
from objects import InteractiveObjetcs

class Paper(InteractiveObjetcs):
    """
        Classe que define os parametros básicos dos pergaminhos
    """
    def __init__(self, x, y, position_mode):
        paper_image = constants.PAPER_IMAGE
        self.paper_image_path = os.path.join(constants.IMAGES_DIR, paper_image)
        super().__init__(self.paper_image_path, x, y, position_mode, (45, 55))
        self.impassable = False


    def after_interaction(self):
        pass


    def define_mask(self):
        mask_width = self.width
        mask_height = self.height
        mask = pygame.mask.Mask((mask_width, mask_height), False)
        rect_width = 0.8*mask_width
        rect_height = 0.8*mask_height
        position = ((mask_width - rect_width)/2, (mask_height - rect_height)/2)
        rect = pygame.mask.Mask((rect_width, rect_height), True)
        mask.draw(rect, position)
        return mask


class Paper1(Paper):
    """
        Classe que define o pergaminho da sala 1
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

        message1 = "Bem vindo a Mistery House!"
        message2 = "Você não se lembra como veio parar aqui, mas não se preocupe, tudo será explicado no tempo"
        message3 = "certo. A única coisa que posso te dizer nesse momento é "
        message4 = "que voce merece tudo que vai ocorrer com voçe."

        options = {'centralized', 'text_offset'}
        parameters = {'message': message1, 'font_size': 16,
            'width': width, 'height': 0.24*constants.HEIGHT,
            'x_text': 0.5*width, 'y_text': 0.2*0.24*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        options = {}
        parameters = {'message': message2, 'font_size': 16,
            'width': width, 'height': 0.06*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.48*constants.HEIGHT
        }
        Utils().print_message(options, parameters)
        
        parameters = {'message': message3, 'font_size': 16,
            'width': width, 'height': 0.06*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.52*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        parameters = {'message': message4, 'font_size': 16,
            'width': width, 'height': 0.06*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.56*constants.HEIGHT
        }
        Utils().print_message(options, parameters)


class Paper2(Paper):
    """
        Classe que define o pergaminho da sala 2
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

        message1 = "Laurent, meu irmão amado, é inaceitável as ações do caçula, ele acha que pode"
        message2 = "assaltar nossa familia! Nosso amado pai é contra, mas o TEMPO dele...."
        message3 = "O resto da mensagem parece destruída "

        options = {}
        parameters = {'message': message1, 'font_size': 16,
            'width': width, 'height': 0.06*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.48*constants.HEIGHT
        }
        Utils().print_message(options, parameters)
        
        parameters = {'message': message2, 'font_size': 16,
            'width': width, 'height': 0.06*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.52*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        parameters = {'message': message3, 'font_size': 16,
            'width': width, 'height': 0.06*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.56*constants.HEIGHT
        }
        Utils().print_message(options, parameters)


class Paper3(Paper):
    """
        Classe que define o pergaminho da sala 3
    """
    def __init__(self, x, y, position_mode):
        super().__init__(x, y, position_mode)
        paper_image = constants.PAPER_IMAGE_2
        self.paper_image_path = os.path.join(constants.IMAGES_DIR, paper_image)
        self.image = pygame.image.load(self.paper_image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (45, 55))
        self.puzzle_completed = False


    def interaction(self, player):
        h = 0.23*constants.HEIGHT
        w = 0.5*constants.WIDTH
        if self.puzzle_completed:
            w = 0.56*constants.WIDTH
            parameters = {'message': 'Papel amassado.', 'wait_time': 1.4,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
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
                            self.puzzle_completed = True
                            player.pocket.append('key_room_return_2')
                            player.stop_acting()


    def print_pop_up(self):
        width = 0.9*constants.WIDTH
        x_pop_up = 0.5*constants.WIDTH

        message1 = "Há uma manchete de jornal, 'O REI ESTÁ MORTO! O mais novo é o suspeito!?'"
        message2 = "Você ganhou a chave número 2."

        options = {'centralized', 'text_offset'}
        parameters = {'message': message1, 'font_size': 18,
            'width': width, 'height': 0.18*constants.HEIGHT,
            'x_text': 0.5*width, 'y_text': 0.2*0.24*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        options = {}
        parameters = {'message': message2, 'font_size': 20,
            'width': width, 'height': 0.06*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.52*constants.HEIGHT
        }
        Utils().print_message(options, parameters)


class Paper3_2(Paper):
    """
        Classe que define o pergaminho da sala 1
    """
    def interaction(self, player):
        self.print_pop_up()
        player.stop_acting()


    def print_pop_up(self):
            h = 0.23*constants.HEIGHT
            w = 0.5*constants.WIDTH
            parameters = {'message': 'Papel amassado.', 'wait_time': 1.2,
                'font_size': 40, 'width': w, 'height': h
            }
            Utils().print_message({'centralized', 'persistent'}, parameters)
            

class Paper4(Paper):
    """
        Classe que define o pergaminho da sala 4
    """
    def __init__(self, x, y, position_mode):
        super().__init__(x, y, position_mode)
        paper_image = constants.PAPER_IMAGE_2
        self.paper_image_path = os.path.join(constants.IMAGES_DIR, paper_image)
        self.image = pygame.image.load(self.paper_image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (45, 55))
        self.puzzle_completed = False

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

        message1 = "Estou impressionado que você tenha chegado até esse ponto..."
        message2 = "Por isso eu vou te da uma recompensa, você está aqui pois realizou "
        message3 = "um ato muito ruim contra a nossa família..."

        options = {}
        parameters = {'message': message1, 'font_size': 16,
            'width': width, 'height': 0.06*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.48*constants.HEIGHT
        }
        Utils().print_message(options, parameters)
        
        parameters = {'message': message2, 'font_size': 16,
            'width': width, 'height': 0.06*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.52*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        parameters = {'message': message3, 'font_size': 16,
            'width': width, 'height': 0.06*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.56*constants.HEIGHT
        }
        Utils().print_message(options, parameters)


class Paper5(Paper):
    """
        Classe que define o pergaminho da sala 5
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

        message1 = "Estou impressionado que tenha chegado até aqui, você deve ter entendido toda a situação "
        message2 = "e o porquê está nesse local. O último desafio é simples, "
        message3 = "você deve me informar seu nome. Muito fácil né ?"

        options = {}
        parameters = {'message': message1, 'font_size': 16,
            'width': width, 'height': 0.06*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.48*constants.HEIGHT
        }
        Utils().print_message(options, parameters)
        
        parameters = {'message': message2, 'font_size': 16,
            'width': width, 'height': 0.06*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.52*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        parameters = {'message': message3, 'font_size': 16,
            'width': width, 'height': 0.06*constants.HEIGHT,
            'x_pop_up': x_pop_up, 'y_pop_up': 0.56*constants.HEIGHT
        }
        Utils().print_message(options, parameters)