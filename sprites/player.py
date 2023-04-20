import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, window, groups):
        pygame.sprite.Sprite.__init__(self)
        
        self.window = window
        self.groups = groups
        
        self.rect = pygame.Rect(120, 0, JETPACK_PLAYER_WIDTH, JETPACK_PLAYER_HEIGHT)
        
        self.bumping = False
        
        self.vely = 0
        
        self.bump_acel = -0.03
        self.bump_max_acel = -0.5
        
        self.gravity_acel = 0.02
        self.gravity_max_acel = 0.5
        
        self.current_image_index = 1
        self.timer_count = 0
        self.timer_vel = 0.1
        
        self.on_top = False
        self.on_floor = False
        

    def movement(self, delta_t):
        current_player_height = WALKING_PLAYER_HEIGHT
        if (not self.on_floor):
            current_player_height = JETPACK_PLAYER_HEIGHT

        pressed_keys = pygame.key.get_pressed()

        if (pressed_keys[pygame.K_SPACE]):
            if (self.rect.y == WINDOW_HEIGHT - current_player_height - FLOOR_HEIGHT):
                self.vely = self.bump_max_acel / 2 # fazer animacao de explosão de poeira por causa do salto 
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

        
        
        if (self.rect.y >= WINDOW_HEIGHT - current_player_height - FLOOR_HEIGHT):
            self.rect.y = WINDOW_HEIGHT - current_player_height - FLOOR_HEIGHT
            
            self.rect.width = WALKING_PLAYER_WIDTH
            self.rect.height = WALKING_PLAYER_HEIGHT
            
            if (not self.on_floor):
                self.current_image_index = 1
                self.timer_vel = 0.2
                
            self.on_floor = True
        else:
            self.rect.width = JETPACK_PLAYER_WIDTH
            self.rect.height = JETPACK_PLAYER_HEIGHT
            
            if (self.on_floor):
                self.current_image_index = 1
                self.timer_vel = 0.1
                
            self.on_floor = False
        
        if (self.rect.y <= 0):
            self.rect.y = 0
            
            if (not self.on_top):
                self.vely = 0
            self.on_top = True
        else: 
            self.on_top = False
        
    def draw(self):
        image = None
        if (not self.on_floor):
            image = pygame.image.load(os.path.join("assets", "img", "player-jetpack", f"{self.current_image_index}.png"))
            image = pygame.transform.smoothscale(image, (JETPACK_PLAYER_WIDTH, JETPACK_PLAYER_HEIGHT))
        elif (self.on_floor):
            image = pygame.image.load(os.path.join("assets", "img", "player-walking", f"{self.current_image_index}.png"))
            image = pygame.transform.smoothscale(image, (WALKING_PLAYER_WIDTH, WALKING_PLAYER_HEIGHT))
            
            
        self.window.blit(image, (self.rect.x, self.rect.y))
            
    
    def update(self, delta_t):
        self.movement(delta_t)
        
        self.timer_count += self.timer_vel * delta_t
        
        if (self.timer_count >= 10):
            self.timer_count = 0
            self.current_image_index += 1
        
        if ((not self.on_floor and self.current_image_index == 8) or (self.on_floor and self.current_image_index == 16)):
            self.current_image_index = 1
            
        
        self.draw()
        
        
        
        
        

   
    