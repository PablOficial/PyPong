## importacion de las librerias
import pygame
from random import randint
BLACK = (0,0,0)

## esta clase define las pelotas en el juego
class Pelota(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()

        ## defino el color, el ancho y alto de la pelota
        ## (en negro para que sea transparente con respecto al fondo)
        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        ## dibujamos la propiedad rectangulo para la pelota (si, un rectangulo)
        pygame.draw.rect(self.image, color, [0,0,width, height])

        ## vamos a indicar una velocidad
        self.velocity = [randint(4,8), randint(-8,8)]

        ## Definimos el rectangulo de la pleota en funcion al objeto
        ## creado anteriormente
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)    
    
    def posicionInicial(self, width, height):
        self.rect.x = width
        self.rect.y = height

    def reiniciarVelocidades(self):
        self.velocity = [randint(4,8), randint(-8,8)]