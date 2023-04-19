import os
import pygame

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 560


PLAYER_WIDTH = 78
PLAYER_HEIGHT = 94


BACKGROUND_IMAGE = pygame.image.load(os.path.join("assets", "img", "background", "1.png"))
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WINDOW_WIDTH, WINDOW_HEIGHT))



FPS = 60


VEL_X = 0.3