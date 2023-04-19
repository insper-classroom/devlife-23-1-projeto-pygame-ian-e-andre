import pygame
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,QUIT)
from config import *
import random

class Propulsion(pygame.sprite.Sprite):
    def __init__(self, window, player):
        pygame.sprite.Sprite.__init__(self)
        
        self.rect = pygame.Rect(player.rect.x, player.rect.y, 16, 32)
        
        
        self.window = window
        self.delta_t = 0
        self.current_image_index = 1
        self.timer_count = 0
        self.timer_vel = 0.1
        self.player = player 
        
    
    def draw(self):
        image = pygame.image.load(os.path.join("assets", "img", "propulsion", f"{self.current_image_index}.png"))
        image = pygame.transform.smoothscale(image, (80, 80))
        bounding_rect = image.get_bounding_rect()
        cropped_image = image.subsurface(bounding_rect)
        
        self.window.blit(cropped_image, (self.player.rect.x - 60, self.player.rect.y + 60))
        
    
    def update(self, delta_t):
        self.delta_t = delta_t
        
        
        self.timer_count += self.timer_vel * self.delta_t
        
        if (self.timer_count >= 10):
            self.timer_count = 0
            self.current_image_index += 1
        
        if (self.current_image_index == 4):
            self.current_image_index = 1
           
        if (self.player.bumping):
            self.draw()