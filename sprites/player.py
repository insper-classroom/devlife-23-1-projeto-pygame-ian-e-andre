import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, window, groups, coin_count):
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
        
        self.coin_count = coin_count

        self.on_top = False
        self.on_floor = False
        
        self.shield = False
        self.alive = False

        self.sounds = {
            "coin_sound": pygame.mixer.Sound("assets/snd/coin01.ogg")
        }
        

    def movement(self, delta_t):
        current_image_height = WALKING_PLAYER_HEIGHT
        if (not self.on_floor):
            current_image_height = JETPACK_PLAYER_HEIGHT

        pressed_keys = pygame.key.get_pressed()

        if (pressed_keys[pygame.K_SPACE]):
            if (self.rect.y == WINDOW_HEIGHT - current_image_height - FLOOR_HEIGHT):
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

        
        
        if (self.rect.y >= WINDOW_HEIGHT - current_image_height - FLOOR_HEIGHT):
            self.rect.y = WINDOW_HEIGHT - current_image_height - FLOOR_HEIGHT
            
            if (not self.on_floor):
                self.current_image_index = 1
                self.timer_vel = 0.2
                
            self.on_floor = True
        else:
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
            
        bounding_rect = image.get_bounding_rect()
        self.rect.width = bounding_rect[2]
        self.rect.height = bounding_rect[3]
        self.window.blit(image, (self.rect.x, self.rect.y))
            
    def check_obstacles_collision(self):
        for grp_name in self.groups:
            grp = self.groups[grp_name]
            
            if (pygame.sprite.spritecollideany(self, grp)):
                if (grp_name == "eletric_obstacles"):
                    pygame.quit()
                elif (grp_name == "coins"):
                    self.coin_count +=1
                    grp.remove(pygame.sprite.spritecollideany(self, grp))
                    self.sounds["coin_sound"].play()
            
                
    
    def update(self, delta_t):
        self.movement(delta_t)
        
        self.timer_count += self.timer_vel * delta_t
        
        if (self.timer_count >= 10):
            self.timer_count = 0
            self.current_image_index += 1
        
        if ((not self.on_floor and self.current_image_index == 8) or (self.on_floor and self.current_image_index == 16)):
            self.current_image_index = 1
            
        self.check_obstacles_collision()
        
        self.draw()
        
        
        
        
        

   
    