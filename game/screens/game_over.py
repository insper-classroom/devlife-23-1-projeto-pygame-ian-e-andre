from config import *
from sprites.button import (Button)
from utils.utils import (get_storaged_data)

class Game_over:
    def __init__(self, window):
        self.window = window
        
        self.groups = {
            "buttons": pygame.sprite.Group(),
        }

        self.background_image = pygame.transform.smoothscale(pygame.image.load("assets/img/blurred-background.png").convert_alpha(), (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.lander_image = pygame.transform.smoothscale(pygame.image.load("assets/img/lander.png").convert_alpha(), (LANDER_WIDTH, LANDER_HEIGHT))
        self.title_panel_image = pygame.transform.smoothscale(pygame.image.load("assets/img/title-panel.png").convert_alpha(), (TITLE_PANEL_WIDTH, TITLE_PANEL_HEIGHT))
        self.digital_font = pygame.font.Font("assets/font/DS-DIGI.ttf", 20)
        
        self.storage_data = get_storaged_data()
        self.dead_char_image = pygame.transform.smoothscale(pygame.image.load(f"assets/img/char-skins/dead-char-{self.storage_data['selected_char']}.png").convert_alpha(), (DEAD_CHAR_IMAGE_WIDTH, DEAD_CHAR_IMAGE_HEIGHT))
        
        self.groups["buttons"].add(Button(window, self.return_initial, "RETURN", [WINDOW_WIDTH / 2 - BUTTON_WIDTH / 2, 280], "3"))
    
    def return_initial(self):
        event = pygame.event.Event(OPEN_INITIAL_EVENT)
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
        
        lander_text = self.digital_font.render("GAME OVER", True, (255, 255, 255))
        self.window.blit(lander_text, (425, 418))
        
        self.window.blit(self.dead_char_image, (WINDOW_WIDTH / 2 - DEAD_CHAR_IMAGE_WIDTH / 2, 130))
        
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
    
    def update(self):
        self.draw()
        
        for i in self.groups:
            self.groups[i].update()
            
        self.change_cursor()