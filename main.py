from json import load
import pygame
import constants
from menu import Menu
from player import Player
from utils import Utils
from room import create_rooms
import os


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        constants.SCREEN = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        pygame.display.set_caption(constants.TITLE)
        self.running = True
        self.playing = False
        self.pressed_keys = {'a': False, 's': False, 'd': False, 'w': False}
        self.options = {}


    def run_game(self):
        self.playing = True

        player_image = self.options['player_image']
        player_speed = self.options['speed']
        constants.countdown = self.options['countdown']
        player = Player(player_image, player_speed)
        self.run_music()
        self.run_rooms(player)


    def run_rooms(self, player):
        room_group = pygame.sprite.GroupSingle()
        created_rooms = create_rooms()
        rooms = created_rooms['rooms']
        obj_rects_list = created_rooms['obj_rects_list']
        if self.playing:
            constants.clock = pygame.time.Clock()
        for i in range(len(rooms)):
            room = rooms[i]
            obj_rects = obj_rects_list[i]
            if self.playing:
                room_group.add(room)
                room.print_room_message()
                pygame.display.update()
                player.x = room.player_position[0]
                player.y = room.player_position[1]
            while self.playing:
                if constants.countdown:
                    seconds_passed = constants.clock.get_time()/1000
                    constants.time_left -= seconds_passed
                if constants.time_left <= 0:
                    self.you_lost()
                    self.running = False
                    self.playing = False
                    break
                constants.clock.tick(constants.FPS)
                self.watch_events(player)
                room_group.draw(constants.SCREEN)
                room.interactive_objects_group.draw(constants.SCREEN)
                player.move_player(obj_rects)
                player.draw_player()
                self.print_pocket(player)
                if constants.countdown:
                    Utils().print_time()
                interacted = player.check_interaction(room.interactive_objects_group)
                if interacted:
                    for key in self.pressed_keys:
                        self.pressed_keys[key] = False
                    player.direction = 0
                pygame.display.update()
                if player.passed_room:
                    player.passed_room = False
                    break


    def print_pocket(self, player):
        x = 30
        y = 30
        image = os.path.join(constants.IMAGES_DIR, 'key.png')
        image = pygame.image.load(image).convert_alpha()
        image = pygame.transform.scale(image, (40, 40))
        rect = image.get_rect()
        for key in player.pocket:
            rect.center = (x, y)
            constants.SCREEN.blit(image, rect)
            x += 40


    def watch_events(self, player):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_a, pygame.K_w, pygame.K_d, pygame.K_s):
                    player.direction = event.unicode.lower()
                    self.pressed_keys[event.unicode.lower()] = True
                elif event.key == pygame.K_e:
                    player.act()
                elif event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.running = False
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_a, pygame.K_w, pygame.K_d, pygame.K_s):
                    player.direction = 0
                    self.pressed_keys[event.unicode.lower()] = False
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
        constants.SCREEN.blit(start_screen_image, start_screen_rect)

        menu = Menu(start_screen_image)
        pygame.display.flip()
        self.options = menu.get_options()
        self.running = menu.running
	
    def run_music(self):
        start_music_path = os.path.join(constants.MUSIC_DIR, constants.MUSIC_GAME)
        pygame.mixer.music.load(start_music_path) 
        pygame.mixer.music.set_volume(1.0)   
        pygame.mixer.music.play()
        
    def end_game(self):
        constants.clock.tick(constants.FPS)
        parameters = {'message': 'Você venceu!'}
        Utils().print_message({'full', 'centralized'}, parameters)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False


    def you_lost(self):
        parameters = {'message': 'Você perdeu!'}
        Utils().print_message({'full', 'centralized'}, parameters)
        in_pop_up = True
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


if __name__ == '__main__':
    game = Game()
    game.draw_start_screen()
    if game.running:
        game.run_game()

    while game.running:
        game.end_game()