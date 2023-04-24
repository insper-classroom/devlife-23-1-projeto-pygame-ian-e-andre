import pygame
from utils.utils import get_animation_images
from utils.counter import Counter

from config import *

class Hud(pygame.sprite.Sprite):
    def __init__(self, WINDOW):
        pygame.sprite.Sprite.__init__(self)

        self.WINDOW = WINDOW


        self.font_bold_20 = pygame.font.Font(os.path.join('assets', 'font', 'static', 'RobotoMono-Bold.ttf'), 20)

        self.animation_counter = Counter(0.1, 8, True, self.animation)
        self.animation_images = get_animation_images("assets/img/coin", 9, 40, 50)
        self.current_animation_index = 1

        coin_box = pygame.image.load(os.path.join('assets', 'img', 'coin_box.png'))
        self.coin_box = pygame.transform.smoothscale(coin_box, (100,50))
        
        
    def animation(self):
        self.current_animation_index += 1
        
        if (self.current_animation_index == 9):
            self.current_animation_index = 1

    def draw_fps(self, delta_t):
        fps = delta_t
        fps_text = self.font_bold_20.render(f"{fps}", True, BLACK)
        self.WINDOW.blit(fps_text, (10, 10))

    def draw_coin_amount(self, game):
        coins_text = self.font_bold_20.render(f'{game.coin_amount}', True, WHITE)
        self.WINDOW.blit(coins_text, (WINDOW_WIDTH - 50, 22))

        self.sprite_image = self.animation_images[self.current_animation_index]
        self.WINDOW.blit(self.sprite_image, (WINDOW_WIDTH - 95, 5))
    
    def draw_coin_box(self):
        self.WINDOW.blit(self.coin_box, (890,10))

    def update(self, delta_t, game):
        self.draw_coin_box()
        self.draw_coin_amount(game)
        self.draw_fps(delta_t)
        self.animation_counter.update(delta_t)
        