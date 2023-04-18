import os
import pygame

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700


PLAYER_WIDTH = 44
PLAYER_HEIGHT = 64
PLAYER_IMAGE = pygame.image.load(os.path.join("assets", "img", "player.png"))
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))


FPS = 60