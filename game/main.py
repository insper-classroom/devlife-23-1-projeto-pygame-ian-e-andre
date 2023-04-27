import pygame
from config import *
from screens.game import (Game)
from screens.initial import (Initial)


WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.init()

clock = pygame.time.Clock()
                    
class Main:
    def __init__(self):
        self.current_screen = Initial(WINDOW)

    def run(self):
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

        while 1:
            for event in pygame.event.get():
                self.current_screen.handle_event(event)
                
                if (event.type == pygame.QUIT):
                    pygame.quit()
                elif (event.type == OPEN_GAME_EVENT):
                    self.current_screen = Game(WINDOW)
            
            self.current_screen.update()
            
            pygame.display.update()  
            
            clock.tick(FPS)
        
main = Main()
main.run()