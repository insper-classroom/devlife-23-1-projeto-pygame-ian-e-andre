import pygame
from config import *

class Background(pygame.sprite.Sprite):
    def __init__(self, window):
        pygame.sprite.Sprite.__init__(self)
        
        self.window = window
        self.parts = self.gen_parts()
        self.floor = {"x1": 0, "x2": WINDOW_WIDTH}
        
    def gen_parts(self):
        parts = []
        
        for i in range(1, 6):
            image = pygame.image.load(os.path.join("assets", "img", "background", f"{i}.png")).convert_alpha()
            image = pygame.transform.scale(image, (WINDOW_WIDTH, WINDOW_HEIGHT))

            parts.append({"x1": 0, "x2": WINDOW_WIDTH, "image": image})
            
        return parts
        
    def draw(self):
        for part in self.parts:
            self.window.blit(part["image"], (part["x1"], 0))
            self.window.blit(part["image"], (part["x2"], 0))
            
        self.window.blit(FLOOR_IMAGE, (self.floor["x1"], 0))
        self.window.blit(FLOOR_IMAGE, (self.floor["x2"], 0))
    
    def movement(self, delta_t):
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
        self.movement(delta_t)
        
        self.draw()
        
        
        
        
        
        

   
    