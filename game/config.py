import os
import pygame

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 562


SHIELD_BUBBLE_WIDTH = 120
SHIELD_BUBBLE_HEIGHT = 120


JETPACK_PLAYER_WIDTH = 76
JETPACK_PLAYER_HEIGHT = 98

WALKING_PLAYER_WIDTH = 58
WALKING_PLAYER_HEIGHT = 96


SHIELD_ITEM_WIDTH = 40
SHIELD_ITEM_HEIGHT = 40


ELECTRIC_OBSTACLE_WIDTH = 130
ELECTRIC_OBSTACLE_HEIGHT = 25


ELECTRIC_BALL_WIDTH = 120
ELECTRIC_BALL_HEIGHT = 120


COIN_WIDTH = 42
COIN_HEIGHT = 51


FLOOR_HEIGHT = 55


BOX_WIDTH = 130
BOX_HEIGHT = 47


LANDER_WIDTH = 270
LANDER_HEIGHT = 466


TITLE_PANEL_WIDTH = 276
TITLE_PANEL_HEIGHT = 79


BOX_BUTTON_WIDTH = 180
BOX_BUTTON_HEIGHT = 65


SPIKE_WIDTH = 147
SPIKE_HEIGHT = 20


DEAD_CHAR_IMAGE_WIDTH = 236
DEAD_CHAR_IMAGE_HEIGHT = 124


PAG_BUTTON_WIDTH = 28
PAG_BUTTON_HEIGHT = 45


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


FPS = 60


VEL_X = 0.3


OPEN_GAME_EVENT = pygame.USEREVENT + 1
OPEN_INITIAL_EVENT = pygame.USEREVENT + 2
OPEN_GAME_OVER_EVENT = pygame.USEREVENT + 3
OPEN_STORE_EVENT = pygame.USEREVENT + 4