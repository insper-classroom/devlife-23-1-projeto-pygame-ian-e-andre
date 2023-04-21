import pygame
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,QUIT)
from config import *
from utils.counter import Counter
from utils.utils import get_animation_images

class Propulsion(pygame.sprite.Sprite):
    def __init__(self, window, player):
        pygame.sprite.Sprite.__init__(self)
        
        self.window = window
        self.animation_images = get_animation_images("assets/img/propulsion", 4, 80, 80)
        self.current_animation_index = 1
        self.player = player 
        self.animation_counter = Counter(0.1, 8, True, self.animation)
        
    
    def draw(self):
        image = self.animation_images[self.current_animation_index]
        bounding_rect = image.get_bounding_rect()
        cropped_image = image.subsurface(bounding_rect)
        
        
        self.window.blit(cropped_image, (self.player.rect.x - 45, self.player.rect.y + 75))
        
    def animation(self):
        self.current_animation_index += 1
        
        if (self.current_animation_index == 4):
            self.current_animation_index = 1
    
    def update(self, delta_t):
        self.animation_counter.update(delta_t)
        if (self.player.bumping):
            self.draw()