import pygame
from animals import *

class Character:
    def __init__(char):
        char.right = False
        char.left = False
        char.lastDirection = 'right'
        char.vel = 3.5
        char.walkCount = 0
        char.countAux = 0
        char.x = 0
        char.y = 450
        char.prevx = char.x
        char.prevy = char.y

    def walkingChar(self, screen,skins):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            char.prevx = char.x
            char.x += char.vel
            char.right = True
            char.left = False
            char.lastDirection = 'right'
        elif keys[pygame.K_LEFT]:
            char.prevx = char.x
            char.x -= char.vel
            char.left = True
            char.right = False
            char.lastDirection = 'left'
        elif keys[pygame.K_z] and char.lastDirection ==  'left':
            char.right = False
            char.left = False
            char.countAux = 0
            while char.countAux +1 <= 15:
                screen.blit(skins.fireLeft[char.countAux//3],(char.x-8,char.y))
                pygame.display.flip()
                char.countAux += 1
                maps.screen.blit(maps.map1, (0,0))
            screen.blit(skins.fireLeft[0],(char.x-8,char.y))
                
        elif keys[pygame.K_z] and char.lastDirection ==  'right':
            char.right = False
            char.left = False
            char.countAux = 0
            while char.countAux +1 <= 15:
                screen.blit(skins.fireRight[char.countAux//3],(char.x+8,char.y))
                pygame.display.flip()
                char.countAux += 1
                maps.screen.blit(maps.map1, (0,0))
            screen.blit(skins.fireRight[0],(char.x+8,char.y))
        else:
            char.right = False
            char.left = False
            if char.lastDirection == 'left':
                screen.blit(skins.stop[0],(char.x,char.y))
            elif char.lastDirection == 'right':
                screen.blit(skins.stop[1],(char.x,char.y))
            
            
    def spriteSheetChar(self,screen,skins):
        if char.walkCount +1 >= 40:
            char.walkCount = 0
        elif char.right:
            screen.blit(skins.walkRight[char.walkCount//5],(char.x,char.y))
            char.walkCount += 1
        elif char.left:
            screen.blit(skins.walkLeft[char.walkCount//5],(char.x,char.y))
            char.walkCount += 1
                  
    def collision(self,general):
        if char.right:
            if char.y <= general.bottom and char.y >= general.top and char.x <= general.right and char.x >= general.left:
                char.x = char.prevx
        elif char.left:
            if char.y <= general.bottom and char.y >= general.top and char.x <= general.right and char.x >= general.left:
                char.x = char.prevx
        
#Inicialização de classes
char = Character()

