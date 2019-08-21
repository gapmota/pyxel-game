import pygame

pygame.mixer.init()

class Maps:
    pygame.display.set_caption('Pyxel')
    def __init__(maps):
        maps.map1 = pygame.image.load('../images/maps/map2.png')
        maps.width = 800
        maps.height = 600
        maps.screen = pygame.display.set_mode((maps.width, maps.height))
        maps.music = pygame.mixer.music.load('../music/ambience.mp3')
        pygame.mixer.music.play(-1)

class Objects:
    def __init__(objects):
        objects.black = (0,0,0)
        objects.blue = (0,0,255)
        objects.general = [pygame.draw.rect(maps.screen, objects.blue,[-22,85,220,125],1)]

        objects.mount = [pygame.draw.rect(maps.screen, objects.blue,[383,305,50,70],1)]
        
#Inicialização de classes
maps = Maps()
objects = Objects()

