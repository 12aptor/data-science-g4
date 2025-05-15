import sys
import pygame
import time

ANCHO = 640
ALTO = 480
color_azul = (0, 0, 64)  # Color azul para el fondo.

pygame.init()
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
        #if self.rect.bottom >= ALTO or self.rect.top <= 0:
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= ANCHO or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        
        self.rect.move_ip(self.speed)
        
class Paleta(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('imagenes/paleta.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = (ANCHO -70,ALTO - 20)
        self.speed = [0,0]
        
    def update(self,evento):
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5,0]
        elif evento.key == pygame.K_RIGHT and self.rect.right < ANCHO:
            self.speed = [5,0]
        else:
            self.speed = [0,0]
            
        self.rect.move_ip(self.speed)
        
class Ladrillo(pygame.sprite.Sprite):
    
    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load('imagenes/ladrillo.png')
        # Obtener rectángulo de la imagen
        self.rect = self.image.get_rect()
        # Posición inicial, provista externamente.
        self.rect.topleft = posicion
        
        
class Muro(pygame.sprite.Group):
    
    def __init__(self,cantidad_ladrillos):
        pygame.sprite.Group.__init__(self)
        
        pos_x = 0
        pos_y = 0
        
        for i in range(cantidad_ladrillos):
            ladrillo = Ladrillo((pos_x,pos_y))
            self.add(ladrillo)
            
            pos_x += ladrillo.rect.width
            if pos_x >= ANCHO:
                pos_x = 0
                pos_y += ladrillo.rect.height
            
        
        


#########################################


pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("MI PRIMER VIDEOJUEGO")

reloj = pygame.time.Clock()
pygame.key.set_repeat(30)

############ OBJETOS DEL VIDEOJUEGO
bolita = Bolita()
jugador = Paleta()
muro = Muro(48)

#carga sonidos para videojuego
sonido_colision_paleta = pygame.mixer.Sound('sonidos/colision.ogg')
sonido_colision_muro = pygame.mixer.Sound('sonidos/colision_muro.ogg')
sonido_game_over = pygame.mixer.Sound('sonidos/game_over.ogg')

def juego_terminado():
    fuente = pygame.font.SysFont('Arial',72)
    texto = fuente.render('GAME OVER',True,(255,255,255))
    texto_rect = texto.get_rect()
    texto_rect.center = [ANCHO / 2, ALTO / 2]
    pantalla.blit(texto,texto_rect)
    pygame.display.flip()
    pygame.mixer.Sound.play(sonido_game_over)
    time.sleep(5)
    sys.exit()

while True:
    # ESTABLECEMOS LOS FRAMES POR SEGUNDO(FPS)
    reloj.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            jugador.update(evento)
            
    #actualizamos la posición de la bolita
    bolita.update()
    
    ###### colisiones
    if pygame.sprite.collide_rect(bolita,jugador):
        bolita.speed[1] = -bolita.speed[1]
        pygame.mixer.Sound.play(sonido_colision_paleta)
        
    lista_ladrillos_colision = pygame.sprite.spritecollide(bolita,muro,False)
    if lista_ladrillos_colision:
        ladrillo_colision = lista_ladrillos_colision[0]
        cx = bolita.rect.centerx
        if cx < ladrillo_colision.rect.left or cx > ladrillo_colision.rect.right:
            bolita.speed[0] = -bolita.speed[0]
        else:
            bolita.speed[1] = -bolita.speed[1]
        muro.remove(ladrillo_colision)
        pygame.mixer.Sound.play(sonido_colision_muro)
    
    if bolita.rect.top > ALTO:
        juego_terminado()
            
    # Rellenar la pantalla.
    pantalla.fill(color_azul)
    #dibujamos la bolita dentro de la pantalla
    pantalla.blit(bolita.image,bolita.rect)
    pantalla.blit(jugador.image,jugador.rect)
    muro.draw(pantalla)
            
    pygame.display.flip()