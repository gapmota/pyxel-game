import pygame
from character import *

class Skins:
    def __init__(skins):
        skins.walkDown = [pygame.image.load('../images/character/human/short/humanFront1.png'),
                         pygame.image.load('../images/character/human/short/humanFront2.png'),
                         pygame.image.load('../images/character/human/short/humanFront3.png'),
                         pygame.image.load('../images/character/human/short/humanFront4.png')]
    
        skins.walkUp = [pygame.image.load('../images/character/human/short/humanBack1.png'),
                        pygame.image.load('../images/character/human/short/humanBack2.png'),
                        pygame.image.load('../images/character/human/short/humanBack3.png'),
                        pygame.image.load('../images/character/human/short/humanBack4.png')]
        
        skins.walkLeft = [pygame.image.load('../images/character/human/short/humanLeft1.png'),
                         pygame.image.load('../images/character/human/short/humanLeft2.png'),
                         pygame.image.load('../images/character/human/short/humanLeft3.png'),
                         pygame.image.load('../images/character/human/short/humanLeft4.png')]
    
        skins.walkRight = [pygame.image.load('../images/character/human/short/humanRight2.png'),
                          pygame.image.load('../images/character/human/short/humanRight1.png'),
                          pygame.image.load('../images/character/human/short/humanRight4.png'),
                          pygame.image.load('../images/character/human/short/humanRight3.png')]

        skins.status = 1
    def interaction(self,mount):
            interact = pygame.key.get_pressed()
            dist = 3
            if interact[pygame.K_z]:
                if char.y <= mount.bottom + dist and char.y >= mount.top - dist and char.x <= mount.right + dist and char.x >= mount.left - dist:
                    if skins.status == 1:
                        skins.walkDown = [pygame.image.load('../images/character/knight/knightFront1.png'),
                                          pygame.image.load('../images/character/knight/knightFront2.png'),
                                          pygame.image.load('../images/character/knight/knightFront3.png'),
                                          pygame.image.load('../images/character/knight/knightFront4.png')]
                    
                        skins.walkUp = [pygame.image.load('../images/animals/modificated/horses/horseStop.png'),
                                        pygame.image.load('../images/animals/modificated/horses/horseStop.png'),
                                        pygame.image.load('../images/animals/modificated/horses/horseStop.png'),
                                        pygame.image.load('../images/animals/modificated/horses/horseStop.png')]
                        
                        skins.walkLeft = [pygame.image.load('../images/animals/modificated/horses/horseStop.png'),
                                          pygame.image.load('../images/animals/modificated/horses/horseStop.png'),
                                          pygame.image.load('../images/animals/modificated/horses/horseStop.png'),
                                          pygame.image.load('../images/animals/modificated/horses/horseStop.png')]
                    
                        skins.walkRight = [pygame.image.load('../images/animals/modificated/horses/horseStop.png'),
                                           pygame.image.load('../images/animals/modificated/horses/horseStop.png'),
                                           pygame.image.load('../images/animals/modificated/horses/horseStop.png'),
                                           pygame.image.load('../images/animals/modificated/horses/horseStop.png')]
                        skins.status = 0
                        pygame.time.delay(100)
                    elif skins.status == 0:
                        skins.walkDown = [pygame.image.load('../images/character/human/short/humanFront1.png'),
                                          pygame.image.load('../images/character/human/short/humanFront2.png'),
                                          pygame.image.load('../images/character/human/short/humanFront3.png'),
                                          pygame.image.load('../images/character/human/short/humanFront4.png')]

                        skins.walkUp = [pygame.image.load('../images/character/human/short/humanBack1.png'),
                                        pygame.image.load('../images/character/human/short/humanBack2.png'),
                                        pygame.image.load('../images/character/human/short/humanBack3.png'),
                                        pygame.image.load('../images/character/human/short/humanBack4.png')]

                        skins.walkLeft = [pygame.image.load('../images/character/human/short/humanLeft1.png'),
                                          pygame.image.load('../images/character/human/short/humanLeft2.png'),
                                          pygame.image.load('../images/character/human/short/humanLeft3.png'),
                                          pygame.image.load('../images/character/human/short/humanLeft4.png')]

                        skins.walkRight = [pygame.image.load('../images/character/human/short/humanRight2.png'),
                                           pygame.image.load('../images/character/human/short/humanRight1.png'),
                                           pygame.image.load('../images/character/human/short/humanRight4.png'),
                                           pygame.image.load('../images/character/human/short/humanRight3.png')]
                        skins.status = 1
                        pygame.time.delay(100)
                        
#Inicialização de classes
skins = Skins()

                    
