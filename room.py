from turtle import position
import pygame
from bed import Bed1, Bed2, Bed3, Bed4
from clock import Clock1, Clock2
import constants
import os
from utils import Utils
from doors import Door1, Door2, Door3, Door3to2, Door2to3, Door2to3Rem,Door4, Door5
from paintings import Painting1
from papers import Paper1, Paper2, Paper3, Paper3_2, Paper4, Paper5
from wardrobe import Wardrobe2, Wardrobe3, Wardrobe2Rem, Wardrobe4
from writingdesk import Writing_Desk1, Writing_Desk2, Writing_Desk4
from chair import DecorationChair, DecorationSofa, DecorationBench, DecorationArmChairLateral, DecorationArmChairFront
from lamp import DecorationLamp, DecorationLamp2
from safe import Safebox3
from shelf import DecorationShelfBooks, DecorationEmptyWardrobe
from vase import DecorationVase1, DecorationVase2, DecorationVaseStar
from piano import DecorationPiano


class Room(pygame.sprite.Sprite):
    """
        Classe que define os aspectos de cada sala
    """
    def __init__(self, name, print_time, player_position, room_image):
        super().__init__()
        room_image_path = os.path.join(constants.IMAGES_DIR, room_image)
        self.image = pygame.image.load(room_image_path).convert()
        self.image = pygame.transform.scale(self.image, (constants.WIDTH, constants.HEIGHT))
        self.rect = self.image.get_rect()
        self.interactive_objects_group = pygame.sprite.Group()
        self.name = name
        self.print_time = print_time
        self.player_position = player_position

    def define_interactive_objects(self, interactive_objects):
        obj_rects_list = []
        for object_name in interactive_objects:
            Constructor = interactive_objects[object_name]['constructor']
            parameters = interactive_objects[object_name]['parameters']
            x = parameters['x']
            y = parameters['y']
            position_mode = parameters['position_mode']
            obj = Constructor(x, y, position_mode)
            self.interactive_objects_group.add(obj)
            if obj.impassable:
                obj_rects_list.append(obj.rect)
        return obj_rects_list
    
    def print_room_message(self):
        parameters = {'message': self.name, 'wait_time': self.print_time}
        Utils().print_message({'full', 'centralized', 'persistent'}, parameters)


def create_rooms():
    created_rooms = {}
    created_rooms['rooms'] = []
    created_rooms['obj_rects_list'] = []

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
            {'x': paper_x, 'y': paper_y, 'position_mode': 'center'}}
    }
    room = Room(name, print_time, player_pos, constants.ROOM_IMAGE_1)
    created_rooms['obj_rects_list'].append(room.define_interactive_objects(interactive_objects))
    created_rooms['rooms'].append(room)

    name = 'Fase 2'
    print_time = 1.7
    player_pos = (int(0.018*constants.WIDTH)*10, int(0.88*constants.HEIGHT/10)*10)
    exit_door_x = 0.12*constants.WIDTH
    exit_door_y = constants.Y_SUPERIOR_WALL
    return_door_x = 0.80*constants.WIDTH
    return_door_y = constants.Y_SUPERIOR_WALL
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
        'return_door': {
            'constructor': Door2to3,
            'parameters': {
                'x': return_door_x,
                'y': return_door_y,
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
         {'constructor': Wardrobe2,
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
            }
        }
    }
    room = Room(name, print_time, player_pos, constants.ROOM_IMAGE_2)
    created_rooms['obj_rects_list'].append(room.define_interactive_objects(interactive_objects))
    created_rooms['rooms'].append(room)


    name = 'Fase 3'
    print_time = 1.7
    player_pos = (int(0.018*constants.WIDTH)*10, int(constants.HEIGHT*0.9/10)*10)
    exit_door_x = 0.12*constants.WIDTH
    exit_door_y = constants.Y_SUPERIOR_WALL
    return_door_x = 0.80*constants.WIDTH
    return_door_y = constants.Y_SUPERIOR_WALL
    paper_x = 0.8*constants.WIDTH
    paper_y = 0.4*constants.HEIGHT
    wdrobe_x = int(0.65*constants.WIDTH/10)*10
    wdrobe_y = 0.20*constants.HEIGHT
    safebox_x = 0.10*constants.WIDTH
    safebox_y = 0.60*constants.HEIGHT
    bed_x = 0.80*constants.WIDTH
    bed_y = 0.90*constants.HEIGHT
    interactive_objects = {

        'exit_door': {
            'constructor': Door3,
            'parameters': {
                'x': exit_door_x,
                'y': exit_door_y,
                'position_mode': 'bottomleft'}},

        'return_door': {
            'constructor': Door3to2,
            'parameters': {
                'x': return_door_x,
                'y': return_door_y,
                'position_mode': 'bottomleft'}},

        'wardrobe': {
            'constructor': Wardrobe3,
            'parameters':{
                'x': wdrobe_x, 
                'y': wdrobe_y, 
                'position_mode': 'center'}},

        'safe': {
            'constructor': Safebox3,
            'parameters':{
                'x': safebox_x, 
                'y': safebox_y, 
                'position_mode': 'center'}},

        'bed': {
            'constructor': Bed3,
            'parameters': {
                'x': bed_x, 
                'y': bed_y, 
                'position_mode': 'center'}},

        'paper': {
            'constructor': Paper3,
            'parameters': {
                'x': paper_x,
                'y': paper_y,
                'position_mode': 'center',
            }
        }
    }
    room = Room(name, print_time, player_pos, constants.ROOM_IMAGE_3)
    created_rooms['obj_rects_list'].append(room.define_interactive_objects(interactive_objects))
    created_rooms['rooms'].append(room)


    name = 'Relembrando...'
    print_time = 1.7
    player_pos = (int(0.084*constants.WIDTH)*10, int(constants.Y_SUPERIOR_WALL/10)*10)
    exit_door_x = 0.12*constants.WIDTH
    exit_door_y = constants.Y_SUPERIOR_WALL
    return_door_x = 0.80*constants.WIDTH
    return_door_y = constants.Y_SUPERIOR_WALL
    vase_x = 0.5*constants.WIDTH
    vase_y = 0.5*constants.HEIGHT
    paper_x = 0.75*constants.WIDTH
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
        'return_door': {
            'constructor': Door2to3Rem,
            'parameters': {
                'x': return_door_x,
                'y': return_door_y,
                'position_mode': 'bottomleft'
            }
        },

        'key': {'constructor': DecorationVaseStar,
        'parameters':
            {'x': vase_x, 
            'y': vase_y, 
            'position_mode': 'center'}
        },

        'writingdesk': 
         {'constructor': Writing_Desk2,
         'parameters':{
             'x': wdesk_x, 
             'y': wdesk_y, 
             'position_mode': 'center'}},

        'wardrobe': 
         {'constructor': Wardrobe2Rem,
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
            }
        }
    }
    room = Room(name, print_time, player_pos, constants.ROOM_IMAGE_2)
    created_rooms['obj_rects_list'].append(room.define_interactive_objects(interactive_objects))
    created_rooms['rooms'].append(room)


    name = 'Voltando...'
    print_time = 1.7
    player_pos = (int(0.018*constants.WIDTH)*10, int(constants.HEIGHT*0.88/10)*10)
    exit_door_x = 0.12*constants.WIDTH
    exit_door_y = constants.Y_SUPERIOR_WALL
    return_door_x = 0.80*constants.WIDTH
    return_door_y = constants.Y_SUPERIOR_WALL
    paper_x = 0.8*constants.WIDTH
    paper_y = 0.4*constants.HEIGHT
    wdrobe_x = 0.65*constants.WIDTH
    wdrobe_y = 0.20*constants.HEIGHT
    safebox_x = 0.10*constants.WIDTH
    safebox_y = 0.60*constants.HEIGHT
    bed_x = 0.80*constants.WIDTH
    bed_y = 0.90*constants.HEIGHT
    interactive_objects = {

        'exit_door': {
            'constructor': Door3,
            'parameters': {
                'x': exit_door_x,
                'y': exit_door_y,
                'position_mode': 'bottomleft'}},

        'return_door': {
            'constructor': Door3to2,
            'parameters': {
                'x': return_door_x,
                'y': return_door_y,
                'position_mode': 'bottomleft'}},

        'wardrobe': {
            'constructor': Wardrobe3,
            'parameters':{
                'x': wdrobe_x, 
                'y': wdrobe_y, 
                'position_mode': 'center'}},

        'safe': {
            'constructor': Safebox3,
            'parameters':{
                'x': safebox_x, 
                'y': safebox_y, 
                'position_mode': 'center'}},

        'bed': {
            'constructor': Bed3,
            'parameters': {
                'x': bed_x, 
                'y': bed_y, 
                'position_mode': 'center'}},

        'paper': {
            'constructor': Paper3_2,
            'parameters': {
                'x': paper_x,
                'y': paper_y,
                'position_mode': 'center',
            }
        }
    }
    room = Room(name, print_time, player_pos, constants.ROOM_IMAGE_3)
    created_rooms['obj_rects_list'].append(room.define_interactive_objects(interactive_objects))
    created_rooms['rooms'].append(room)


    name = 'Fase 4'
    print_time = 1.7
    player_pos = (int(0.018*constants.WIDTH)*10, int(constants.Y_SUPERIOR_WALL/10)*10)
    exit_door_x = 0.12*constants.WIDTH
    exit_door_y = constants.Y_SUPERIOR_WALL
    paper_x = 0.8*constants.WIDTH
    paper_y = 0.4*constants.HEIGHT
    wdesk_x = 0.95*constants.WIDTH
    wdesk_y = 0.50*constants.HEIGHT
    wdrobe_x = 0.50*constants.WIDTH
    wdrobe_y = 0.20*constants.HEIGHT
    bed_x = 0.80*constants.WIDTH
    bed_y = 0.90*constants.HEIGHT
    interactive_objects = {
        'exit_door': {
            'constructor': Door4,
            'parameters': {
                'x': exit_door_x,
                'y': exit_door_y,
                'position_mode': 'bottomleft'
            }
        },
        'writingdesk': 
         {'constructor': Writing_Desk4,
         'parameters':{
             'x': wdesk_x, 
             'y': wdesk_y, 
             'position_mode': 'center'}},

        'wardrobe': 
         {'constructor': Wardrobe4,
         'parameters':{
             'x': wdrobe_x, 
             'y': wdrobe_y, 
             'position_mode': 'center'}},

        'bed': {'constructor': Bed4,
        'parameters':
            {'x': bed_x, 
             'y': bed_y, 
            'position_mode': 'center'}},

        'paper': {
            'constructor': Paper4,
            'parameters': {
                'x': paper_x,
                'y': paper_y,
                'position_mode': 'center',
            }
        }
    }
    room = Room(name, print_time, player_pos, constants.ROOM_IMAGE_1)
    created_rooms['obj_rects_list'].append(room.define_interactive_objects(interactive_objects))
    created_rooms['rooms'].append(room)

    name = 'Fase 5'
    print_time = 1.2
    player_pos = (int(0.012*constants.WIDTH)*10, int(0.088*constants.HEIGHT)*10)
    exit_door_x = 0.48*constants.WIDTH
    exit_door_y = constants.Y_SUPERIOR_WALL
    paper_x = 0.25*constants.WIDTH
    paper_y = 0.8*constants.HEIGHT
    interactive_objects = {
        'exit_door': {
            'constructor': Door5,
            'parameters': {
                'x': exit_door_x,
                'y': exit_door_y,
                'position_mode': 'bottomleft'}},

        'paper': {
            'constructor': Paper5,
            'parameters': {
                'x': paper_x,
                'y': paper_y,
                'position_mode': 'center',
            }
        }
    }
    room = Room(name, print_time, player_pos, constants.ROOM_IMAGE_1)
    created_rooms['obj_rects_list'].append(room.define_interactive_objects(interactive_objects))
    created_rooms['rooms'].append(room)

    return created_rooms