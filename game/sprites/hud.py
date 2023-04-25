import pygame
from config import *
from utils.utils import get_animation_images
from utils.counter import Counter

class Hud(pygame.sprite.Sprite):
    def __init__(self, WINDOW, game):
        pygame.sprite.Sprite.__init__(self)

        self.WINDOW = WINDOW

        self.font_bold_20 = pygame.font.Font(os.path.join( 'assets', 'font', 'static', 'RobotoMono-Bold.ttf'), 20)
        self.font_bold_12 = pygame.font.Font(os.path.join( 'assets', 'font', 'static', 'RobotoMono-Bold.ttf'), 12)

        self.coin_icon_animation_counter = Counter(0.1, 8, True, self.coin_icon_animation)
        self.coin_icon_animation_images = get_animation_images("assets/img/coin", 9, 40, 50)
        self.current_animation_index = 1
        
        self.game = game

        self.background_box = pygame.transform.smoothscale(pygame.image.load(os.path.join( 'assets', 'img', 'coin_box.png')).convert(), (100,50))
        
        
    def coin_icon_animation(self):
        self.current_animation_index += 1
        
        if (self.current_animation_index == 9):
            self.current_animation_index = 1

    def draw_fps(self, delta_t):
        fps = 1000 / delta_t
        fps_text = self.font_bold_12.render(f"{fps}", True, BLACK)
        self.WINDOW.blit(fps_text, (965, 535))

    def draw_score(self):
        self.WINDOW.blit(self.background_box, (10,10))
        
        score = self.game.score
        score_text = self.font_bold_20.render(f"{score}", True, WHITE)
        self.WINDOW.blit(score_text, (57-(score_text.get_width()//2), 22))
        

    def draw_coin(self,):
        self.WINDOW.blit(self.background_box, (890,10))
        
        coins_text = self.font_bold_20.render(f'{self.game.coin_amount}', True, WHITE)
        self.WINDOW.blit(coins_text, (WINDOW_WIDTH - 50, 22))

        image = self.coin_icon_animation_images[self.current_animation_index]
        self.WINDOW.blit(image, (WINDOW_WIDTH - 95, 5))
        
    
    def update(self, delta_t):
        self.draw_coin()
        self.draw_score()
        self.draw_fps(delta_t)
        
        self.coin_icon_animation_counter.update(delta_t)
        
