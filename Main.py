## importacion de las librerias
import pygame
from Paleta import Paleta
from Pelota import Pelota

## inicio de la instancia
pygame.init()

## declaracion de propiedades
BACKGROUND = (0,0,0)
WHITE      = (255,255,255)
size       = (800, 700)
screen     = pygame.display.set_mode(size)
pygame.display.set_caption("Pong game")

## creamos las paletas y su posicion inicial
paletaUno = Paleta(WHITE, 10, 60)
## posicion izquierda 
paletaUno.posicionIncial(80,300)


paletaDos = Paleta(WHITE, 10, 60)
## posicion derecha
paletaDos.posicionIncial(720,300)

## creamos la pelota
pelota = Pelota(WHITE, 15,15)
## posicion de inicio
pelota.posicionInicial(400,350)

## creamos una lista con todos los Sprites del juego
listaSprites = pygame.sprite.Group()
listaSprites.add(paletaUno)
listaSprites.add(paletaDos)
listaSprites.add(pelota)

## variables de ejecucion
run = True
##el reloj se utiliza para indicar cuan seguido se actualiza la pantalla
clock = pygame.time.Clock()

## variables de puntajes iniciales
puntajeUno = 0
puntajeDos = 0

def reiniciarPosiciones(): 
    paletaUno.posicionIncial(80,300) 
    paletaDos.posicionIncial(720,300)
    pelota.posicionInicial(400,350)
    pelota.reiniciarVelocidades()


## bucle de ejecucion
while run:
    ## validamos con un bucle for los eventos realizados por el usuario
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

        

    ## obtenemos los eventos segun las teclas presionadas
    ## y en funcion a ello determinamos que paleta se mueve
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: 
        paletaUno.moverArriba(10)
       
    if keys[pygame.K_s]:
        paletaUno.moverAbajo(10)

    if keys[pygame.K_UP]:
        paletaDos.moverArriba(10)

    if keys[pygame.K_DOWN]:
        paletaDos.moverAbajo(10)   
    
    
    ## aqui va a ir la logica del juego
    listaSprites.update()

    ## si la pelota llega a los limites de la pantalla, que rebote
    if pelota.rect.x>=800:
        puntajeUno +=1
        ##pelota.velocity[0] = -pelota.velocity[0]
        reiniciarPosiciones()

    if pelota.rect.x<=0:
        puntajeDos +=1
        ##pelota.velocity[0] = -pelota.velocity[0]
        reiniciarPosiciones()
    
    if pelota.rect.y>690:
       pelota.velocity[1] = -pelota.velocity[1]
       
    if pelota.rect.y<0:
        pelota.velocity[1] = -pelota.velocity[1]     

    ## si la pelota colisiona con uno de las paletas, que rebote
    if pygame.sprite.collide_mask(pelota, paletaUno) or pygame.sprite.collide_mask(pelota, paletaDos):
        pelota.bounce()

    ## colocamos el fondo 
    screen.fill(BACKGROUND)
    
    ## dibujamos la malla
    pygame.draw.line(screen, WHITE, [398,0], [398,700], 5)

    ## dibujamos todos los Sprites en pantalla
    listaSprites.draw(screen)

    ## mostrar los puntajes
    font = pygame.font.Font(None, 74)
    text = font.render(str(puntajeUno), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(puntajeDos), 1, WHITE)
    screen.blit(text, (420, 10))
    

    ## actualizamos la pantalla con lo que se dibuje
    pygame.display.flip()
    ## Frames per Second (FPS)
    clock.tick(60)

## el juego acaba
pygame.quit()