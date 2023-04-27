import pygame
from config import *
import random

class Spike(pygame.sprite.Sprite):
    def __init__(self, window, obj_groups):
        pygame.sprite.Sprite.__init__(self)
        
        self.window = window
        self.obj_groups = obj_groups
        
        self.rect = pygame.Rect(WINDOW_WIDTH, WINDOW_HEIGHT - FLOOR_HEIGHT - SPIKE_HEIGHT, SPIKE_WIDTH, SPIKE_HEIGHT)
        self.sprite_image = pygame.transform.smoothscale(pygame.image.load("assets/img/spike.png").convert_alpha(), (SPIKE_WIDTH,SPIKE_HEIGHT))
        self.mask = pygame.mask.from_surface(self.sprite_image)
        
        
    def movement(self, delta_t):
        self.rect.x -= VEL_X * delta_t
            
        if (self.rect.x < -ELECTRIC_OBSTACLE_WIDTH):
            self.obj_groups["electric_obstacles"].remove(self)
            
    def update_hitbox(self):
        self.mask = pygame.mask.from_surface(self.sprite_image)    
    
    def draw(self):
        self.window.blit(self.sprite_image, (self.rect.x, self.rect.y))
    
    def update(self, delta_t):
        self.movement(delta_t)
        
        self.update_hitbox()
        self.draw()
        
