import pygame
from config import *
import random
from utils.counter import Counter
from utils.utils import get_animation_images

class Electric_obstacle(pygame.sprite.Sprite):
    '''
    This class is responsible for the electric obstacle and its animation.
    '''
    def __init__(self, window, obj_groups):
        '''
        Initializes the class and its attributes.
        '''
        pygame.sprite.Sprite.__init__(self)
        
        self.window = window
        self.obj_groups = obj_groups
        
        position = self.gen_random_position()
        
        '''
        The animation images are loaded, the animation counter is initialized
        and the sprite image is set.
        '''
        self.rect = pygame.Rect(position[0], position[1], ELECTRIC_OBSTACLE_WIDTH, ELECTRIC_OBSTACLE_HEIGHT)
        self.animation_images = get_animation_images("assets/img/electric-obstacle", 4, ELECTRIC_OBSTACLE_WIDTH, ELECTRIC_OBSTACLE_HEIGHT)
        self.current_animation_index = 1
        self.sprite_image = self.animation_images[self.current_animation_index]
        self.mask = pygame.mask.from_surface(self.sprite_image)
        self.animation_counter = Counter(0.1, 10, True, self.animation)
        
    def animation(self):
        '''
        Animates the electric obstacle, changing its sprite image.
        '''
        self.current_animation_index += 1
        
        if (self.current_animation_index == 4):
            self.current_animation_index = 1
    
    def gen_random_position(self):
        '''
        Generates a random position for the electric obstacle.
        '''
        x = WINDOW_WIDTH
        y = random.randint(0, WINDOW_HEIGHT - ELECTRIC_OBSTACLE_HEIGHT - FLOOR_HEIGHT)
        
        return [x, y]


    def movement(self, delta_t):
        '''
        Moves the electric obstacle at a constant speed, 
        using delta_t to make it frame rate independent.
        Removes the electric obstacle from the electric_obstacles group when it goes off screen.
        '''
        self.rect.x -= VEL_X * delta_t
            
        if (self.rect.x < -ELECTRIC_OBSTACLE_WIDTH):
            self.obj_groups["electric_obstacles"].remove(self)
            
    def update_hitbox(self):
        '''
        Updates the hitbox of the electric obstacle based on its sprite image.
        '''
        self.mask = pygame.mask.from_surface(self.sprite_image)    
    
    def draw(self):
        '''
        Draws the electric obstacle.
        '''
        self.sprite_image = self.animation_images[self.current_animation_index]
        self.window.blit(self.sprite_image, (self.rect.x, self.rect.y))
    
    def update(self, delta_t):
        '''
        Updates the electric obstacle and its animation and draws it.
        '''
        self.movement(delta_t)
        self.animation_counter.update(delta_t)        
        self.update_hitbox()
        self.draw()
        
