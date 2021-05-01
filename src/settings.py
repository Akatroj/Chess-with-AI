import pygame
from Game.utils import BOARD_SIZE
import os.path

# General
FPS = 60
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

BOARD_HEIGHT = BOARD_WIDTH = min(WINDOW_WIDTH, WINDOW_HEIGHT)

AI_LEVEL = 3
SQUARE_SIZE = WINDOW_HEIGHT//BOARD_SIZE
ASSET_FOLDER = 'src/assets'
ICON_PATH = os.path.join(ASSET_FOLDER, 'wp.png')
ICON_SIZE = 32

