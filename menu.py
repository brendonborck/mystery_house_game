import pygame
import constants
from utils import Utils

class Menu():
    """Classe que define a criação do menu do jogo"""
    def __init__(self, start_screen_image):
        self.start_screen_image = start_screen_image
        self.running = True
        self.playing = False
        self.font_size = 35


    def draw_options(self, colors):
        Utils().draw_text('Modo 1', self.font_size, colors[0], constants.WIDTH/2, constants.HEIGHT * 0.7)
        Utils().draw_text('Modo 2', self.font_size, colors[1], constants.WIDTH/2, constants.HEIGHT * 0.8)
        Utils().draw_text('Modo 3', self.font_size, colors[2], constants.WIDTH/2, constants.HEIGHT * 0.9)
        pygame.display.flip()

    
    def draw_menu(self):
        n_buttons = 3
        selected_button = 0
        colors = [constants.GRAY, constants.WHITE, constants.WHITE]
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
            speed = 10
        elif selected_button == 1:
            player_image = "player2.png"
            speed = 10
        elif selected_button == 2:
            player_image = "player1.png"
            speed = 20

        options = {}
        options['player_image'] = player_image
        options['speed'] = speed
        return options


    def get_options(self):
        return self.draw_menu()