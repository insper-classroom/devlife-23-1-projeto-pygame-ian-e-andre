from config import *
from sprites.player import (Player)
from sprites.background import (Background)
from sprites.electric_obstacle import (Electric_obstacle)
from sprites.electric_ball import (Electric_ball)
from sprites.coin import (Coin)
from sprites.shield_item import (Shield_item)
from utils.counter import (Counter)
from sprites.hud import (Hud)
from sprites.spike import (Spike)
import random
import json

class Game:
    '''
    This class is responsible for the game screen and its methods.
    '''
    def __init__(self, window):
        '''
        This method is responsible for initializing the class.
        It contains the main attributes of the class.
        '''
        self.window = window
        
        self.obj_groups = {
            "electric_obstacles": pygame.sprite.Group(),
            "coins": pygame.sprite.Group(),
            "electric_balls": pygame.sprite.Group(),
            "shield_items": pygame.sprite.Group(),
            "spikes": pygame.sprite.Group()
        }

        self.background_image = pygame.image.load(os.path.join( "assets", "img", "background", "1.png"))
        self.background_image = pygame.transform.scale(self.background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        self.prev_time = 0
        self.taken_coins = 0
        self.score = 0
        self.score_counter = Counter(0.1, 4, True, self.update_score)
        self.player = Player(window, self.obj_groups, self)
        self.background = Background(window)
        self.hud = Hud(window, self)

        self.obstacle_count = 0
        self.obstacle_count_vel = 0.1

        self.add_objects_counter = Counter(0.1, 50, True, self.add_object)
        
    def update_score(self):
        '''
        Updates the score.
        '''
        self.score += 1
    
    def handle_event(self, event):
        '''
        Handles the events of the game screen.
        '''
        pass

    def update_high_score(self):
        '''
        Updates the high score and saves it in the json file.
        '''
        with open('db/stored_data.json', 'r') as json_file:
            data = json.load(json_file)
            if self.score>data["highscore"]:
                data["highscore"] = self.score
                
        with open('db/stored_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
 
    def calc_delta_t(self):
        '''
        Calculates the time between frames and returns it.
        '''
        now = pygame.time.get_ticks()
        delta_t = now - self.prev_time
        self.prev_time = now
        
        return delta_t
    
    def add_object(self):
        '''
        Adds objects to the game screen, such as coins, electric obstacles, electric balls, shield items and spikes.
        '''
        objects = [{"group": "coins", "sprite": Coin}, {"group": "electric_obstacles", "sprite": Electric_obstacle}, {"group": "electric_balls", "sprite": Electric_ball}]
        sorted_index = random.randint(0, len(objects) - 1)
        
        self.obj_groups[objects[sorted_index]["group"]].add(objects[sorted_index]["sprite"](self.window, self.obj_groups))
        
        if (random.random() < 0.05): 
            self.obj_groups["shield_items"].add(Shield_item(self.window, self.obj_groups))
        
        if (random.random() < 0.07):
            self.obj_groups["spikes"].add(Spike(self.window, self.obj_groups))
    
    def update(self):
        '''
        Updates the game state. 
        '''
        self.window.fill((100, 100, 100))
        self.window.blit(self.background_image, (0, 0))
        delta_t = self.calc_delta_t()
        self.background.update(delta_t)
        self.player.update(delta_t)

        
        for i in self.obj_groups:
            self.obj_groups[i].update(delta_t)
            
        self.add_objects_counter.update(delta_t)
        self.score_counter.update(delta_t)
        self.hud.update(delta_t)
