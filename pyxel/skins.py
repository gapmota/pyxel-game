import pygame
from character import *

class Skins:
    def __init__(skins):
        skins.stop = [pygame.image.load('../images/character/warriors/womanWR/left/warriorStopLeft1.png'),
                      pygame.image.load('../images/character/warriors/womanWR/right/warriorStopRight1.png')]

        skins.walkLeft = [pygame.image.load('../images/character/warriors/womanWR/left/warriorWalkLeft1.png'),
                          pygame.image.load('../images/character/warriors/womanWR/left/warriorWalkLeft2.png'),
                          pygame.image.load('../images/character/warriors/womanWR/left/warriorWalkLeft3.png'),
                          pygame.image.load('../images/character/warriors/womanWR/left/warriorWalkLeft4.png'),
                          pygame.image.load('../images/character/warriors/womanWR/left/warriorWalkLeft5.png'),
                          pygame.image.load('../images/character/warriors/womanWR/left/warriorWalkLeft6.png'),
                          pygame.image.load('../images/character/warriors/womanWR/left/warriorWalkLeft7.png'),
                          pygame.image.load('../images/character/warriors/womanWR/left/warriorWalkLeft8.png')]
    
        skins.walkRight = [pygame.image.load('../images/character/warriors/womanWR/right/warriorWalkRight1.png'),
                           pygame.image.load('../images/character/warriors/womanWR/right/warriorWalkRight2.png'),
                           pygame.image.load('../images/character/warriors/womanWR/right/warriorWalkRight3.png'),
                           pygame.image.load('../images/character/warriors/womanWR/right/warriorWalkRight4.png'),
                           pygame.image.load('../images/character/warriors/womanWR/right/warriorWalkRight5.png'),
                           pygame.image.load('../images/character/warriors/womanWR/right/warriorWalkRight6.png'),
                           pygame.image.load('../images/character/warriors/womanWR/right/warriorWalkRight7.png'),
                           pygame.image.load('../images/character/warriors/womanWR/right/warriorWalkRight8.png')]

        skins.fireLeft = [pygame.image.load('../images/character/warriors/womanWR/fire/fireLeft1.png'),
                          pygame.image.load('../images/character/warriors/womanWR/fire/fireLeft2.png'),
                          pygame.image.load('../images/character/warriors/womanWR/fire/fireLeft3.png'),
                          pygame.image.load('../images/character/warriors/womanWR/fire/fireLeft4.png'),
                          pygame.image.load('../images/character/warriors/womanWR/fire/fireLeft5.png')]

        skins.fireRight = [pygame.image.load('../images/character/warriors/womanWR/fire/fireRight1.png'),
                           pygame.image.load('../images/character/warriors/womanWR/fire/fireRight2.png'),
                           pygame.image.load('../images/character/warriors/womanWR/fire/fireRight3.png'),
                           pygame.image.load('../images/character/warriors/womanWR/fire/fireRight4.png'),
                           pygame.image.load('../images/character/warriors/womanWR/fire/fireRight5.png')]
        
#Inicialização de classes
skins = Skins()  
