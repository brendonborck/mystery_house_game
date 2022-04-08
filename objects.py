import pygame
import constants
from utils import Text, Utils
import os
import time
from abc import abstractmethod

class InteractiveObjetcs(pygame.sprite.Sprite):
    
    def __init__(self, screen, clock, image_path, x, y, position_mode, scale = None):
        super().__init__()
        self.screen = screen
        self.clock = clock
        self.image = pygame.image.load(image_path).convert_alpha()
        if scale:
            self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        if position_mode == 'center':
            self.rect.center = (x, y)
        elif position_mode == 'bottomleft':
            self.rect.bottomleft = (x, y)
        self.width = self.rect.width
        self.height = self.rect.height
        self.mask = self.define_mask()
        

    @abstractmethod
    def interaction(self):
        pass
    
    
    @abstractmethod
    def after_interaction(self):
        pass

    
    @abstractmethod
    def define_mask(self):
        pass


class Door(InteractiveObjetcs):
    
    def __init__(self, screen, clock, x, y, position_mode):
        self.closed_door_image = os.path.join(constants.IMAGES_DIR, 'closed_door.png')
        self.open_door_image = os.path.join(constants.IMAGES_DIR, 'open_door.png')
        super().__init__(screen, clock, self.closed_door_image, x, y, position_mode)
        self.puzzle_completed = False

    
    def interaction(self, player):        
        self.print_pop_up()

        in_pop_up = True
        password_input = ''
        password = 'senha'
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

        if self.puzzle_completed:
            self.image = pygame.image.load(self.open_door_image).convert_alpha()
            self.screen.blit(self.image, self.rect)
            player.draw_player(self.screen)
            self.print_message('Senha correta!', 1.4)
            player.passed_room = True
        else:
            self.print_message('Senha incorreta', 0.8)


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


    def print_pop_up(self):
        x_pop_up = constants.WIDTH/2
        y_pop_up1 = constants.HEIGHT/2
        y_pop_up2 = 0.51*constants.HEIGHT
        message1 = 'Porta trancada'
        message2 = 'Insira a senha:'
        font_size1 = 40
        font_size2 = 20
        color = constants.WHITE
        width = 0.5*constants.WIDTH
        height1 = 0.23*constants.HEIGHT
        height2 = 0.03*constants.HEIGHT
        x_text = width/2
        y_text1 = 0.26*height1
        y_text2 = 0.5*height2
        text_group = pygame.sprite.Group()
        text1 = Text(message1, font_size1, x_pop_up, y_pop_up1, x_text, y_text1, width, height1, color)
        text2 = Text(message2, font_size2, x_pop_up, y_pop_up2, x_text, y_text2, width, height2, color)
        text_group.add(text1, text2)

        text_group.draw(self.screen)
        pygame.display.update()
        self.print_password('')


    def print_password(self, password_input):
        x_pop_up = constants.WIDTH/2
        y_pop_up = 0.57*constants.HEIGHT
        message = password_input
        font_size = 16
        color = constants.BLACK
        width = 0.4*constants.WIDTH
        height = 0.03*constants.HEIGHT
        x_text = 0.5*width
        y_text = 0.5*height
        text_group = pygame.sprite.Group()
        text = Text(message, font_size, x_pop_up, y_pop_up, x_text, y_text, width, height, color, constants.WHITE)
        text_group.add(text)

        text_group.draw(self.screen)
        pygame.display.update()


    def print_message(self, message, wait_time):
        x_pop_up = constants.WIDTH/2
        y_pop_up = constants.HEIGHT/2
        font_size = 40
        color = constants.WHITE
        width = 0.5*constants.WIDTH
        height = 0.2*constants.HEIGHT
        x_text = 0.5*width
        y_text = 0.5*height
        text_group = pygame.sprite.Group()
        text = Text(message, font_size, x_pop_up, y_pop_up, x_text, y_text, width, height, color)
        text_group.add(text)

        text_group.draw(self.screen)
        pygame.display.update()
        time.sleep(wait_time)
        for event in pygame.event.get():
            pass


class Painting(InteractiveObjetcs):
    
    def __init__(self, screen, clock, x, y, position_mode):
        self.painting_image = os.path.join(constants.IMAGES_DIR, 'painting.png')
        super().__init__(screen, clock, self.painting_image, x, y, position_mode, (69, 74))

    
    def interaction(self, player):
        x_pop_up, y_pop_up = (constants.WIDTH/2, constants.HEIGHT/2)
        message = 'Senha: 01110011 01100101 01101110 01101000 01100001'
        font_size = 20
        color = constants.WHITE
        width = 0.72*constants.WIDTH
        height = 0.1*constants.HEIGHT
        x_text = width/2
        y_text = height/2
        text = Text(message, font_size, x_pop_up, y_pop_up, x_text, y_text, width, height, color)
        text_group = pygame.sprite.Group()
        text_group.add(text)
        text_group.draw(self.screen)
        pygame.display.update()
        
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


class Paper(InteractiveObjetcs):

    def __init__(self, screen, clock, x, y, position_mode):
        self.paper_image_path = os.path.join(constants.IMAGES_DIR, 'paper.png')
        super().__init__(screen, clock, self.paper_image_path, x, y, position_mode, (45, 55))


    def interaction(self, player):
        x_pop_up, y_pop_up = (constants.WIDTH/2, constants.HEIGHT/2)
        width = 0.87*constants.WIDTH
        height = 0.24*constants.HEIGHT
        image = pygame.Surface([width, height])
        image.fill(constants.BLACK)
        rect = image.get_rect()
        rect.center = (x_pop_up ,y_pop_up)
        self.screen.blit(image, rect)

        font_size = 16
        color = constants.WHITE
        x_text = x_pop_up
        y_text1 = 0.44*constants.HEIGHT
        y_text2 = 0.48*constants.HEIGHT
        y_text3 = 0.52*constants.HEIGHT
        y_text4 = 0.56*constants.HEIGHT
        message1 = "Bem vindo a Mistery House!"
        message2 = "Você não se lembra como veio parar aqui, mas não se preocupe, tudo será explicado no tempo"
        message3 = "certo. A única coisa que posso te dizer nesse momento é que, por muitas vezes, a vida"
        message4 = "parece ser apenas preto no branco, mas, na verdade, ela não é. Tudo não é sempre 0 ou 1."
        Utils().draw_text(self.screen, message1, font_size, color, x_text, y_text1)
        Utils().draw_text(self.screen, message2, font_size, color, x_text, y_text2)
        Utils().draw_text(self.screen, message3, font_size, color, x_text, y_text3)
        Utils().draw_text(self.screen, message4, font_size, color, x_text, y_text4)


        pygame.display.update()

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


    def after_interaction(self):
        pass


    def define_mask(self):
        mask_width = self.width
        mask_height = self.height
        mask = pygame.mask.Mask((mask_width, mask_height), False)
        rect_width = 0.8*mask_width
        rect_height = 0.8*mask_height
        position = ((mask_width - rect_width)/2, (mask_height - rect_width)/2)
        rect = pygame.mask.Mask((rect_width, rect_height), True)
        mask.draw(rect, position)
        return mask        

