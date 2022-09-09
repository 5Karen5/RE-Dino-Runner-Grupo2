import pygame 
from dino_runner.utils.constants import SCREEN_WIDTH

FONT_STYLE = "freesansbold.ttf"
black_color = (0,0,0,0)

def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE,20)

    text = font.render('SCORE: '+ str (points), True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (900,70)
    
    return text, text_rect

def get_centered_message(message, widht = SCREEN_WIDTH//2, height = SCREEN_WIDTH//2):
    font = pygame.font.Font(FONT_STYLE,30)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center =(widht, height)

    return text, text_rect


def get_hight_score_element(hight_score):
    font = pygame.font.Font(FONT_STYLE,20)

    text = font.render('HIGHT_SCORE: '+ str (hight_score), True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (930,100)
    
    return text, text_rect
    