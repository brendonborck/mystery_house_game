import pygame
import constants
from utils import Utils

class Menu():
    def __init__(self, screen, start_screen_image):
        self.screen = screen
        self.start_screen_image = start_screen_image
        self.running = True
        self.playing = False
        self.font_size = 35
        self.player_image = None
        self.speed = None


    def draw_options(self, colors):
        Utils().draw_text(self.screen, 'Modo 1', self.font_size, colors[0], constants.WIDTH/2, constants.HEIGHT * 0.7)
        Utils().draw_text(self.screen, 'Modo 2', self.font_size, colors[1], constants.WIDTH/2, constants.HEIGHT * 0.8)
        Utils().draw_text(self.screen, 'Modo 3', self.font_size, colors[2], constants.WIDTH/2, constants.HEIGHT * 0.9)
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
                        self.game_options(selected_button)
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
                        self.screen.blit(self.start_screen_image, screen_rect)
                        self.draw_options(colors)
                        pygame.display.update()

    
    def game_options(self, selected_button):
        if selected_button == 0:
            self.player_image = "player1.png"
            self.speed = 10
        elif selected_button == 1:
            self.player_image = "player2.png"
            self.speed = 10
        elif selected_button == 2:
            self.player_image = "player1.png"
            self.speed = 20
