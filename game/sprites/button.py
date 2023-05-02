import pygame
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,QUIT)
from config import *
clock = pygame.time.Clock()

class Button(pygame.sprite.Sprite):
    def __init__(self, window, onclick, text, position, type, id=""):
        pygame.sprite.Sprite.__init__(self)
        
        self.dimensions = [BOX_BUTTON_WIDTH, BOX_BUTTON_HEIGHT]
        self.window = window
        self.text = text
        self.position = position
        self.onclick = onclick
        self.font = pygame.font.Font('assets/font/DS-DIGI.ttf', 26)
        self.click_sound = pygame.mixer.Sound('assets/snd/vgmenuhighlight.wav')
        self.type = type
        self.id = id
        self.text_pos = [0, 0]
        
        if (type == "b1"):
            self.background_box = pygame.transform.smoothscale(pygame.image.load(os.path.join('assets', 'img', 'box.png')).convert_alpha(), (self.dimensions[0], self.dimensions[1]))
        elif (type == "b2"):
            self.background_box = pygame.transform.smoothscale(pygame.image.load(os.path.join('assets', 'img', 'box2.png')).convert_alpha(), (self.dimensions[0], self.dimensions[1]))
        elif (type == "b3"):
            self.background_box = pygame.transform.smoothscale(pygame.image.load(os.path.join('assets', 'img', 'box3.png')).convert_alpha(), (self.dimensions[0], self.dimensions[1]))
        elif (type == "b4"):
            self.background_box = pygame.transform.smoothscale(pygame.image.load(os.path.join('assets', 'img', 'box4.png')).convert_alpha(), (self.dimensions[0], self.dimensions[1]))
        elif (type == "l_arr"):
            self.dimensions = [28, 45]
            self.background_box = pygame.transform.smoothscale(pygame.image.load(os.path.join('assets', 'img', 'LeftArrow.png')).convert_alpha(), (self.dimensions[0], self.dimensions[1]))
        elif (type == "r_arr"):
            self.dimensions = [28, 45]
            self.background_box = pygame.transform.smoothscale(pygame.image.load(os.path.join('assets', 'img', 'RightArrow.png')).convert_alpha(), (self.dimensions[0], self.dimensions[1]))
        elif (type == "l_arr_2"):
            self.dimensions = [20, 32]
            self.background_box = pygame.transform.smoothscale(pygame.image.load(os.path.join('assets', 'img', 'BackArrow.png')).convert_alpha(), (self.dimensions[0], self.dimensions[1]))

        self.rect = pygame.Rect(position[0], position[1], self.dimensions[0], self.dimensions[1])
        
    def get_text_center(self, text_width, text_height):
        x = self.position[0] + (self.dimensions[0] / 2 - text_width / 2) 
        y = self.position[1] + (self.dimensions[1] / 2 - text_height / 2) 
        
        return [x, y]

    def draw(self):
        self.window.blit(self.background_box, (self.position[0], self.position[1]))
        
        text = self.font.render(self.text, True, (255, 255, 255))
        self.text_pos = self.get_text_center(text.get_width(), text.get_height())
        self.window.blit(text, self.text_pos)
    
    def handle_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if (self.rect.collidepoint(mouse_pos)):
            pygame.mixer.Sound.play(self.click_sound)
            self.onclick()
        
    def update(self):
        self.draw()
        