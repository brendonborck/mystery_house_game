from turtle import position
import pygame
import constants
import os
from utils import Utils
from doors import Door1, Door2
from paintings import Painting1
from papers import Paper1, Paper2

class Room(pygame.sprite.Sprite):

    def __init__(self, name, print_time, player_position):
        super().__init__()
        room_image_path = os.path.join(constants.IMAGES_DIR, constants.ROOM_IMAGE)
        self.image = pygame.image.load(room_image_path).convert()
        self.image = pygame.transform.scale(self.image, (constants.WIDTH, constants.HEIGHT))
        self.rect = self.image.get_rect()
        self.interactive_objects_group = pygame.sprite.Group()
        self.name = name
        self.print_time = print_time
        self.player_position = player_position


    def define_interactive_objects(self, interactive_objects):
        for object_name in interactive_objects:
            Constructor = interactive_objects[object_name]['constructor']
            parameters = interactive_objects[object_name]['parameters']
            x = parameters['x']
            y = parameters['y']
            position_mode = parameters['position_mode']
            obj = Constructor(x, y, position_mode)
            self.interactive_objects_group.add(obj)

    
    def print_room_message(self):
        parameters = {'message': self.name, 'wait_time': self.print_time}
        Utils().print_message({'full', 'centralized', 'persistent'}, parameters)


def create_rooms():
    rooms = []

    name = 'Fase 1'
    print_time = 1.2
    player_pos = (int(0.012*constants.WIDTH)*10, int(0.088*constants.HEIGHT)*10)
    painting_x = 0.15*constants.WIDTH
    painting_y = 0.36*constants.Y_SUPERIOR_WALL
    exit_door_x = 0.75*constants.WIDTH
    exit_door_y = constants.Y_SUPERIOR_WALL
    paper_x = 0.25*constants.WIDTH
    paper_y = 0.8*constants.HEIGHT
    interactive_objects = {
        'painting': {'constructor': Painting1,'parameters':
            {'x': painting_x, 'y': painting_y, 'position_mode': 'center'}},
        'exit_door': {'constructor': Door1, 'parameters':
            {'x': exit_door_x, 'y': exit_door_y, 'position_mode': 'bottomleft'}},
        'paper': {'constructor': Paper1, 'parameters':
            {'x': paper_x, 'y': paper_y, 'position_mode': 'center'}}
    }
    room = Room(name, print_time, player_pos)
    room.define_interactive_objects(interactive_objects)
    rooms.append(room)

    name = 'Fase 2'
    print_time = 1.7
    player_pos = (int(0.018*constants.WIDTH)*10, int(constants.Y_SUPERIOR_WALL/10)*10)
    exit_door_x = 0.12*constants.WIDTH
    exit_door_y = constants.Y_SUPERIOR_WALL
    paper_x = 0.8*constants.WIDTH
    paper_y = 0.4*constants.HEIGHT
    interactive_objects = {
        'exit_door': {'constructor': Door2, 'parameters': {'x': exit_door_x, 'y': exit_door_y, 'position_mode': 'bottomleft'}},
        'paper': {'constructor': Paper2, 'parameters': {'x': paper_x, 'y': paper_y, 'position_mode': 'center'}}
    }
    room = Room(name, print_time, player_pos)
    room.define_interactive_objects(interactive_objects)
    rooms.append(room)

    return rooms
    
rooms = create_rooms()