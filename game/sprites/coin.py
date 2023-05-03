import pygame
from config import *
import random
from utils.counter import Counter
from utils.utils import get_animation_images


class Coin(pygame.sprite.Sprite):
    '''
    This class is responsible for the coin and its animation.
    '''
    def __init__(self, window, obj_groups):
        '''
        Initializes the class and its attributes.
        '''
        pygame.sprite.Sprite.__init__(self)
        
        self.window = window
        self.obj_groups = obj_groups
        
        position = self.gen_random_position()
        
        self.rect = pygame.Rect(position[0], position[1], COIN_WIDTH, COIN_HEIGHT)

        '''
        The animation images are loaded, the animation counter is initialized 
        and the sprite image is set.
        '''
        self.animation_images = get_animation_images("assets/img/coin", 9, COIN_WIDTH, COIN_HEIGHT)
        self.current_animation_index = 1
        self.animation_counter = Counter(0.1, 8, True, self.animation)
        self.sprite_image = self.animation_images[self.current_animation_index]
        self.mask = pygame.mask.from_surface(self.sprite_image)

    def gen_random_position(self):
        '''
        Generates a random position for the coin.
        '''
        x = WINDOW_WIDTH
        y = random.randint(0, WINDOW_HEIGHT - COIN_HEIGHT - FLOOR_HEIGHT)
        
        return [x, y]


    def movement(self, delta_t):
        '''
        Moves the coin at a constant speed, using delta_t to make it frame rate independent.
        Removes the coin from the coins group when it leaves the screen.
        '''
        self.rect.x -= VEL_X * delta_t
        
        if (self.rect.x < -COIN_WIDTH):
            self.obj_groups["coins"].remove(self)
        
    def draw(self):
        '''
        Draws the coin.
        '''
        self.sprite_image = self.animation_images[self.current_animation_index]
        
        self.window.blit(self.sprite_image, (self.rect.x, self.rect.y))
    
    def animation(self):
        '''
        Animates the coin, changing the current animation index.
        '''
        self.current_animation_index += 1
        
        if (self.current_animation_index == 9):
            self.current_animation_index = 1
    
    def update_hitbox(self):
        '''
        Updates the coin's hitbox based on its sprite image.
        '''
        self.mask = pygame.mask.from_surface(self.sprite_image)
    
    def update(self, delta_t):
        '''
        Updates the coin and its animation and draws it.
        '''
        self.movement(delta_t)
        self.animation_counter.update(delta_t)
        self.update_hitbox()   
        self.draw()