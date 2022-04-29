import os
import pygame

WIDTH=800
HEIGHT=800
TITLE='Mystery House'
FPS=60
SCREEN = None

# Dir paths -----------------------------------------------------------------------
ASSETS_DIR = os.path.join(os.getcwd(), 'assets')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')
MUSIC_DIR = os.path.join(ASSETS_DIR, 'music')
START_IMAGE = 'start_image.jpg'

# Music-------------------------------------------------------------------------
MUSIC_GAME = "Defeat.mp3"
# Room images -----------------------------------------------------------------------
ROOM_IMAGE_1 = "room_v1.jpeg"
ROOM_IMAGE_2 = "room_v2.jpeg"
ROOM_IMAGE_3 = "room_v3.jpg"
ROOM_IMAGE_4 = "room_v4.jpg"

# Room images -----------------------------------------------------------------------
PAPER_IMAGE = "paper.png"
PAPER_IMAGE_2 = "paper 2.png"

# Colors -----------------------------------------------------------------------
GRAY = (110, 110, 110)
BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
BLUE=(0, 0, 255)
FONT='comicsansms'

Y_SUPERIOR_WALL = 0.2575*HEIGHT
