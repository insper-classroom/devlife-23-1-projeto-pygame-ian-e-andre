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
        
        self.current_image_index = 1
        self.timer_count = 0
        self.timer_vel = 0.1
        
    def movement(self, delta_t):
        pressed_keys = pygame.key.get_pressed()

        if (pressed_keys[pygame.K_SPACE]):
            if (self.rect.y == WINDOW_HEIGHT - PLAYER_HEIGHT):
                self.vely = self.bump_max_acel # fazer animacao de explosão de poeira por causa do salto 
            elif (self.vely <= self.bump_max_acel):
                self.vely = self.bump_max_acel
            elif (self.rect.y > 0):
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
        elif (self.rect.y <= 0):
            self.rect.y = 0
            
            
        
    def draw(self):
        image = pygame.image.load(os.path.join("assets", "img", "player", f"{self.current_image_index}.png"))
        image = pygame.transform.smoothscale(image, (150, 150))
        bounding_rect = image.get_bounding_rect()
        cropped_image = image.subsurface(bounding_rect)
        
        self.window.blit(cropped_image, (self.rect.x, self.rect.y))
    
    def update(self, delta_t):
        self.movement(delta_t)
        
        self.timer_count += self.timer_vel * delta_t
        
        if (self.timer_count >= 10):
            self.timer_count = 0
            self.current_image_index += 1
        
        if (self.current_image_index == 4):
            self.current_image_index = 1
        
        self.draw()
        
        
        
        
        

   
    