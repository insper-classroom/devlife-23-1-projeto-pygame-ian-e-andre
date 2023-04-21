from config import *
from sprites.player import (Player)
from sprites.background import (Background)
from sprites.propulsion import (Propulsion)
from sprites.eletric_obstacle import (Eletric_obstacle)
from sprites.coin import (Coin)
from utils.counter import Counter
import random

class Game:
    def __init__(self, window):
        self.window = window
        
        self.groups = {
            "eletric_obstacles": pygame.sprite.Group(),
            "coins": pygame.sprite.Group(),
        }
        
        self.prev_time = 0
        self.coin_count = 0
        self.player = Player(window, self.groups, self.coin_count)
        self.background = Background(window)
        self.propulsion = Propulsion(window, self.player)
        self.obstacle_count = 0
        self.obstacle_count_vel = 0.1

        self.groups["eletric_obstacles"].add(Eletric_obstacle(window, self.groups))
        self.groups["coins"].add(Coin(window, self.groups))
        
        self.add_objects_counter = Counter(0.1, 100, True, self.add_object)
        
    
    def handle_event(self, event):
        pass

    def calc_delta_t(self):
        now = pygame.time.get_ticks()
        delta_t = now - self.prev_time
        self.prev_time = now
        
        return delta_t
    
    def add_object(self):
        objects = [{"group": "coins", "sprite": Coin}, {"group": "eletric_obstacles", "sprite": Eletric_obstacle}]
        sorted_index = random.randint(0, len(objects) - 1)
        
        self.groups[objects[sorted_index]["group"]].add(objects[sorted_index]["sprite"](self.window, self.groups))
        
    
    def update(self):
        self.window.fill((100, 100, 100))
        self.window.blit(BACKGROUND_IMAGE, (0, 0))
        

        delta_t = self.calc_delta_t()
        
        self.background.update(delta_t)
        self.propulsion.update(delta_t)
        self.player.update(delta_t)
        for i in self.groups:
            self.groups[i].update(delta_t)
            
        self.add_objects_counter.update(delta_t)
        
        
                
        
            