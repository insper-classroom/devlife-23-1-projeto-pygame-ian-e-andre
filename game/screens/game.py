from config import *
from sprites.player import (Player)
from sprites.background import (Background)
from sprites.eletric_obstacle import (Eletric_obstacle)
from sprites.coin import (Coin)
from utils.counter import (Counter)
from sprites.hud import (Hud)
import random

class Game:
    def __init__(self, window):
        self.window = window
        
        self.obj_groups = {
            "eletric_obstacles": pygame.sprite.Group(),
            "coins": pygame.sprite.Group(),
        }

        self.background_image = pygame.image.load(os.path.join( "assets", "img", "background", "1.png"))
        self.background_image = pygame.transform.scale(self.background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        self.prev_time = 0
        self.coin_amount = 0
        self.score = 0
        self.score_counter = Counter(0.1, 4, True, self.update_score)
        self.player = Player(window, self.obj_groups, self)
        self.background = Background(window)
        self.hud = Hud(window)

        self.obstacle_count = 0
        self.obstacle_count_vel = 0.1

        self.add_objects_counter = Counter(0.1, 100, True, self.add_object)
        
    def update_score(self):
        self.score += 1
    
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
        
        self.obj_groups[objects[sorted_index]["group"]].add(objects[sorted_index]["sprite"](self.window, self.obj_groups))
        
    
    def update(self):
        self.window.fill((100, 100, 100))
        self.window.blit(self.background_image, (0, 0))
        delta_t = self.calc_delta_t()
        
        self.background.update(delta_t)
        self.player.update(delta_t)

        
        for i in self.obj_groups:
            self.obj_groups[i].update(delta_t)
            
        self.add_objects_counter.update(delta_t)
        self.score_counter.update(delta_t)
        self.hud.update(delta_t, self)

