import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, window, groups):
        pygame.sprite.Sprite.__init__(self)
        
        self.window = window
        self.groups = groups
        
        self.rect = pygame.Rect(120, 0, PLAYER_WIDTH, PLAYER_HEIGHT)
        
        self.bumping = False
        
        self.vely = 0
        
        self.bump_acel = -0.03
        self.bump_max_acel = -0.5
        
        self.gravity_acel = 0.01
        self.gravity_max_acel = 0.5
        
    def movement(self, delta_t):
        pressed_keys = pygame.key.get_pressed()

        if (pressed_keys[pygame.K_SPACE]):
            if (self.rect.y == WINDOW_HEIGHT - PLAYER_HEIGHT):
                self.vely = self.bump_max_acel # fazer animacao de explosão de poeira por causa do salto 
            elif (self.vely <= self.bump_max_acel):
                self.vely = self.bump_max_acel
            else:
                self.vely += self.bump_acel
                
            self.bumping = True
        else:
            if (self.vely >= self.gravity_max_acel):
                self.vely = self.gravity_max_acel
            else:
                self.vely += self.gravity_acel
                
            self.bumping = False
        self.rect.y += self.vely * delta_t
        
        if (self.rect.y >= WINDOW_HEIGHT - PLAYER_HEIGHT):
            self.rect.y = WINDOW_HEIGHT - PLAYER_HEIGHT
        
    def draw(self):
        self.window.blit(PLAYER_IMAGE, (self.rect.x, self.rect.y))
    
    def update(self, delta_t):
        self.movement(delta_t)
        
        self.draw()
        
        
        
        
        

   
    