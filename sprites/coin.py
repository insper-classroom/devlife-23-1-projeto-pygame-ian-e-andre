import pygame
from config import *
import random
from utils.counter import Counter
from utils.utils import get_animation_images


class Coin(pygame.sprite.Sprite):
    def __init__(self, window, obj_groups):
        pygame.sprite.Sprite.__init__(self)
        
        self.window = window
        self.obj_groups = obj_groups
        
        position = self.gen_random_position()
        
        self.rect = pygame.Rect(position[0], position[1], COIN_WIDTH, COIN_HEIGHT)

        self.animation_images = get_animation_images("assets/img/coin", 9, COIN_WIDTH, COIN_HEIGHT)
        self.current_animation_index = 1
        
        self.animation_counter = Counter(0.1, 8, True, self.animation)
        self.sprite_image = self.animation_images[self.current_animation_index]
        self.mask = pygame.mask.from_surface(self.sprite_image)

    def gen_random_position(self):
        x = WINDOW_WIDTH
        y = random.randint(0, WINDOW_HEIGHT - COIN_HEIGHT - FLOOR_HEIGHT)
        
        return [x, y]


    def movement(self, delta_t):
        self.rect.x -= VEL_X * delta_t
        
        if (self.rect.x < -COIN_WIDTH):
            self.obj_groups["coins"].remove(self)
        
    def draw(self):
        self.sprite_image = self.animation_images[self.current_animation_index]
        
        self.window.blit(self.sprite_image, (self.rect.x, self.rect.y))
    
    def animation(self):
        self.current_animation_index += 1
        
        if (self.current_animation_index == 9):
            self.current_animation_index = 1
    
    def update_hitbox(self):
        self.mask = pygame.mask.from_surface(self.sprite_image)
    
    def update(self, delta_t):
        self.movement(delta_t)
        
        self.animation_counter.update(delta_t)
        self.update_hitbox()
            
        self.draw()