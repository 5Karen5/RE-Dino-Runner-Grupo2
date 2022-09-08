from dino_runner.components.heart import Heart
from dino_runner.utils.constants import HEART_COUNT


class PlayerHeartManager:
    def __init__(self):
        self.heart_count =HEART_COUNT


    def reduce_heart_count(self):
        self.heart_count -=1 
        # pass

    def draw(self, screen):
        x_position = 20
        y_position = 40

        for counter in range(self.heart_count):
            heart = Heart(x_position, y_position)
            heart.draw(screen)
            x_position += 30
            
