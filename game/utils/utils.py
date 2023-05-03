import pygame
from config import *
import json
from datetime import datetime

'''
This file contains the utility functions used in the game.
'''

def get_animation_images(path, max_index, width, height):
    '''
    Returns a list of images to be used in an animation.
    '''
    animation_images = []

    for i in range(1, max_index + 1):
        image = pygame.image.load(f"{path}/{i}.png").convert_alpha()
        image = pygame.transform.smoothscale(image, (width, height))

        animation_images.append(image)
        
    return animation_images

def group_mask_collided(sprite, group):
    '''
    Returns a list of sprites that collided with the sprite.
    '''
    collided_sprites = []
    
    for grp_sprite in group:
        if (pygame.sprite.collide_mask(sprite, grp_sprite)):
            collided_sprites.append(grp_sprite)

    if len(collided_sprites) > 0:
        return collided_sprites

    return False    

def get_stored_data():
    '''
    Returns the stored data.
    '''
    file = open('./db/stored_data.json')
    data = json.load(file)
    
    return data

def update_stored_data(data): 
    '''
    Updates the stored data.
    '''
    with open('db/stored_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
        
def get_matches_history():
    '''
    Returns the matches history.
    '''
    file = open("./db/history.txt", "r")
    return file.readlines()

def store_last_match(score):
    '''
    Stores the last match in the history file.
    '''
    file = open("./db/history.txt", "a")
    file.writelines(f"{score} - {get_date_time()}\n")
    file.close()

def get_date_time():
    '''
    Returns the current date and time.
    '''
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y")
    return date_time
