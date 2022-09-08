import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH
class Obstacle(Sprite):
    def __init__(self,imagen,type):
        self.imagen = imagen
        self.type = type

        self.rect = self.imagen[self.type].get_rect()
        # self.rect.inflate_ip(-5,-5)
        # self.rect.topleft =(100,100)
        self.rect.x = SCREEN_WIDTH
        
    def update(self,game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self,screen):
        screen.blit(self.imagen[self.type], self.rect)