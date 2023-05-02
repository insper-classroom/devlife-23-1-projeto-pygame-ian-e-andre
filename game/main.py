import pygame
from config import *
from screens.game import (Game)
from screens.initial import (Initial)
from screens.history import (History)
from screens.game_over import (Game_over)
from screens.store import (Store)
import sys


WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.init()

clock = pygame.time.Clock()
                    
class Main:
    def __init__(self):
        self.current_screen = Initial(WINDOW)

    def run(self):
        pygame.mixer.music.load('assets/snd/Cyberpunk Moonlight Sonata v2.mp3')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(loops=-1)

        while 1:
            for event in pygame.event.get():
                self.current_screen.handle_event(event)
                
                if (event.type == pygame.QUIT) or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    sys.exit()
                elif (event.type == OPEN_GAME_EVENT):
                    self.current_screen = Game(WINDOW)
                elif (event.type == OPEN_INITIAL_EVENT):
                    self.current_screen = Initial(WINDOW)
                elif (event.type == OPEN_GAME_OVER_EVENT):
                    self.current_screen = Game_over(WINDOW)
                elif (event.type == OPEN_STORE_EVENT):
                    self.current_screen = Store(WINDOW)
                elif (event.type == OPEN_HISTORY_EVENT):
                    self.current_screen = History(WINDOW)
                    
            
            self.current_screen.update()
            
            pygame.display.update()  
            
            clock.tick(FPS)
        
main = Main()
main.run()