import pygame
from pygame.locals import *
from character import *
from maps import *
from animals import *

pygame.init()

char = Character()
maps = Maps()
objects = Objects()

clock = pygame.time.Clock()

while True:
    clock.tick(27)
    maps.screen.blit(maps.map1, (0,0))

    for house in objects.houses:
        char.collision(house)
    char.spriteSheetChar(maps.screen)
    char.walkingChar()
    animals = Horse()
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            break
        break
