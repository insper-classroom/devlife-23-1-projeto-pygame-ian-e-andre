import pygame
from config import *
import random
from utils.counter import Counter


class Shuriken(pygame.sprite.Sprite):
    def __init__(self, window, obj_groups):
        pygame.sprite.Sprite.__init__(self)
        
        self.window = window
        self.obj_groups = obj_groups
        
        position = self.gen_random_position()
        
        self.rect = pygame.Rect(position[0], position[1], SHURIKEN_WIDTH, SHURIKEN_HEIGHT)
        self.sprite_image = pygame.transform.smoothscale(pygame.image.load(os.path.join( 'assets', 'img', 'shurikens', '3.png')).convert_alpha(), (SHURIKEN_WIDTH, SHURIKEN_HEIGHT))
        self.sprite_image_rotate = self.sprite_image
        
        self.mask = pygame.mask.from_surface(self.sprite_image)
        
        self.animation_counter = Counter(0.1, 2, True, self.animation)
        self.rotation_angle = 0
        
    def animation(self):
        self.rotation_angle += 10
        self.sprite_image_rotate = pygame.transform.rotate(self.sprite_image, self.rotation_angle)
    
    def gen_random_position(self):
        x = WINDOW_WIDTH
        y = random.randint(0, WINDOW_HEIGHT - SHURIKEN_HEIGHT - FLOOR_HEIGHT)
        
        return [x, y]

    def movement(self, delta_t):
        self.rect.x -= VEL_X * delta_t
        self.rect.y -= VEL_Y * delta_t
            
        if (self.rect.x < -SHURIKEN_WIDTH):
            self.obj_groups["shurikens"].remove(self)
            
    def update_hitbox(self):
        self.mask = pygame.mask.from_surface(self.sprite_image_rotate)    
    
    def draw(self):
        self.window.blit(self.sprite_image_rotate, (self.rect.x, self.rect.y))
    
    def update(self, delta_t):
        self.movement(delta_t)
        self.animation_counter.update(delta_t)        
        self.update_hitbox()
        self.draw()
        
