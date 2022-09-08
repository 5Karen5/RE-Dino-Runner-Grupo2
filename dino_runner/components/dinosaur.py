from mimetypes import init
from signal import default_int_handler
import pygame
from pygame.locals import * #gestiona eventos


from dino_runner.utils.constants import RUNNING
from dino_runner.utils.constants import DUCKING
from dino_runner.utils.constants import JUMPING

class Dinosaur():
    X_POS = 80
    Y_POS = 310#330 
    Y_POS_DUCK = 340
    GRAVITY = 8.5
    # SOUND = pygame.mixer.music.load("y2mate.com-Chrome-Dino-Game-jump-sound-effect.wav")

   
    def __init__(self):

        self.soud = pygame.mixer.Sound("jump.wav")
         
        # dinosaur sprites 

        self.run_imagen = RUNNING
        self.duck_imagen = DUCKING
        self.jump_imagen = JUMPING
        
        #self.dino_rect = self.run_imagen.get_rect()
        # Controles

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        
        self.step_index = 0
        self.gravity = self.GRAVITY
        self.image = self.run_imagen[0]
        self.dino_rect = self.image.get_rect()
        # self.dino_rect.inflate_ip(-5,-5)
        # self.dino_rect.topleft =(100,100)

        
        # Definiendo la posicion del Dino
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

        
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
        self.image = self.duck_imagen[self.step_index //5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index +=1

    def run(self):
        self.image = self.run_imagen[self.step_index //5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index +=1
         
    def jump(self):
        self.image = self.jump_imagen
        
        if self.dino_jump:
            self.dino_rect.y -= self.gravity * 4
            self.gravity -=0.8
        if self.gravity < - self.GRAVITY:
            self.dino_jump = False
            self.gravity = self.GRAVITY
        #self.run()
        #pass

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    # def run(self):
        
    #     if self.step_index <5 :
    #         self.image = RUNNING[0]
    #     elif self.step_index >5:
    #         self.image = RUNNING[1]

    #     if self.step_index >10:
    #         self.step_index = 0
        
    #     self.step_index += 1
 
 
    # def custum (self,):
    #     if self.step_index <5 :
    #         self.image2 = self.image2[self.index_change][0] 
    #     elif self.step_index >5:
    #         self.image2 = self.image2[self.index_change][1]

    #     if self.step_index >10:
    #         self.step_index = 0
        
    #     self.step_index += 1
   


    # def event(self):
    #     pass

    # def ducking (self):
    #     if self.step_index <5 :
    #         self.image = DUCKING[0]
    #     elif self.step_index >5:
    #         self.image = DUCKING[1]

    #     if self.step_index >10:
    #         self.step_index = 0
        
    #     self.step_index += 1

    # def keys(self):
    #     # pass
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == K_DOWN:
    #                 self.image2[0]
    #                 return self.image2[0]
    #                 #self.index_change  = self.change[0]    
                    
    #             # elif event.key == K_UP:
    #             #     self.index_change  = self.change[0]    
    #             #     return self.index_changepass
            
    #         elif event.type == pygame.KEYUP:
    #             if event.key == K_DOWN:
    #                 self.image2[1]
    #                 return self.image2[1]
    #                 #self.index_change  = self.change[1]    
                    

    
                

        # self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        # self.dino_rect = self.image.get_rect()

        # self.dino_rect.x = self.X_POS
        # self.dino_rect.y = self.Y_POS

        # self.step_index += 1
        # self.image = RUNNING[0] 
        # if self.step_index <5 :
        #     self.dino_rect = self.image.get_rect()
        # else:
        #     self.dino_rect.x = self.X_POS
        #     self.dino_rect.y = self.Y_POS
        
        # self.step_index +=1
        



