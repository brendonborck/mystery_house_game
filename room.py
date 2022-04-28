from turtle import position
import pygame
from bed import Bed1, Bed2, Bed3, Bed4
from clock import Clock1, Clock2
import constants
import os
from utils import Utils
from doors import Door1, Door2
from paintings import Painting1
from papers import Paper1, Paper2, Paper3, Paper4, Paper5
from wardrobe import Wardrobe1
from writingdesk import Writing_Desk1, Writing_Desk2


class Room(pygame.sprite.Sprite):

    def __init__(self, name, print_time, player_position, level):
        super().__init__()
        
        room_image = constants.ROOM_IMAGE
        if level == 2:
            room_image = constants.ROOM_IMAGE_2
        elif level == 3:
            room_image = constants.ROOM_IMAGE_3
        else:        
            room_image = constants.ROOM_IMAGE_4

        room_image_path = os.path.join(constants.IMAGES_DIR, room_image)
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
    wdesk_x = 0.95*constants.WIDTH
    wdesk_y = 0.50*constants.HEIGHT
    bed_x = 0.80*constants.WIDTH
    bed_y = 0.90*constants.HEIGHT
    clock_x = 0.30*constants.WIDTH
    clock_y = 0.36*constants.Y_SUPERIOR_WALL
    painting_x = 0.15*constants.WIDTH
    painting_y = 0.36*constants.Y_SUPERIOR_WALL
    exit_door_x = 0.75*constants.WIDTH
    exit_door_y = constants.Y_SUPERIOR_WALL
    paper_x = 0.25*constants.WIDTH
    paper_y = 0.8*constants.HEIGHT
    interactive_objects = {
        'writingdesk': {'constructor': Writing_Desk1,'parameters':
            {'x': wdesk_x, 'y': wdesk_y, 'position_mode': 'center'}},
        'painting': {'constructor': Painting1,'parameters':
            {'x': painting_x, 'y': painting_y, 'position_mode': 'center'}},
        'bed': {'constructor': Bed1,'parameters':
            {'x': bed_x, 'y': bed_y, 'position_mode': 'center'}},
        'clock': {'constructor': Clock1,'parameters':
            {'x': clock_x, 'y': clock_y, 'position_mode': 'center'}},
        'exit_door': {'constructor': Door1, 'parameters':
            {'x': exit_door_x, 'y': exit_door_y, 'position_mode': 'bottomleft'}},
        'paper': {'constructor': Paper1, 'parameters':
            {'x': paper_x, 'y': paper_y, 'position_mode': 'center', 'type': 1}}
    }
    room = Room(name, print_time, player_pos, 1)
    room.define_interactive_objects(interactive_objects)
    rooms.append(room)

    name = 'Fase 2'
    print_time = 1.7
    player_pos = (int(0.018*constants.WIDTH)*10, int(constants.Y_SUPERIOR_WALL/10)*10)
    exit_door_x = 0.12*constants.WIDTH
    exit_door_y = constants.Y_SUPERIOR_WALL
    paper_x = 0.8*constants.WIDTH
    paper_y = 0.4*constants.HEIGHT
    wdesk_x = 0.95*constants.WIDTH
    wdesk_y = 0.50*constants.HEIGHT
    wdrobe_x = 0.70*constants.WIDTH
    wdrobe_y = 0.20*constants.HEIGHT
    clock_x = 0.30*constants.WIDTH
    clock_y = 0.36*constants.Y_SUPERIOR_WALL
    bed_x = 0.80*constants.WIDTH
    bed_y = 0.90*constants.HEIGHT
    interactive_objects = {
        'exit_door': {
            'constructor': Door2,
            'parameters': {
                'x': exit_door_x,
                'y': exit_door_y,
                'position_mode': 'bottomleft'
            }
        },
        'writingdesk': 
         {'constructor': Writing_Desk2,
         'parameters':{
             'x': wdesk_x, 
             'y': wdesk_y, 
             'position_mode': 'center'}},

        'wardrobe': 
         {'constructor': Wardrobe1,
         'parameters':{
             'x': wdrobe_x, 
             'y': wdrobe_y, 
             'position_mode': 'center'}},

        'bed': {'constructor': Bed2,
        'parameters':
            {'x': bed_x, 
             'y': bed_y, 
            'position_mode': 'center'}},

        'clock': {'constructor': Clock2,
        'parameters':
            {'x': clock_x, 
            'y': clock_y, 
            'position_mode': 'center'}},

        'paper': {
            'constructor': Paper2,
            'parameters': {
                'x': paper_x,
                'y': paper_y,
                'position_mode': 'center',
                'type': 1
            }
        }
    }
    room = Room(name, print_time, player_pos, 2)
    room.define_interactive_objects(interactive_objects)
    rooms.append(room)


    name = 'Fase 3'
    print_time = 1.7
    player_pos = (int(0.018*constants.WIDTH)*10, int(constants.Y_SUPERIOR_WALL/10)*10)
    exit_door_x = 0.12*constants.WIDTH
    exit_door_y = constants.Y_SUPERIOR_WALL
    paper_x = 0.8*constants.WIDTH
    paper_y = 0.4*constants.HEIGHT
    wdesk_x = 0.95*constants.WIDTH
    wdesk_y = 0.50*constants.HEIGHT
    wdrobe_x = 0.70*constants.WIDTH
    wdrobe_y = 0.20*constants.HEIGHT
    clock_x = 0.30*constants.WIDTH
    clock_y = 0.36*constants.Y_SUPERIOR_WALL
    bed_x = 0.80*constants.WIDTH
    bed_y = 0.90*constants.HEIGHT
    interactive_objects = {
        'exit_door': {
            'constructor': Door3,
            'parameters': {
                'x': exit_door_x,
                'y': exit_door_y,
                'position_mode': 'bottomleft'
            }
        },

        'wardrobe': 
         {'constructor': Wardrobe3,
         'parameters':{
             'x': wdrobe_x, 
             'y': wdrobe_y, 
             'position_mode': 'center'}},

        'bed': {'constructor': Bed3,
        'parameters':
            {'x': bed_x, 
             'y': bed_y, 
            'position_mode': 'center'}},

        'paper': {
            'constructor': Paper3,
            'parameters': {
                'x': paper_x,
                'y': paper_y,
                'position_mode': 'center',
                'type': 2
            }
        }
    }
    room = Room(name, print_time, player_pos, 3)
    room.define_interactive_objects(interactive_objects)
    rooms.append(room)


    name = 'Fase 4'
    print_time = 1.7
    player_pos = (int(0.018*constants.WIDTH)*10, int(constants.Y_SUPERIOR_WALL/10)*10)
    exit_door_x = 0.12*constants.WIDTH
    exit_door_y = constants.Y_SUPERIOR_WALL
    paper_x = 0.8*constants.WIDTH
    paper_y = 0.4*constants.HEIGHT
    wdesk_x = 0.95*constants.WIDTH
    wdesk_y = 0.50*constants.HEIGHT
    wdrobe_x = 0.70*constants.WIDTH
    wdrobe_y = 0.20*constants.HEIGHT
    clock_x = 0.30*constants.WIDTH
    clock_y = 0.36*constants.Y_SUPERIOR_WALL
    bed_x = 0.80*constants.WIDTH
    bed_y = 0.90*constants.HEIGHT
    interactive_objects = {
        'exit_door': {
            'constructor': Door2,
            'parameters': {
                'x': exit_door_x,
                'y': exit_door_y,
                'position_mode': 'bottomleft'
            }
        },
        'writingdesk': 
         {'constructor': Writing_Desk2,
         'parameters':{
             'x': wdesk_x, 
             'y': wdesk_y, 
             'position_mode': 'center'}},

        'wardrobe': 
         {'constructor': Wardrobe1,
         'parameters':{
             'x': wdrobe_x, 
             'y': wdrobe_y, 
             'position_mode': 'center'}},

        'bed': {'constructor': Bed4,
        'parameters':
            {'x': bed_x, 
             'y': bed_y, 
            'position_mode': 'center'}},

        'clock': {'constructor': Clock2,
        'parameters':
            {'x': clock_x, 
            'y': clock_y, 
            'position_mode': 'center'}},

        'paper': {
            'constructor': Paper4,
            'parameters': {
                'x': paper_x,
                'y': paper_y,
                'position_mode': 'center',
                'type': 1
            }
        }
    }
    room = Room(name, print_time, player_pos, 4)
    room.define_interactive_objects(interactive_objects)
    rooms.append(room)



    name = 'Fase 5'
    print_time = 1.2
    player_pos = (int(0.012*constants.WIDTH)*10, int(0.088*constants.HEIGHT)*10)
    paper_x = 0.25*constants.WIDTH
    paper_y = 0.8*constants.HEIGHT
    interactive_objects = {
        'paper': {
            'constructor': Paper5,
            'parameters': {
                'x': paper_x,
                'y': paper_y,
                'position_mode': 'center',
                'type': 2
            }
        }
    }
    room = Room(name, print_time, player_pos, 5)
    room.define_interactive_objects(interactive_objects)
    rooms.append(room)

    return rooms