import pygame
from config import *
from pygame.locals import (KEYDOWN)
from screens.game import (Game)

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.init()

class Main:
    def __init__(self):
        self.current_screen = Game(WINDOW)
        
    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(FPS)
            
            for event in pygame.event.get():
                self.current_screen.handle_event(event)
                
                if (event.type == pygame.QUIT):
                    pygame.quit()
            
            self.current_screen.update()
                   
            pygame.display.update()  
            

main = Main()
main.run()