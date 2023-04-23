import pygame
from config import *
from pygame.locals import (KEYDOWN)
from screens.game import (Game)

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.init()

font = pygame.font.SysFont("Arial", 12)
clock = pygame.time.Clock()

class Main:
    def __init__(self):
        self.current_screen = Game(WINDOW)
        
    def draw_fps(self):
        fps = str(int(clock.get_fps()))
        fps_text = font.render(f"{fps}", True, (0, 0, 0))
        WINDOW.blit(fps_text, (10, 10))
    
    def run(self):
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

        while 1:
            for event in pygame.event.get():
                self.current_screen.handle_event(event)
                
                if (event.type == pygame.QUIT):
                    pygame.quit()
            
            self.current_screen.update()
            self.draw_fps()
            
            pygame.display.update()  
            
            clock.tick(FPS)
            
            

main = Main()
main.run()