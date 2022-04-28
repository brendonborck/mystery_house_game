import os
import pygame

WIDTH=800
HEIGHT=800
TITLE='Mistery House'
FPS=30
SCREEN = None

# Dir paths -----------------------------------------------------------------------
ASSETS_DIR = os.path.join(os.getcwd(), 'assets')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')
START_IMAGE = 'start_image.jpg'

# Room images -----------------------------------------------------------------------
ROOM_IMAGE = "room_v1.jpeg"
ROOM_IMAGE_2 = "room_v2.jpeg"
ROOM_IMAGE_3 = "room_v3.jpeg"
ROOM_IMAGE_4 = "room_v4.jpeg"

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
