import pygame 
from dino_runner.components.Obstaculo import Obstacle
import random 

class SmallCactus(Obstacle):
    def __init__(self,imagen):
        self.type = random.randint(0,2)
        super().__init__(imagen,self.type)
        self.rect.y= 320
        
