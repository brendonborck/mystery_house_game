import pygame
import constants
import os
from utils import Utils

class Menu():
    """
        Classe que define a criação do menu do jogo
    """
    def __init__(self, start_screen_image):
        self.start_screen_image = start_screen_image
        self.start_screen_rect = self.start_screen_image.get_rect()
        self.start_screen_rect.midtop = (constants.WIDTH/2, 0)
        self.running = True
        self.playing = False
        self.font_size = 35


    def draw_options(self, colors):
        Utils().draw_text('Jogar com emoção', self.font_size, colors[0], constants.WIDTH/2, constants.HEIGHT * 0.7)
        Utils().draw_text('Jogar sem emoção', self.font_size, colors[1], constants.WIDTH/2, constants.HEIGHT * 0.8)
        Utils().draw_text('Teclas do jogo', self.font_size, colors[2], constants.WIDTH/2, constants.HEIGHT * 0.9)
        pygame.display.flip()

    
    def draw_menu(self):
        n_buttons = 3
        selected_button = 0
        colors = [constants.GRAY, constants.WHITE, constants.WHITE]
        constants.SCREEN.blit(self.start_screen_image, self.start_screen_rect)
        self.draw_options(colors)

        in_menu=True
        while in_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    in_menu = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        in_menu = False
                        options = self.game_options(selected_button)
                        return options
                    elif event.key == pygame.K_ESCAPE: 
                        in_menu = False
                        self.running = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP and selected_button > 0:
                        selected_button -= 1
                    if event.key == pygame.K_DOWN and selected_button < n_buttons - 1:
                        selected_button += 1
                    if event.key in (pygame.K_UP, pygame.K_DOWN):
                        colors = [constants.WHITE] * n_buttons
                        colors[selected_button] = constants.GRAY
                        screen_rect = self.start_screen_image.get_rect()
                        screen_rect.midtop = (constants.WIDTH/2,0)
                        constants.SCREEN.blit(self.start_screen_image, screen_rect)
                        self.draw_options(colors)
                        pygame.display.update()

    
    def game_options(self, selected_button):
        if selected_button == 0:
            player_image = "player1.png"
            speed = 5
            countdown = True
        elif selected_button == 1:
            player_image = "player1.png"
            speed = 5
            countdown = False
        elif selected_button == 2:
            self.game_keys()
            options = self.get_options()
            if options:
                player_image = options['player_image']
                speed = options['speed']
                countdown = options['countdown']    

        options = {}
        try:
            options['player_image'] = player_image
            options['speed'] = speed
            options['countdown'] = countdown
        except:
            pass
        return options

    def game_keys(self):
        image = pygame.Surface([constants.WIDTH, constants.HEIGHT])
        image.fill(constants.BLACK)

        rect = image.get_rect()
        rect.topleft = (0, 0)
        in_pop_up = True
        constants.SCREEN.blit(image, rect)

        message = 'Movimentar jogador'
        options = {}
        parameters = {'message': message, 'font_size': 20,
            'width': 0.72*constants.WIDTH, 'height': 0.1*constants.HEIGHT,
            'x_pop_up': 0.72*constants.WIDTH, 'y_pop_up': 0.29*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        x = constants.WIDTH*0.3
        y = constants.HEIGHT*0.29
        image = os.path.join(constants.IMAGES_DIR, 'wasd.png')
        image = pygame.image.load(image)
        image = pygame.transform.scale(image, (280, 180))
        rect = image.get_rect()
        rect.center = (x, y)
        constants.SCREEN.blit(image, rect)

        message = 'Interagir'
        parameters = {'message': message, 'font_size': 20,
            'width': 0.72*constants.WIDTH, 'height': 0.1*constants.HEIGHT,
            'x_pop_up': 0.72*constants.WIDTH, 'y_pop_up': 0.56*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        x = constants.WIDTH*0.29
        y = constants.HEIGHT*0.56
        image = os.path.join(constants.IMAGES_DIR, 'letter_e.png')
        image = pygame.image.load(image)
        image = pygame.transform.scale(image, (80, 80))
        rect = image.get_rect()
        rect.center = (x, y)
        constants.SCREEN.blit(image, rect)


        message = 'Sair da interação/Sair do jogo'
        parameters = {'message': message, 'font_size': 20,
            'width': 0.72*constants.WIDTH, 'height': 0.1*constants.HEIGHT,
            'x_pop_up': 0.72*constants.WIDTH, 'y_pop_up': 0.75*constants.HEIGHT
        }
        Utils().print_message(options, parameters)

        x = constants.WIDTH*0.29
        y = constants.HEIGHT*0.75
        image = os.path.join(constants.IMAGES_DIR, 'esc_key.png')
        image = pygame.image.load(image)
        image = pygame.transform.scale(image, (80, 80))
        rect = image.get_rect()
        rect.center = (x, y)
        constants.SCREEN.blit(image, rect)

        pygame.display.update()
        while in_pop_up:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.playing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        in_pop_up = False
                    elif event.key == pygame.K_ESCAPE:
                        in_pop_up = False

    def get_options(self):
        return self.draw_menu()