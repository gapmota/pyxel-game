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
    
    for general in objects.general:
        char.collision(general)
        
    for mount in objects.mount:
        skins.interaction(mount)
    
    char.spriteSheetChar(maps.screen,skins)
    char.walkingChar()
    animals = Horse()        
    
    pygame.display.update()
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            break
        break
