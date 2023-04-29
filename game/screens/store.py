from config import *
from sprites.button import (Button)
from utils.utils import (get_stored_data, update_stored_data)

class Store:
    def __init__(self, window):
        self.window = window
        
        self.groups = {
            "buttons": pygame.sprite.Group(),
        }

        self.background_image = pygame.transform.smoothscale(pygame.image.load("assets/img/blurred-background.png").convert_alpha(), (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.lander_image = pygame.transform.smoothscale(pygame.image.load("assets/img/lander.png").convert_alpha(), (LANDER_WIDTH, LANDER_HEIGHT))
        self.title_panel_image = pygame.transform.smoothscale(pygame.image.load("assets/img/title-panel.png").convert_alpha(), (TITLE_PANEL_WIDTH, TITLE_PANEL_HEIGHT))
        self.coin_bar_image = pygame.transform.smoothscale(pygame.image.load("assets/img/CoinBar.png").convert_alpha(), (COIN_BAR_WIDTH, COIN_BAR_HEIGHT))
        self.coin_image = pygame.transform.smoothscale(pygame.image.load("assets/img/coin/1.png").convert_alpha(), (28, 34))
        self.digital_font_30 = pygame.font.Font("assets/font/DS-DIGI.ttf", 30)
        
        self.char_width = 149
        self.char_height = 192
        self.current_char_image = pygame.transform.smoothscale(pygame.image.load("assets/img/char-skins/char-jetpack-1/1.png").convert_alpha(), (self.char_width, self.char_height))
        self.current_char_id = "1"
        
        self.stored_data = get_stored_data()
        self.chars_id = self.stored_data["chars_id"]
        
        self.show_coin = True
        
        self.groups["buttons"].add(Button(window, self.return_initial_screen, "", [10, 10], "l_arr_2"))

    def return_initial_screen(self):
        event = pygame.event.Event(OPEN_INITIAL_EVENT)
        pygame.event.post(event)

    def show_previous_char(self):
        if (self.chars_id.index(self.current_char_id) - 1 < 0): return
        
        self.current_char_id = self.chars_id[self.chars_id.index(self.current_char_id) - 1]
        self.current_char_image = pygame.transform.smoothscale(pygame.image.load(f"assets/img/char-skins/char-jetpack-{self.current_char_id}/1.png").convert_alpha(), (self.char_width, self.char_height))

        
    def show_next_char(self):
        if (self.chars_id.index(self.current_char_id) + 1 >= len(self.chars_id)):
            return
        
        self.current_char_id = self.chars_id[self.chars_id.index(self.current_char_id) + 1]
        self.current_char_image = pygame.transform.smoothscale(pygame.image.load(f"assets/img/char-skins/char-jetpack-{self.current_char_id}/1.png").convert_alpha(), (self.char_width, self.char_height))

    def check_buttons(self):
        for bttn in self.groups["buttons"]: 
            if (bttn.id in ["pagination", "select", "buy", "selected"]):
                self.groups["buttons"].remove(bttn)
            
        
        if (self.chars_id.index(self.current_char_id) + 1 < len(self.chars_id)):
            self.groups["buttons"].add(Button(self.window, self.show_next_char, "", [(WINDOW_WIDTH / 2 - PAG_BUTTON_WIDTH / 2) + 130, 180], "r_arr", "pagination"))
        
        if (self.chars_id.index(self.current_char_id) - 1 >= 0):
            self.groups["buttons"].add(Button(self.window, self.show_previous_char, "", [(WINDOW_WIDTH / 2 - PAG_BUTTON_WIDTH / 2) - 130, 180], "l_arr", "pagination"))
        
        if (self.current_char_id not in self.stored_data["purchased_characters"]):
            price = str(self.stored_data["chars_price"][self.current_char_id])
            self.groups["buttons"].add(Button(self.window, self.buy_char, price, [(WINDOW_WIDTH / 2 - BOX_BUTTON_WIDTH / 2), 280], "b2", "buy"))
            self.show_coin = True
        elif (self.current_char_id != self.stored_data["selected_char"]):
            self.show_coin = False
            self.groups["buttons"].add(Button(self.window, self.select_char, "SELECT", [(WINDOW_WIDTH / 2 - BOX_BUTTON_WIDTH / 2), 280], "b1", "select"))
        elif (self.current_char_id == self.stored_data["selected_char"]):
            self.show_coin = False
            self.groups["buttons"].add(Button(self.window, lambda: 1, "SELECTED", [(WINDOW_WIDTH / 2 - BOX_BUTTON_WIDTH / 2), 280], "b4", "selected"))


    def select_char(self): 
        self.stored_data["selected_char"] = self.current_char_id
        update_stored_data(self.stored_data)
    
    def buy_char(self):
        price = self.stored_data["chars_price"][self.current_char_id]
        if (self.stored_data["coins_amount"] < price): return
        
        self.stored_data["coins_amount"] -= price
        self.stored_data["purchased_characters"].append(self.current_char_id)
        update_stored_data(self.stored_data)
        
    
    
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
        self.window.blit(self.coin_bar_image, (WINDOW_WIDTH - 10 - COIN_BAR_WIDTH, 10))
        
        
        lander_text = self.digital_font_30.render("STORE", True, (255, 255, 255))
        self.window.blit(lander_text, (430, 412))
        
        coins_text = self.digital_font_30.render(str(self.stored_data["coins_amount"]), True, (255, 255, 255))
        self.window.blit(coins_text, ((WINDOW_WIDTH - 10 - COIN_BAR_WIDTH) + (COIN_BAR_WIDTH / 2 - coins_text.get_width() / 2) , 15))
            
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
        
    def draw_coin(self):
        if (not self.show_coin): return
        
        x = 0
        for bttn in self.groups["buttons"]:
            if (bttn.id == "buy"):
                x = bttn.text_pos[0] - 30
                
        
        self.window.blit(self.coin_image, (x, 290))
        
    def update(self):
        self.draw()
        
        for i in self.groups:
            self.groups[i].update()
            
        self.draw_coin()
        
        self.check_buttons()
        self.change_cursor()