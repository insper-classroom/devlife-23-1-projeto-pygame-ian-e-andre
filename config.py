import os
import pygame

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 560


PLAYER_WIDTH = 44
PLAYER_HEIGHT = 64
PLAYER_IMAGE = pygame.image.load(os.path.join("assets", "img", "player.png"))
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))


BACKGROUND_IMAGE = pygame.image.load(os.path.join("assets", "img", "background", "1.png"))
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WINDOW_WIDTH, WINDOW_HEIGHT))



FPS = 60


VEL_X = 0.3