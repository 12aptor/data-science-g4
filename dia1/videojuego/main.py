import sys
import pygame

ANCHO = 640
ALTO = 480
color_azul = (0, 0, 64)  # Color azul para el fondo.

######## CLASES #############################
class Bolita(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #cargamos imagen del Sprite
        self.image = pygame.image.load('imagenes/bolita.png')
        #creamos un rectangulo para contener la bolita
        self.rect = self.image.get_rect()
        #dibujamos la bolita en el centro de la pantalla
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2
        
        self.speed = [3,3]
        
    def update(self):
        if self.rect.bottom >= ALTO or self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= ANCHO or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        
        self.rect.move_ip(self.speed)
        
        


#########################################


pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("MI PRIMER VIDEOJUEGO")

reloj = pygame.time.Clock()

############ OBJETOS DEL VIDEOJUEGO
bolita = Bolita()



while True:
    # ESTABLECEMOS LOS FRAMES POR SEGUNDO(FPS)
    reloj.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
            
    #actualizamos la posición de la bolita
    bolita.update()
            
    # Rellenar la pantalla.
    pantalla.fill(color_azul)
    #dibujamos la bolita dentro de la pantalla
    pantalla.blit(bolita.image,bolita.rect)
            
    pygame.display.flip()