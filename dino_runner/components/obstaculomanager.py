import pygame 
import random
from dino_runner.components.smallcactus import SmallCactus
from dino_runner.components.largecactus import LargeCatus
from dino_runner.components.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import BIRD


class Obstaclemanager:

    def __init__(self):
        self.obstacles = []
        self.tries = 5
        self.death_sound = pygame.mixer.Sound("dead.wav")
        
    
    def update(self,game):
        if len(self.obstacles) == 0:
            if random.randint(0,2) ==0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0,2) ==1:
                self.obstacles.append(LargeCatus(LARGE_CACTUS))
            elif random.randint(0,2) == 2:
                self.obstacles.append(Bird(BIRD))
        
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if(game.player.dino_rect.colliderect(obstacle.rect)) and not game.player.shield :
                self.tries -=1
                game.player_heart_manager.heart_count = self.tries
                # if  game.player.shield:
                #     self.obstacles.pop()
                # if not game.player.shield:
                #     pygame.time.delay(500)
                #     game.playing= False
                #     game.death_count+=1
                #     break
                # else:
                #     self.obstacles.remove(obstacle)
                if self.tries != 0 or game.player.shield :

                    self.obstacles.pop()
                    pygame.time.delay(100)
                elif self.tries <0 or not game.player.shield:

                
                    self.death_sound.play()
                    pygame.time.delay(1200)
                    game.playing = False
                    game.death_count +=1
                    self.tries = 6
                    
                    break
                    
                


        
    def draw(self, screen ):
        for obstacle in self.obstacles:
            obstacle.draw(screen)


