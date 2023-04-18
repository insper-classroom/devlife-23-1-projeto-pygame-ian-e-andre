import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, window, groups):
        pygame.sprite.Sprite.__init__(self)
        
        self.window = window
        self.groups = groups
        
        
    def draw(self):
        pass
    
    def update(self, delta_t):
        self.draw()
        
        
        
        
        

   
    