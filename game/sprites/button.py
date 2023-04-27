import pygame
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,QUIT)
from config import *
clock = pygame.time.Clock()

class Button(pygame.sprite.Sprite):
    def __init__(self, window, onclick, text, position, box_type = "1"):
        pygame.sprite.Sprite.__init__(self)
        
        self.rect = pygame.Rect(position[0], position[1], BUTTON_WIDTH, BUTTON_HEIGHT)

        self.window = window
        self.text = text
        self.position = position
        self.onclick = onclick
        self.font = pygame.font.Font('assets/font/DS-DIGI.ttf', 26)
        
        if (box_type == "1"):
            self.background_box = pygame.transform.smoothscale(pygame.image.load(os.path.join('assets', 'img', 'box.png')).convert_alpha(), (BUTTON_WIDTH,BUTTON_HEIGHT))
        elif (box_type == "2"):
            self.background_box = pygame.transform.smoothscale(pygame.image.load(os.path.join('assets', 'img', 'box2.png')).convert_alpha(), (BUTTON_WIDTH,BUTTON_HEIGHT))
        elif (box_type == "3"):
            self.background_box = pygame.transform.smoothscale(pygame.image.load(os.path.join('assets', 'img', 'box3.png')).convert_alpha(), (BUTTON_WIDTH,BUTTON_HEIGHT))
            
        
    def get_text_center(self, text_width, text_height):
        x = self.position[0] + (BUTTON_WIDTH / 2 - text_width / 2) 
        y = self.position[1] + (BUTTON_HEIGHT / 2 - text_height / 2) 
        
        return [x, y]
        

    def draw(self):
        self.window.blit(self.background_box, (self.position[0], self.position[1]))
        
        text = self.font.render(self.text, True, (255, 255, 255))
        self.window.blit(text, self.get_text_center(text.get_width(), text.get_height()))
    
    def handle_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if (self.rect.collidepoint(mouse_pos)):
            self.onclick()
        
    def update(self):
        self.draw()
        