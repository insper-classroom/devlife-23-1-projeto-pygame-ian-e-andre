import pygame
from config import *
from utils.counter import Counter
from utils.utils import get_animation_images

class Propulsion_fx(pygame.sprite.Sprite):
    '''
    This class is responsible for the propulsion effect and animation.
    '''
    def __init__(self, window, player):
        '''
        Initializes the class and its attributes.
        '''
        pygame.sprite.Sprite.__init__(self)
        
        self.window = window
        self.animation_images = get_animation_images("assets/img/propulsion", 4, 70, 93)
        self.current_animation_index = 1
        self.player = player 
        self.animation_counter = Counter(0.1, 8, True, self.animation)
    
    def draw(self):
        '''
        Draws the propulsion effect.
        '''
        image = self.animation_images[self.current_animation_index]
        bounding_rect = image.get_bounding_rect()
        cropped_image = image.subsurface(bounding_rect)
        
        
        self.window.blit(cropped_image, (self.player.rect.x - 27, self.player.rect.y + 70))
        
    def animation(self):
        '''
        Animates the propulsion effect, changing the current animation index.
        '''
        self.current_animation_index += 1
        
        if (self.current_animation_index == 4):
            self.current_animation_index = 1
    
    def update(self, delta_t):
        '''
        Updates the propulsion effect.
        '''
        self.animation_counter.update(delta_t)
        if (self.player.bumping):
            self.draw()