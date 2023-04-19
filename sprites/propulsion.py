import pygame
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,QUIT)
from config import *
import random

class Propulsion(pygame.sprite.Sprite):
    def __init__(self, WINDOW, player):
        pygame.sprite.Sprite.__init__(self)
        
        self.rect = pygame.Rect(player.rect.x, player.rect.y, 16, 32)
        
        
        self.WINDOW = WINDOW
        self.delta_t = 0
        self.current_image_index = 1
        self.timer_count = 0
        self.timer_vel = 0.1
        self.player = player 
        
    
    def draw(self):
        img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "img", "propulsion", f"{self.current_image_index}.png")), (20, 40))
        img = pygame.transform.rotate(img, 180)
        self.WINDOW.blit(img, [self.player.rect.x, self.player.rect.y + 40])
    
    def update(self, delta_t):
        self.delta_t = delta_t
        
        
        self.timer_count += self.timer_vel * self.delta_t
        
        if (self.timer_count >= 10):
            self.timer_count = 0
            self.current_image_index += 1
        
        if (self.current_image_index == 5):
            self.current_image_index = 1
           
        if (self.player.bumping):
            self.draw()