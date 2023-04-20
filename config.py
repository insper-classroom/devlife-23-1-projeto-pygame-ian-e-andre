import os
import pygame

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 562


JETPACK_PLAYER_WIDTH = 76
JETPACK_PLAYER_HEIGHT = 98
WALKING_PLAYER_WIDTH = 58
WALKING_PLAYER_HEIGHT = 96


ELETRIC_OBSTACLE_WIDTH = 130
ELETRIC_OBSTACLE_HEIGHT = 25


BACKGROUND_IMAGE = pygame.image.load(os.path.join("assets", "img", "background", "1.png"))
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WINDOW_WIDTH, WINDOW_HEIGHT))


FLOOR_HEIGHT = 55
FLOOR_IMAGE = pygame.image.load(os.path.join("assets", "img", "floor.png"))
FLOOR_IMAGE = pygame.transform.scale(FLOOR_IMAGE, (WINDOW_WIDTH, WINDOW_HEIGHT))


FPS = 60


VEL_X = 0.3