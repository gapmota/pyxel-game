import pygame
from pygame.locals import *
from character import *
from maps import *
from animals import *
from skins import *

pygame.init()

char = Character()
maps = Maps()
objects = Objects()

clock = pygame.time.Clock()

while True:
    clock.tick(27)
    maps.screen.blit(maps.map1, (0,0))

    char.spriteSheetChar(maps.screen,skins)
    char.walkingChar(maps.screen,skins) 
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)
            break
        break
