## importacion de las librerias
import pygame
import random
BLACK = (0,0,0)

## esta clase contendra los Sprites de las paletas
class Paleta(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        ## defino el color, el ancho y alto de la paleta 
        ## (en negro para que sea transparente con respecto al fondo)
        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        ## Dibujamos una propiedad rectangulo
        pygame.draw.rect(self.image, color, [0,0,width, height])

        ## Definimos el rectangulo de la paleta en funcion al objeto
        ## creado anteriormente
        self.rect = self.image.get_rect()

    
    def moverArriba(self, speed):
        self.rect.y -= speed
        ## validamos que no salgamos de la pantalla
        if self.rect.y < 0:
            self.rect.y = 0    

    
    def moverAbajo(self, speed):
        self.rect.y += speed
        ## validamos que no salgamos de la pantalla
        if self.rect.y > 600:
            self.rect.y = 600 

    def posicionIncial(self, width, height):
        self.rect.x = width
        self.rect.y = height