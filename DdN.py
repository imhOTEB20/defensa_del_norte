import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAY = pygame.display.set_mode((1024, 800))
pygame.display.set_caption("Defensa del Norte.")

DISPLAY.fill("WHITE")
run = True

#BUCLE PRINCIPAL DEL JUEGO
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            pygame.quit()
            sys.exit()
        
        pygame.display.update()

#