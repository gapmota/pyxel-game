import pygame
from maps import *

class Horse:
    def __init__(horse): 
        horse.stop = [pygame.image.load('../images/animals/modificated/horses/horseStop.png')]

        horse.x = 410
        horse.y = 340
        
        maps.screen.blit(horse.stop[0],(horse.x,horse.y))
