from config import *
from sprites.player import (Player)
from sprites.background import (Background)
from sprites.propulsion import (Propulsion)

class Game:
    def __init__(self, window):
        self.window = window
        
        self.groups = {}
        self.prev_time = 0
        self.player = Player(window, self.groups)
        self.background = Background(window)
        self.propulsion = Propulsion(window, self.player)
        
    
    def handle_event(self, event):
        pass

    def calc_delta_t(self):
        now = pygame.time.get_ticks()
        delta_t = now - self.prev_time
        self.prev_time = now
        
        return delta_t
    
    def update(self):
        self.window.fill((100, 100, 100))
        self.window.blit(BACKGROUND_IMAGE, (0, 0))
        

        delta_t = self.calc_delta_t()
        self.background.update(delta_t)
        self.propulsion.update(delta_t)
        self.player.update(delta_t)
        
                
        
            