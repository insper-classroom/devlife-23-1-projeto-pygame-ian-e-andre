import pygame
from config import *
from utils.counter import Counter
from utils.utils import get_animation_images

class Jump_fx(pygame.sprite.Sprite):
    def __init__(self, window, player):
        pygame.sprite.Sprite.__init__(self)
        
        self.width = 241
        self.height = 46
        
        self.window = window
        self.animation_images = get_animation_images("game/assets/img/jump-fx", 22, self.width, self.height)
        self.current_animation_index = 0
        self.player = player 
        self.animation_counter = Counter(0.5, 10, True, self.animation)
        self.jump = False
        self.jumped = False
    
    def draw(self):
        image = self.animation_images[self.current_animation_index]
        
        self.window.blit(image, (30, WINDOW_HEIGHT - self.height - FLOOR_HEIGHT))
        
    def animation(self):
        self.current_animation_index += 1
        
        if (self.current_animation_index == len(self.animation_images) - 1):
            self.jump = False
            self.jumped = False
    
    def update(self, delta_t):
        if (self.jump and not self.jumped):
            self.current_animation_index = 0
            self.jumped = True
        
        if (self.jump):
            self.animation_counter.update(delta_t)
            self.draw()
            
