import pygame
import constants
from menu import Menu
from player import Player
from objects import Door, Painting, Paper
from utils import Text
import os
from abc import abstractmethod

class Game:
    def __init__(self):
        #Criando a Tela do Jogo
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((constants.WIDTH,constants.HEIGHT))
        self.player_image = None
        pygame.display.set_caption(constants.TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False
        self.pressed_keys = {'a': False, 's': False, 'd': False, 'w': False}
        self.speed = 0


    def new_game(self):
        #instancia as classes
        self.run_level_1()
        #self.run_level_2()


    def run_level_1(self):
        #loop do jogo
        self.playing = True
        room = Room()
        player = Player(self.player_image, self.speed)
        
        painting_x = 0.15*constants.WIDTH
        painting_y = 0.36*constants.Y_SUPERIOR_WALL
        painting = Painting(self.screen, self.clock, painting_x, painting_y, 'center')
        
        exit_door_x = 0.75*constants.WIDTH
        exit_door_y = constants.Y_SUPERIOR_WALL
        exit_door = Door(self.screen, self.clock, exit_door_x, exit_door_y, 'bottomleft')
        
        paper_x = 0.25*constants.WIDTH
        paper_y = 0.8*constants.HEIGHT
        paper = Paper(self.screen, self.clock, paper_x, paper_y, 'center')
        
        interactive_objects_group = pygame.sprite.Group()
        room_group = pygame.sprite.GroupSingle()
        interactive_objects_group.add(exit_door, painting, paper)
        room_group.add(room)
        while self.playing:
            self.clock.tick(constants.FPS)
            self.events(player)
            room_group.draw(self.screen)
            interactive_objects_group.draw(self.screen)
            player.move_player()
            player.draw_player(self.screen)
            interacted = player.check_interaction(interactive_objects_group)
            if interacted:
                for key in self.pressed_keys:
                    self.pressed_keys[key] = False
                player.direction = 0
            pygame.display.update()
            if player.passed_room:
                self.playing = False

    def events(self, player):
        #Define os events do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_a, pygame.K_w, pygame.K_d, pygame.K_s):
                    player.direction = event.unicode
                    self.pressed_keys[event.unicode] = True
                elif event.key == pygame.K_e:
                    player.act()
                elif event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.running = False
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_a, pygame.K_w, pygame.K_d, pygame.K_s):
                    player.direction = 0
                    self.pressed_keys[event.unicode] = False
                elif event.key == pygame.K_e:
                    player.stop_acting()
                for key in ('a','w','s','d'):
                    if self.pressed_keys[key]:
                        player.direction = key     


    def draw_start_screen(self):
        start_screen_path = os.path.join(constants.IMAGES_DIR, constants.START_IMAGE)
        start_screen_image = pygame.image.load(start_screen_path).convert()
        start_screen_image = pygame.transform.scale(start_screen_image, (1000, 800))
        start_screen_rect = start_screen_image.get_rect()
        start_screen_rect.midtop = (constants.WIDTH/2,0)
        self.screen.blit(start_screen_image, start_screen_rect)

        menu = Menu(self.screen, start_screen_image)
        pygame.display.flip()
        menu.draw_menu()
        self.running = menu.running
        self.player_image = menu.player_image
        self.speed = menu.speed
	
                    
    def game_ended(self):
        self.clock.tick(constants.FPS)
        x_pop_up = constants.WIDTH/2
        y_pop_up = constants.HEIGHT/2
        font_size = 60
        message = 'Você venceu!'
        color = constants.WHITE
        width = constants.WIDTH
        height = constants.HEIGHT
        x_text = 0.5*width
        y_text = 0.5*height
        text_group = pygame.sprite.Group()
        text = Text(message, font_size, x_pop_up, y_pop_up, x_text, y_text, width, height, color)
        text_group.add(text)

        text_group.draw(self.screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False


class Room(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        room_image_path = os.path.join(constants.IMAGES_DIR, constants.ROOM_IMAGE)
        self.image = pygame.image.load(room_image_path).convert()
        self.image = pygame.transform.scale(self.image, (constants.WIDTH, constants.HEIGHT))
        self.rect = self.image.get_rect()


if __name__ == '__main__':
    g = Game()
    g.draw_start_screen()
    g.new_game()

    while g.running:
        g.game_ended()