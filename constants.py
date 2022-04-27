import os
import pygame

WIDTH=800
HEIGHT=800
TITLE='Mistery House'
FPS=30
SCREEN = None

ASSETS_DIR = os.path.join(os.getcwd(), 'assets')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')
START_IMAGE='start_image.jpg'
ROOM_IMAGE="room_v2.jpeg"
GRAY = (110, 110, 110)
BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
BLUE=(0, 0, 255)
FONT='comicsansms'

Y_SUPERIOR_WALL = 0.2575*HEIGHT