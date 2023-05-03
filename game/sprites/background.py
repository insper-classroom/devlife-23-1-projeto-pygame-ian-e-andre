import pygame
from config import *

class Background(pygame.sprite.Sprite):
    '''
    This class is responsible for the background and floor.
    '''
    def __init__(self, window):
        '''
        Initializes the class and its attributes.
        '''
        pygame.sprite.Sprite.__init__(self)
        
        self.floor_image = pygame.image.load(os.path.join( "assets", "img", "floor.png"))
        self.floor_image = pygame.transform.scale(self.floor_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        self.window = window
        self.parts = self.gen_parts()
        self.floor = {"x1": 0, "x2": WINDOW_WIDTH}
        
    def gen_parts(self):
        '''
        Generates the background parts and returns them.
        '''
        parts = []
        
        for i in range(1, 6):
            image = pygame.image.load(os.path.join( "assets", "img", "background", f"{i}.png")).convert_alpha()
            image = pygame.transform.scale(image, (WINDOW_WIDTH, WINDOW_HEIGHT))

            parts.append({"x1": 0, "x2": WINDOW_WIDTH, "image": image})
            
        return parts
        
    def draw(self):
        '''
        Draws the background and floor using the current parts.'''
        for part in self.parts:
            self.window.blit(part["image"], (part["x1"], 0))
            self.window.blit(part["image"], (part["x2"], 0))
            
        self.window.blit(self.floor_image, (self.floor["x1"], 0))
        self.window.blit(self.floor_image, (self.floor["x2"], 0))
    
    def movement(self, delta_t):
        '''
        Moves the background and floor at a constant speed, using the delta_t.
        '''
        for i in range(len(self.parts)):
            self.parts[i]["x1"] -= (VEL_X * delta_t) * (0 + ((i + 1) * 0.2))
            self.parts[i]["x2"] -= (VEL_X * delta_t) * (0 + ((i + 1) * 0.2))
            
            if (self.parts[i]["x1"] < WINDOW_WIDTH * -1):
                self.parts[i]["x1"] = 0
            
            if (self.parts[i]["x2"] < 0):
                self.parts[i]["x2"] = WINDOW_WIDTH

        self.floor["x1"] -= (VEL_X * delta_t) 
        self.floor["x2"] -= (VEL_X * delta_t)

        if (self.floor["x1"] < WINDOW_WIDTH * -1):
            self.floor["x1"] = 0
            
        if (self.floor["x2"] < 0):
            self.floor["x2"] = WINDOW_WIDTH

    
    def update(self, delta_t):
        '''
        Updates the background and floor, moving and drawing them.
        '''
        self.movement(delta_t)
        
        self.draw()
        
