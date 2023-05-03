import pygame
from config import *
import random
from utils.counter import Counter
from utils.utils import get_animation_images



class Electric_ball(pygame.sprite.Sprite):
    '''
    This class is responsible for the electric ball and its animation.
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
        self.rect = pygame.Rect(position[0], position[1], ELECTRIC_BALL_WIDTH//3, ELECTRIC_BALL_HEIGHT//3)
        self.animation_images = get_animation_images("assets/img/electric-balls", 8, ELECTRIC_BALL_WIDTH, ELECTRIC_BALL_HEIGHT)
        self.current_animation_index = 1
        self.sprite_image = self.animation_images[self.current_animation_index]
        self.mask = pygame.mask.from_surface(self.sprite_image)
        self.animation_counter = Counter(0.1, 10, True, self.animation)

        '''
        The electric ball's vertical velocity is set.
        '''
        self.vel_y = 0.5 * [1, -1][random.randint(0, 1)]
        
    def animation(self):
        '''
        Animates the electric ball, changing its sprite image.
        '''
        self.current_animation_index += 1
        
        if (self.current_animation_index == 8):
            self.current_animation_index = 1
    
    def gen_random_position(self):
        '''
        Generates a random position for the electric ball.
        '''
        x = WINDOW_WIDTH
        y = random.randint(0, (WINDOW_HEIGHT - (ELECTRIC_BALL_HEIGHT // 3) - FLOOR_HEIGHT) // 2)
        return [x, y]

    def movement(self, delta_t):
        '''
        Moves the electric ball at a constant speed, using delta_t to make it frame rate independent.
        Uses the vertical velocity to move the electric ball up and down. 
        If the electric ball hits the floor or the top, its vertical velocity is inverted.
        Removes the electric ball from the electric balls group when it leaves the screen.
        '''
        self.rect.x -= VEL_X * delta_t * 1.5
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
        '''
        Updates the electric ball's hitbox based on its sprite image.
        '''
        self.mask = pygame.mask.from_surface(self.sprite_image)
    
    def draw(self):
        '''
        Draws the electric ball.
        '''
        self.sprite_image = self.animation_images[self.current_animation_index]
        
        self.window.blit(self.sprite_image, (self.rect.x, self.rect.y))
    
    def update(self, delta_t):
        '''
        Updates the electric ball and its animation and draws it.
        '''
        self.movement(delta_t)
        self.animation_counter.update(delta_t)        
        self.update_hitbox()
        self.draw()
        
