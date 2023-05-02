from config import *
from sprites.button import (Button)
from utils.utils import get_matches_history, get_stored_data

class History:
    def __init__(self, window):
        self.window = window
        
        self.groups = {
            "buttons": pygame.sprite.Group(),
        }

        self.background_image = pygame.transform.smoothscale(pygame.image.load("assets/img/blurred-background.png").convert_alpha(), (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.lander_image = pygame.transform.smoothscale(pygame.image.load("assets/img/lander.png").convert_alpha(), (LANDER_WIDTH, LANDER_HEIGHT))
        self.title_panel_image = pygame.transform.smoothscale(pygame.image.load("assets/img/title-panel.png").convert_alpha(), (TITLE_PANEL_WIDTH, TITLE_PANEL_HEIGHT))
        self.history_panel_image = pygame.transform.smoothscale(pygame.image.load("assets/img/history-panel.png").convert_alpha(), (HISTORY_PANEL_WIDTH, HISTORY_PANEL_HEIGHT))
        
        self.digital_font_30 = pygame.font.Font("assets/font/DS-DIGI.ttf", 30)
        self.digital_font_26 = pygame.font.Font("assets/font/DS-DIGI.ttf", 26)
        self.digital_font_20 = pygame.font.Font("assets/font/DS-DIGI.ttf", 20)
        
        self.matches_history = get_matches_history()
        self.matches_history.reverse()
        self.matches_history = self.matches_history[0:9]
        self.stored_data = get_stored_data()
        
        self.groups["buttons"].add(Button(window, self.return_initial_screen, "", [10, 10], "l_arr_2"))

    def return_initial_screen(self):
        event = pygame.event.Event(OPEN_INITIAL_EVENT)
        pygame.event.post(event)
        
    def start_game(self):
        event = pygame.event.Event(OPEN_GAME_EVENT)
        pygame.event.post(event)
    
    def open_store(self):
        event = pygame.event.Event(OPEN_STORE_EVENT)
        pygame.event.post(event)
    
    def handle_event(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN):
            for bttn in self.groups["buttons"]:
                bttn.handle_click()

    def draw(self):
        self.window.fill((100, 100, 100))
        self.window.blit(self.background_image, (0, 0))
        self.window.blit(self.lander_image, (WINDOW_WIDTH / 2 - LANDER_WIDTH / 2, WINDOW_HEIGHT / 2 - LANDER_HEIGHT / 2))
        self.window.blit(self.title_panel_image, (WINDOW_WIDTH / 2 - TITLE_PANEL_WIDTH / 2, 0))
        
        self.window.blit(self.history_panel_image, (WINDOW_WIDTH / 2 - HISTORY_PANEL_WIDTH / 2, 105))
        
        record_text = self.digital_font_26.render(f"RECORD: {self.stored_data['high_score']}", True, (255, 255, 255))
        self.window.blit(record_text, (WINDOW_WIDTH / 2 - record_text.get_width() / 2, 130))
        
        lander_text = self.digital_font_30.render("HISTORY", True, (255, 255, 255))
        self.window.blit(lander_text, (418, 412))
        
    def change_cursor(self):
        hovering = False
        mouse_pos = pygame.mouse.get_pos()
        for bttn in self.groups["buttons"]:
            if (bttn.rect.collidepoint(mouse_pos)):
                hovering = True

        if (hovering):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) 
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 
        
    def draw_matches_history(self):
        basex = WINDOW_WIDTH / 2 - HISTORY_PANEL_WIDTH / 2
        basey = 160
        
        for i in range(len(self.matches_history)):
            text = self.digital_font_20.render(self.matches_history[i].replace("\n", ""), True, (196, 228, 255))
            self.window.blit(text, (basex + HISTORY_PANEL_WIDTH / 2 - text.get_width() / 2, basey + i * 20))
        
    def update(self):
        self.draw()
        
        for i in self.groups:
            self.groups[i].update()
        
        self.draw_matches_history()
            
        self.change_cursor()