import pygame
from config import *

def get_animation_images(path, max_index, width, height):
    animation_images = []

    for i in range(1, max_index + 1):
        image = pygame.image.load(f"{path}/{i}.png").convert_alpha()
        image = pygame.transform.smoothscale(image, (width, height))

        animation_images.append(image)
        
    return animation_images

def group_mask_collided(sprite, group):
    collided_sprites = []
    
    for grp_sprite in group:
        if (pygame.sprite.collide_mask(sprite, grp_sprite)):
            collided_sprites.append(grp_sprite)

    if len(collided_sprites) > 0:
        return collided_sprites

    return False    