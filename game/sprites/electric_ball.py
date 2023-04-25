import pygame
from config import *
import random
from utils.counter import Counter
from utils.utils import get_animation_images



class Electric_ball(pygame.sprite.Sprite):
    def __init__(self, window, obj_groups):
        pygame.sprite.Sprite.__init__(self)
        
        self.window = window
        self.obj_groups = obj_groups
        
        position = self.gen_random_position()
        
        self.rect = pygame.Rect(position[0], position[1], ELECTRIC_BALL_WIDTH, ELECTRIC_BALL_HEIGHT)
        self.animation_images = get_animation_images("assets/img/electric-balls", 8, ELECTRIC_BALL_WIDTH, ELECTRIC_BALL_HEIGHT)
        self.current_animation_index = 1
        
        self.sprite_image = self.animation_images[self.current_animation_index]
        
        self.mask = pygame.mask.from_surface(self.sprite_image)
        
        self.animation_counter = Counter(0.1, 10, True, self.animation)

        self.vel_y = 0.3
        
    def animation(self):
        self.current_animation_index += 1
        
        if (self.current_animation_index == 8):
            self.current_animation_index = 1
    
    def gen_random_position(self):
        x = WINDOW_WIDTH
        y = random.randint(0, WINDOW_HEIGHT - ELECTRIC_BALL_HEIGHT - FLOOR_HEIGHT)
        
        return [x, y]

    def movement(self, delta_t):
        self.rect.x -= VEL_X * delta_t
        self.rect.y -= self.vel_y * delta_t

        if self.rect.y <= -(ELECTRIC_BALL_HEIGHT // 3):
            self.vel_y *= -1
            self.rect.y = -(ELECTRIC_BALL_HEIGHT // 3)

        elif self.rect.y >= WINDOW_HEIGHT - FLOOR_HEIGHT - (2 * ELECTRIC_BALL_HEIGHT // 3):
            self.vel_y *= -1
            self.rect.y = WINDOW_HEIGHT - FLOOR_HEIGHT - (2 * ELECTRIC_BALL_HEIGHT // 3)
        
            
        if (self.rect.x < -ELECTRIC_BALL_WIDTH):
            self.obj_groups["electric_balls"].remove(self)
            
    def update_hitbox(self):
        dimensions = self.sprite_image.get_bounding_rect()
        self.rect.width = dimensions[2]
        self.rect.height = dimensions[3]
        self.mask = pygame.mask.from_surface(self.sprite_image)
    
    def draw(self):
        self.sprite_image = self.animation_images[self.current_animation_index]
        self.window.blit(self.sprite_image, (self.rect.x, self.rect.y))
    
    def update(self, delta_t):
        self.movement(delta_t)
        self.animation_counter.update(delta_t)        
        self.update_hitbox()
        self.draw()
        
