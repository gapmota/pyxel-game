import pygame
from animals import *

class Character:
    def __init__(char):
        char.walkDown = [pygame.image.load('../images/character/human/short/humanFront1.png'),
                         pygame.image.load('../images/character/human/short/humanFront2.png'),
                         pygame.image.load('../images/character/human/short/humanFront3.png'),
                         pygame.image.load('../images/character/human/short/humanFront4.png')]
        
        char.walkUp = [pygame.image.load('../images/character/human/short/humanBack1.png'),
                      pygame.image.load('../images/character/human/short/humanBack2.png'),
                      pygame.image.load('../images/character/human/short/humanBack3.png'),
                      pygame.image.load('../images/character/human/short/humanBack4.png')]
        
        char.walkLeft = [pygame.image.load('../images/character/human/short/humanLeft1.png'),
                        pygame.image.load('../images/character/human/short/humanLeft2.png'),
                        pygame.image.load('../images/character/human/short/humanLeft3.png'),
                        pygame.image.load('../images/character/human/short/humanLeft4.png')]
        
        char.walkRight = [pygame.image.load('../images/character/human/short/humanRight2.png'),
                         pygame.image.load('../images/character/human/short/humanRight1.png'),
                         pygame.image.load('../images/character/human/short/humanRight4.png'),
                         pygame.image.load('../images/character/human/short/humanRight3.png')]
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
        elif keys[pygame.K_z]:
            print('Apertou z')
        else:
            char.walkCount = 0

    def spriteSheetChar(self,screen):
        if char.walkCount +1 >= 12:
            char.walkCount = 0
        if char.up:
            screen.blit(char.walkUp[char.walkCount//3],(char.x,char.y))
            char.walkCount += 1
        elif char.down:
            screen.blit(char.walkDown[char.walkCount//3],(char.x,char.y))
            char.walkCount += 1
        elif char.right:
            screen.blit(char.walkRight[char.walkCount//3],(char.x,char.y))
            char.walkCount += 1
        elif char.left:
            screen.blit(char.walkLeft[char.walkCount//3],(char.x,char.y))
            char.walkCount += 1
        else:
            screen.blit(char.walkRight[0],(char.x,char.y))
        
    def collision(self,houses):
        if char.up:
            if char.y <= houses.bottom and char.y >= houses.top and char.x <= houses.right and char.x >= houses.left:
                char.y = char.prevy
        elif char.down:
            if char.y <= houses.bottom and char.y >= houses.top and char.x <= houses.right and char.x >= houses.left:
                char.y = char.prevy
        elif char.right:
            if char.y <= houses.bottom and char.y >= houses.top and char.x <= houses.right and char.x >= houses.left:
                char.x = char.prevx
        elif char.left:
            if char.y <= houses.bottom and char.y >= houses.top and char.x <= houses.right and char.x >= houses.left:
                char.x = char.prevx

#Inicialização de classes
char = Character()
animals = Horse()
