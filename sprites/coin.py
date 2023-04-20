import pygame
from config import *
import random

class Coin(pygame.sprite.Sprite):
    def __init__(self, window, groups):
        pygame.sprite.Sprite.__init__(self)
        
        self.window = window
        self.groups = groups
        
        position = self.gen_random_position()
        
        self.rect = pygame.Rect(position[0], position[1], COIN_WIDTH, COIN_HEIGHT)

        self.current_image_index = 1
        self.timer_count = 0
        self.timer_vel = 0.1
        
        self.velx = 0.1


    def gen_random_position(self):
        x = WINDOW_WIDTH
        y = random.randint(0, WINDOW_HEIGHT - COIN_HEIGHT - FLOOR_HEIGHT)
        
        return [x, y]


    def movement(self, delta_t):
        self.rect.x -= VEL_X * delta_t
            
        
    def draw(self):
        image = pygame.image.load(os.path.join("assets", "img", "coin", f"{self.current_image_index}.png"))
        image = pygame.transform.smoothscale(image, (COIN_WIDTH, COIN_HEIGHT))
                
        self.window.blit(image, (self.rect.x, self.rect.y))
    
    def update(self, delta_t):
        self.movement(delta_t)
        
        self.timer_count += self.timer_vel * delta_t
        
        if (self.timer_count >= 10):
            self.timer_count = 0
            self.current_image_index += 1
        
        if (self.current_image_index == 4):
            self.current_image_index = 1
            
        
        self.draw()