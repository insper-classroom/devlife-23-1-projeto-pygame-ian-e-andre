import pygame
from config import *
import random
from utils.counter import Counter
from utils.utils import get_animation_images

class Eletric_obstacle(pygame.sprite.Sprite):
    def __init__(self, window, obj_groups):
        pygame.sprite.Sprite.__init__(self)
        
        self.window = window
        self.obj_groups = obj_groups
        
        position = self.gen_random_position()
        
        self.rect = pygame.Rect(position[0], position[1], ELETRIC_OBSTACLE_WIDTH, ELETRIC_OBSTACLE_HEIGHT)
        self.animation_images = get_animation_images("assets/img/eletric-obstacle", 4, ELETRIC_OBSTACLE_WIDTH, ELETRIC_OBSTACLE_HEIGHT)
        self.current_animation_index = 1
        
        self.sprite_image = self.animation_images[self.current_animation_index]
        self.mask = pygame.mask.from_surface(self.sprite_image)
        
        self.animation_counter = Counter(0.1, 10, True, self.animation)
        
    def animation(self):
        self.current_animation_index += 1
        
        if (self.current_animation_index == 4):
            self.current_animation_index = 1
    
    def gen_random_position(self):
        x = WINDOW_WIDTH
        y = random.randint(0, WINDOW_HEIGHT - ELETRIC_OBSTACLE_HEIGHT - FLOOR_HEIGHT)
        
        return [x, y]


    def movement(self, delta_t):
        self.rect.x -= VEL_X * delta_t
            
        if (self.rect.x < -ELETRIC_OBSTACLE_WIDTH):
            self.obj_groups["eletric_obstacles"].remove(self)
            
    def update_hitbox(self):
        self.mask = pygame.mask.from_surface(self.sprite_image)    
    
    def draw(self):
        self.sprite_image = self.animation_images[self.current_animation_index]
        self.window.blit(self.sprite_image, (self.rect.x, self.rect.y))
    
    def update(self, delta_t):
        self.movement(delta_t)
        
        self.animation_counter.update(delta_t)        
        self.update_hitbox()
        self.draw()
        
