import sys
import pygame

ANCHO = 640
ALTO = 480

pantalla = pygame.display.set_mode((ANCHO,ALTO))

pygame.display.set_caption("MI PRIMER VIDEOJUEGO")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
            
    pygame.display.flip()