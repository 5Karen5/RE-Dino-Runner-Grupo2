import pygame 
from dino_runner.components.Obstaculo import Obstacle
import random 

class Bird(Obstacle):
    def __init__(self,imagen):
        self.type = 0
        super().__init__(imagen,self.type)
        self.rect.y = 250
        self.index =0

    def draw(self,screen):
        if self.index >=9:
            self.index =0

        screen.blit(self.imagen[self.index//5],self.rect)
        self.index +=1
