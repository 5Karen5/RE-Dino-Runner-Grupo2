
import pygame
from dino_runner.utils.constants import CLOUD
from dino_runner.utils.constants import SCREEN_WIDTH
import random

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800,1000)
        self.y = random.randint(50,100)
        self.imagen = CLOUD
        self.width = self.imagen.get_width()



    def update(self,game):
        self.x -= game.game_speed
        if self.x < -self.width:
            self.x =SCREEN_WIDTH+ random.randint(2500,3000)
            self.y = random.randint(50,100)


    def draw(self, screen):
        screen.blit(self.imagen,(self.x,self.y))
