from config import *
from sprites.button import (Button)
from utils.utils import (get_stored_data)

class Game_over:
    '''
    This class is responsible for the game over screen and its methods.
    '''
    def __init__(self, window):
        '''
        This method is responsible for initializing the class.
        It contains the main attributes of the class.
        '''
        self.window = window
        
        self.groups = {
            "buttons": pygame.sprite.Group(),
        }

        '''
        Loads the data, images and fonts used in the screen.
        '''
        self.background_image = pygame.transform.smoothscale(pygame.image.load("assets/img/blurred-background.png").convert_alpha(), (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.lander_image = pygame.transform.smoothscale(pygame.image.load("assets/img/lander.png").convert_alpha(), (LANDER_WIDTH, LANDER_HEIGHT))
        self.title_panel_image = pygame.transform.smoothscale(pygame.image.load("assets/img/title-pannel-empty.png").convert_alpha(), (TITLE_PANEL_WIDTH, TITLE_PANEL_HEIGHT))
        self.digital_font_20 = pygame.font.Font("assets/font/DS-DIGI.ttf", 20)
        self.digital_font_30 = pygame.font.Font("assets/font/DS-DIGI.ttf", 30)
        
        self.stored_data = get_stored_data()
        self.dead_char_image = pygame.transform.smoothscale(pygame.image.load(f"assets/img/char-skins/dead-char-{self.stored_data['selected_char']}.png").convert_alpha(), (DEAD_CHAR_IMAGE_WIDTH, DEAD_CHAR_IMAGE_HEIGHT))
        
        self.groups["buttons"].add(Button(window, self.return_initial, "RETURN", [WINDOW_WIDTH / 2 - BOX_BUTTON_WIDTH / 2, 280], "b3"))
    
    def return_initial(self):
        '''
        Returns to the initial screen.
        '''
        event = pygame.event.Event(OPEN_INITIAL_EVENT)
        pygame.event.post(event)
    
    def handle_event(self, event):
        '''
        Handles the events of the screen, such as mouse clicks.
        '''
        if (event.type == pygame.MOUSEBUTTONDOWN):
            for bttn in self.groups["buttons"]:
                bttn.handle_click()

    def draw(self):
        '''
        Draws the screen and its elements, such as buttons and player images.
        '''
        self.window.fill((100, 100, 100))
        self.window.blit(self.background_image, (0, 0))
        self.window.blit(self.lander_image, (WINDOW_WIDTH / 2 - LANDER_WIDTH / 2, WINDOW_HEIGHT / 2 - LANDER_HEIGHT / 2))
        self.window.blit(self.title_panel_image, (WINDOW_WIDTH / 2 - TITLE_PANEL_WIDTH / 2, 0))
        
        lander_text = self.digital_font_20.render("GAME OVER", True, (255, 255, 255))
        self.window.blit(lander_text, (425, 418))
        
        score_text = self.digital_font_30.render(str(self.stored_data["last_score"]), True, (255, 255, 255))
        self.window.blit(score_text, (WINDOW_WIDTH / 2 - score_text.get_width() / 2, 35))
        
        self.window.blit(self.dead_char_image, (WINDOW_WIDTH / 2 - DEAD_CHAR_IMAGE_WIDTH / 2, 130))
        
    def change_cursor(self):
        '''
        Changes the cursor when it's hovering a button.
        '''
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
        '''
        Updates the game state. 
        '''
        self.draw()
        
        for i in self.groups:
            self.groups[i].update()
            
        self.change_cursor()