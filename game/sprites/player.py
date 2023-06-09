import pygame
from config import *
from utils.counter import Counter
from utils.utils import (get_animation_images, group_mask_collided, get_stored_data, update_stored_data, store_last_match)
from sprites.effects.jump_fx import (Jump_fx)
from sprites.effects.propulsion_fx import (Propulsion_fx)


class Player(pygame.sprite.Sprite):
    '''
    This class is responsible for the player and its animations and methods.
    '''
    def __init__(self, window, obj_groups, game):
        '''
        Initializes the class and its attributes.
        '''
        pygame.sprite.Sprite.__init__(self)
        
        self.window = window
        self.obj_groups = obj_groups
        
        self.rect = pygame.Rect(120, 0, JETPACK_PLAYER_WIDTH, JETPACK_PLAYER_HEIGHT)
    
        self.bumping = False
        
        '''
        Sets the player's velocity and acceleration.
        '''
        self.vely = 0
        
        self.bump_acel = -0.03
        self.bump_max_acel = -0.5
        
        self.gravity_acel = 0.02
        self.gravity_max_acel = 0.5

        self.game = game
        
        self.on_top = False
        self.on_floor = False
        
        self.shield = False

        '''
        Loads the player's data, sounds, images, effects and masks.
        '''
        self.sounds = {
            "coin_sound": pygame.mixer.Sound("assets/snd/coin01.ogg"),
            "death_sound": pygame.mixer.Sound("assets/snd/vgdeathsound.wav"),
        }
        
        pygame.mixer.Sound.set_volume(self.sounds["coin_sound"], 0.1)
        
        self.stored_data = get_stored_data()
        
        self.jetpack_animation_images = get_animation_images(f"assets/img/char-skins/char-jetpack-{self.stored_data['selected_char']}", 8, JETPACK_PLAYER_WIDTH, JETPACK_PLAYER_HEIGHT)
        self.walking_animation_images = get_animation_images(f"assets/img/char-skins/char-walking-{self.stored_data['selected_char']}", 16, WALKING_PLAYER_WIDTH, WALKING_PLAYER_HEIGHT)
        self.animation_counter = Counter(0.1, 10, True, self.animation)
        self.current_animation_index = 0
        
        self.sprite_image = self.jetpack_animation_images[self.current_animation_index]
        self.mask = pygame.mask.from_surface(self.sprite_image)
        
        self.effects = {
            "jump": Jump_fx(window, self),
            "propulsion": Propulsion_fx(window, self),
        }
        
        self.shield_image = pygame.transform.smoothscale(pygame.image.load("./assets/img/shield.png").convert_alpha(), (SHIELD_BUBBLE_WIDTH, SHIELD_BUBBLE_HEIGHT))
        

    def movement(self, delta_t):
        '''
        Moves the player, animates it depending on the player's state.
        '''
        current_image_height = WALKING_PLAYER_HEIGHT
        if (not self.on_floor):
            current_image_height = JETPACK_PLAYER_HEIGHT

        pressed_keys = pygame.key.get_pressed()

        if (pressed_keys[pygame.K_SPACE]):
            if (self.rect.y == WINDOW_HEIGHT - current_image_height - FLOOR_HEIGHT):
                self.vely = self.bump_max_acel  
                self.effects["jump"].jump = True
            elif (self.vely <= self.bump_max_acel):
                self.vely = self.bump_max_acel
            elif (self.rect.y > 0):
                self.vely += self.bump_acel
                
            self.bumping = True
        else:
            if (self.vely >= self.gravity_max_acel):
                self.vely = self.gravity_max_acel
            else:
                self.vely += self.gravity_acel
                
            self.bumping = False
        self.rect.y += self.vely * delta_t
        
        '''
        Sets limits to the player's position and determines if the player 
        is on the floor or on the top.
        '''
        if (self.rect.y >= WINDOW_HEIGHT - current_image_height - FLOOR_HEIGHT):
            self.rect.y = WINDOW_HEIGHT - current_image_height - FLOOR_HEIGHT
            
            if (not self.on_floor):
                self.current_animation_index = 0
                self.animation_counter.timer_vel = 0.3
                
            self.on_floor = True
        else:
            if (self.on_floor):
                self.current_animation_index = 0
                self.animation_counter.timer_vel = 0.1
                
            self.on_floor = False
        
        if (self.rect.y <= 0):
            self.rect.y = 0
            
            if (not self.on_top):
                self.vely = 0
            self.on_top = True
        else: 
            self.on_top = False
            
    def kill_player(self, group_name, collided_sprites):
        '''
        Checks if the player has a shield, if it does, the shield is removed,
        otherwise, the player dies.
        Saves the player's score and coins amount and updates the stored data 
        on the json file.
        '''
        if (self.shield):
            self.obj_groups[group_name].remove(collided_sprites)
            self.shield = False
        else: 
            '''
            Updates the high score if the current score is higher than the
            stored high score.
            '''
            if (self.game.score > self.stored_data["high_score"] ):
                self.stored_data["high_score"] = self.game.score
                
            self.stored_data["coins_amount"] += self.game.taken_coins
            self.stored_data["last_score"] = self.game.score
                
            update_stored_data(self.stored_data)
            store_last_match(self.game.score)
            self.sounds["death_sound"].play()
            
            event = pygame.event.Event(OPEN_GAME_OVER_EVENT)
            pygame.event.post(event)
            
        
    def update_hitbox(self):
        '''
        Updates the player's hitbox based on the current sprite image.
        '''
        dimensions = self.sprite_image.get_bounding_rect()
        self.rect.width = dimensions[2]
        self.rect.height = dimensions[3]
        self.mask = pygame.mask.from_surface(self.sprite_image)
        
    def draw(self):
        '''
        Draws the player depending on the current animation and state.
        '''
        if (not self.on_floor):
            self.sprite_image = self.jetpack_animation_images[self.current_animation_index]
        elif (self.on_floor):
            self.sprite_image = self.walking_animation_images[self.current_animation_index] 
            
        self.window.blit(self.sprite_image, (self.rect.x, self.rect.y))
        
        if (self.shield):
            self.window.blit(self.shield_image, (self.rect.x - 25, self.rect.y - 10))
            
    def check_group_collision(self):
        '''
        Checks if the player collides with any of the groups in the game, 
        such as coins, shields or obstacles, and performs the corresponding
        action.
        '''
        for grp_name in self.obj_groups:
            grp = self.obj_groups[grp_name]
                
            collided_sprites = group_mask_collided(self, grp)
            if (collided_sprites):
                if (grp_name in ["electric_obstacles", "electric_balls", "spikes"]):
                    self.kill_player(grp_name, collided_sprites)
                elif (grp_name == "coins"):
                    self.game.taken_coins += 1
                    grp.remove(collided_sprites)
                    self.sounds["coin_sound"].play()
                elif (grp_name == "shield_items"):
                    grp.remove(collided_sprites)
                    self.shield = True
                    self.sounds["coin_sound"].play()
                    
                    
    def animation(self):
        '''
        Animates the player depending on the current state.
        '''
        self.current_animation_index += 1
        
        if (
            (not self.on_floor and self.current_animation_index == len(self.jetpack_animation_images) - 1) 
            or 
            (self.on_floor and self.current_animation_index == len(self.walking_animation_images) - 1)
        ):
            self.current_animation_index = 0
                
    
    def update(self, delta_t):
        '''
        Updates the player's position, animation, effects, hitbox and draws it.
        
        '''
        self.movement(delta_t)
        self.animation_counter.update(delta_t)
        self.check_group_collision()
        self.update_hitbox()
        
        for fx in self.effects.values():
            fx.update(delta_t)
        
        self.draw()
        