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

        self.coin_image = pygame.transform.smoothscale(pygame.image.load("assets/img/coin/1.png").convert_alpha(), (28, 34))
        
        self.game = game

        self.default_background_box = pygame.transform.smoothscale(pygame.image.load(os.path.join('assets', 'img', 'box.png')).convert_alpha(), (BOX_WIDTH,BOX_HEIGHT))
        self.coin_background_box = pygame.transform.smoothscale(pygame.image.load(os.path.join('assets', 'img', 'box2.png')).convert_alpha(), (BOX_WIDTH,BOX_HEIGHT))
        

    def draw_fps(self, delta_t):
        fps = 1000 / delta_t
        fps_text = self.font_bold_12.render(f"{fps}", True, BLACK)
        self.WINDOW.blit(fps_text, (965, 535))

    def draw_score(self):
        self.WINDOW.blit(self.default_background_box, (10,10))
        
        score = self.game.score
        score_text = self.font_bold_20.render(f"{score}", True, WHITE)
        self.WINDOW.blit(score_text, (10 + ((BOX_WIDTH / 2) - (score_text.get_width() / 2)), 8 + ((BOX_HEIGHT / 2) - (score_text.get_height() / 2))))
        
    def draw_coin(self,):
        self.WINDOW.blit(self.coin_background_box, (WINDOW_WIDTH - 10 - BOX_WIDTH,10))
        
        coins_text = self.font_bold_20.render(f'{self.game.coin_amount}', True, WHITE)
        self.WINDOW.blit(coins_text, (WINDOW_WIDTH - 10 - ((BOX_WIDTH / 2) + (coins_text.get_width() / 2)), 8 + ((BOX_HEIGHT / 2) - (coins_text.get_height() / 2))))

        self.WINDOW.blit(self.coin_image, (WINDOW_WIDTH - BOX_WIDTH , 10 + ((BOX_HEIGHT / 2) - 22)))
        
    
    def update(self, delta_t):
        self.draw_coin()
        self.draw_score()
        self.draw_fps(delta_t)
        
        
