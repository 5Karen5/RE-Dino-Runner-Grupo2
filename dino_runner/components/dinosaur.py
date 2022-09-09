from mimetypes import init
from re import S
from signal import default_int_handler
import pygame
from pygame.locals import * #gestiona eventos

from dino_runner.utils.constants import DUCKING  
from dino_runner.utils.constants import RUNNING
from dino_runner.utils.constants import DUCKING
from dino_runner.utils.constants import JUMPING
from dino_runner.utils.constants import DEFAULT_TYPE
from dino_runner.utils.constants import RUNNING_SHIELD
from dino_runner.utils.constants import DUCKING_SHIELD
from dino_runner.utils.constants import SHIELD_TYPE
from dino_runner.utils.constants import JUMPING_SHIELD


class Dinosaur():
    X_POS = 80
    Y_POS = 310#330 
    Y_POS_DUCK = 340
    GRAVITY = 8.5
    
   
    def __init__(self):

        self.soud = pygame.mixer.Sound("jump.wav")
         
        # dinosaur sprites 

        self.run_imagen = {DEFAULT_TYPE:RUNNING,SHIELD_TYPE:RUNNING_SHIELD}
        self.duck_imagen = {DEFAULT_TYPE:DUCKING,SHIELD_TYPE:DUCKING_SHIELD}
        self.jump_imagen = {DEFAULT_TYPE:JUMPING,SHIELD_TYPE:JUMPING_SHIELD}
        self.type = DEFAULT_TYPE
        
        #self.dino_rect = self.run_imagen.get_rect()
        # Controles

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        
        self.step_index = 0
        self.gravity = self.GRAVITY
        self.image = self.run_imagen[self.type][0]
        self.dino_rect = self.image.get_rect()
        # self.dino_rect.inflate_ip(-5,-5)
        # self.dino_rect.topleft =(100,100)

        
        # Definiendo la posicion del Dino
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        
        self.setup_state_boolean()


    def setup_state_boolean(self):
        self.has_powerup = False
        self.shield = False
        self.show_text = False
        self.shield_time_up =0


        
    def update(self, Keys):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >=10:
            self.step_index = 0

        if Keys[pygame.K_UP] and not self.dino_jump:
            # self.sound_jump.play()
            #pygame.mixer.play()
            self.soud.play()
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif Keys[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not(self.dino_jump or Keys[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False
 
#self.image = self.run_imagen[self.step_index]
    def duck(self):
        self.image = self.duck_imagen[self.type][self.step_index //5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index +=1

    def run(self):
        self.image = self.run_imagen[self.type][self.step_index //5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index +=1
         
    def jump(self):
        self.image = self.jump_imagen[self.type]
        self.image = JUMPING
        
        if self.dino_jump:
            self.dino_rect.y -= self.gravity * 4
            self.gravity -=0.8
        if self.gravity < - self.GRAVITY:
            self.dino_jump = False
            self.gravity = self.GRAVITY
        #self.run()
        #pass
    def check_visibility(self,screen):
        if self.shield:
            time_to_show = round((self.shield_time_up-pygame.time.get_ticks())/1000,2)
            if(time_to_show>=0):
                fond = pygame.font.Font("freesansbold.ttf",18)
                text = fond.render(f'shield enable for {time_to_show}', True,(0,0,0))
                textRect = text.get_rect()
                textRect.center=(500,40)
                screen.blit(text,textRect)
            else:
                self.shield = False 
                self.update_to_default(SHIELD_TYPE)

    def update_to_default(self,current_type):
        if(self.type == current_type):
            self.type = DEFAULT_TYPE

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
