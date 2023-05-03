import pygame
from config import *
import random
from utils.counter import Counter
from utils.utils import get_animation_images


class Shield_item(pygame.sprite.Sprite):
    '''
    This class is responsible for the shield item.
    '''
    def __init__(self, window, obj_groups):
        '''
        Initializes the class and its attributes.
        '''
        pygame.sprite.Sprite.__init__(self)
        
        self.window = window
        self.obj_groups = obj_groups
        
        '''
        Sets the shield item's position, sprite image and mask.
        '''
        position = self.gen_random_position()
        self.rect = pygame.Rect(position[0], position[1], SHIELD_ITEM_WIDTH, SHIELD_ITEM_HEIGHT)

        self.sprite_image = pygame.transform.smoothscale(pygame.image.load("assets/img/shield-item.png").convert_alpha(), (40, 40))
        self.mask = pygame.mask.from_surface(self.sprite_image)

    def gen_random_position(self):
        '''
        Generates a random position for the shield item.
        '''
        x = WINDOW_WIDTH
        y = random.randint(0, WINDOW_HEIGHT - SHIELD_ITEM_HEIGHT - FLOOR_HEIGHT)
        
        return [x, y]

    def movement(self, delta_t):
        '''
        Moves the shield item at a constant speed,
        using delta_t to make it frame rate independent.
        Remove the shield item from the shield items group when it goes off screen.
        '''
        self.rect.x -= VEL_X * delta_t
        
        if (self.rect.x < -SHIELD_ITEM_WIDTH):
            self.obj_groups["shield_items"].remove(self)
        
    def draw(self):
        '''
        Draws the shield item.
        '''
        self.window.blit(self.sprite_image, (self.rect.x, self.rect.y))
    
    def update_hitbox(self):
        '''
        Updates the shield item's hitbox.
        '''
        self.mask = pygame.mask.from_surface(self.sprite_image)
    
    def update(self, delta_t):
        '''
        Updates the shield position, hitbox and draws it.
        '''
        self.movement(delta_t)
        self.update_hitbox()
        self.draw()