import pygame
from animals import *

class Character:
    def __init__(char):
        char.up = False
        char.down = False
        char.right = False
        char.left = False
        char.vel = 2.5
        char.walkCount = 0
        char.x = 20
        char.y = 280
        char.prevx = char.x
        char.prevy = char.y

    def walkingChar(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            char.prevy = char.y
            char.y -= char.vel
            char.up = True
            char.down = False
            char.right = False
            char.left = False
        elif keys[pygame.K_DOWN]:
            char.prevy = char.y
            char.y += char.vel
            char.up = False
            char.down = True
            char.right = False
            char.left = False
        elif keys[pygame.K_RIGHT]:
            char.prevx = char.x
            char.x += char.vel
            char.up = False
            char.down = False
            char.right = True
            char.left = False
        elif keys[pygame.K_LEFT]:
            char.prevx = char.x
            char.x -= char.vel
            char.up = False
            char.down = False
            char.right = False
            char.left = True
        else:
            char.walkCount = 0

    def spriteSheetChar(self,screen,skins):
        if char.walkCount +1 >= 12:
            char.walkCount = 0
        if char.up:
            screen.blit(skins.walkUp[char.walkCount//3],(char.x,char.y))
            char.walkCount += 1
        elif char.down:
            screen.blit(skins.walkDown[char.walkCount//3],(char.x,char.y))
            char.walkCount += 1
        elif char.right:
            screen.blit(skins.walkRight[char.walkCount//3],(char.x,char.y))
            char.walkCount += 1
        elif char.left:
            screen.blit(skins.walkLeft[char.walkCount//3],(char.x,char.y))
            char.walkCount += 1
        else:
            screen.blit(skins.walkRight[0],(char.x,char.y))
        
    def collision(self,general):
        if char.up:
            if char.y <= general.bottom and char.y >= general.top and char.x <= general.right and char.x >= general.left:
                char.y = char.prevy
        elif char.down:
            if char.y <= general.bottom and char.y >= general.top and char.x <= general.right and char.x >= general.left:
                char.y = char.prevy
        elif char.right:
            if char.y <= general.bottom and char.y >= general.top and char.x <= general.right and char.x >= general.left:
                char.x = char.prevx
        elif char.left:
            if char.y <= general.bottom and char.y >= general.top and char.x <= general.right and char.x >= general.left:
                char.x = char.prevx
                
#Inicialização de classes
char = Character()
