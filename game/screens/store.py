from config import *
from sprites.button import (Button)


class Store:
    def __init__(self, window):
        self.window = window
        
        self.groups = {
            "buttons": pygame.sprite.Group(),
        }

        self.background_image = pygame.transform.smoothscale(pygame.image.load("assets/img/blurred-background.png").convert_alpha(), (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.lander_image = pygame.transform.smoothscale(pygame.image.load("assets/img/lander.png").convert_alpha(), (LANDER_WIDTH, LANDER_HEIGHT))
        self.title_panel_image = pygame.transform.smoothscale(pygame.image.load("assets/img/title-panel.png").convert_alpha(), (TITLE_PANEL_WIDTH, TITLE_PANEL_HEIGHT))
        self.digital_font = pygame.font.Font("assets/font/DS-DIGI.ttf", 30)
        
        self.char_width = 149
        self.char_height = 192
        self.current_char_image = pygame.transform.smoothscale(pygame.image.load("assets/img/char-skins/char-jetpack-1/1.png").convert_alpha(), (self.char_width, self.char_height))
        self.current_char_id = "1"
        self.chars_id = ["1", "2", "3", "4"]
        
        self.groups["buttons"].add(Button(window, self.show_next_char, "", [(WINDOW_WIDTH / 2 - ARROW_WIDTH / 2) + 130, 180], "5"))

    def show_previous_char(self):
        if (self.chars_id.index(self.current_char_id) - 1 < 0):
            return
        
        self.current_char_id = self.chars_id[self.chars_id.index(self.current_char_id) - 1]
        self.current_char_image = pygame.transform.smoothscale(pygame.image.load(f"assets/img/char-skins/char-jetpack-{self.current_char_id}/1.png").convert_alpha(), (self.char_width, self.char_height))

        
    def show_next_char(self):
        if (self.chars_id.index(self.current_char_id) + 1 >= len(self.chars_id)):
            return
        
        self.current_char_id = self.chars_id[self.chars_id.index(self.current_char_id) + 1]
        self.current_char_image = pygame.transform.smoothscale(pygame.image.load(f"assets/img/char-skins/char-jetpack-{self.current_char_id}/1.png").convert_alpha(), (self.char_width, self.char_height))

    def check_buttons(self):
        if (self.chars_id.index(self.current_char_id) + 1 >= len(self.chars_id)):
            for bttn in self.groups["buttons"]:
                if (bttn.onclick == self.show_next_char):
                    self.groups["buttons"].remove(bttn)
            return
        else:
            has_next_bttn = False
            for bttn in self.groups["buttons"]:
                if (bttn.onclick == self.show_next_char):
                    has_next_bttn = True
            if (not has_next_bttn):
                self.groups["buttons"].add(Button(self.window, self.show_next_char, "", [(WINDOW_WIDTH / 2 - ARROW_WIDTH / 2) + 130, 180], "5"))

        if (self.chars_id.index(self.current_char_id) - 1 < 0):
            for bttn in self.groups["buttons"]:
                if (bttn.onclick == self.show_previous_char):
                    self.groups["buttons"].remove(bttn)
            return
        else:
            has_previous_bttn = False
            for bttn in self.groups["buttons"]:
                if (bttn.onclick == self.show_previous_char):
                    has_previous_bttn = True
            if (not has_previous_bttn):
                self.groups["buttons"].add(Button(self.window, self.show_previous_char, "", [(WINDOW_WIDTH / 2 - ARROW_WIDTH / 2) - 130, 180], "4"))

    def open_store(self):
        pass
    
    def handle_event(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN):
            for bttn in self.groups["buttons"]:
                bttn.handle_click()

    def draw(self):
        self.window.fill((100, 100, 100))
        self.window.blit(self.background_image, (0, 0))
        self.window.blit(self.lander_image, (WINDOW_WIDTH / 2 - LANDER_WIDTH / 2, WINDOW_HEIGHT / 2 - LANDER_HEIGHT / 2))
        self.window.blit(self.title_panel_image, (WINDOW_WIDTH / 2 - TITLE_PANEL_WIDTH / 2, 0))
        self.window.blit(self.current_char_image, (WINDOW_WIDTH / 2 - self.char_width / 2, 80))
        
        lander_text = self.digital_font.render("STORE", True, (255, 255, 255))
        self.window.blit(lander_text, (430, 412))
        
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
            
        self.check_buttons()
        self.change_cursor()