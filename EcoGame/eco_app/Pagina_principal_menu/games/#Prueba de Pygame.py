#Prueba de Pygame

import pygame, sys, time
pygame.init() #Inicializar esta libreria, siempre se deben escribrir las dos anteriores lineas

###Definir colores###
BLACK   = (   0,   0,   0)
WHITE   = ( 255, 255, 255)
GREEN   = (   0, 255,   0)
RED     = ( 255,   0,   0)
BLUE    = (   0,   0, 255)

size = (800,500) #Variable en dupla del tamaño de la ventana

###Ventana###
screen =  pygame.display.set_mode(size) #Establece la pantalla en base a las variables dentro del set_mode()
delay = pygame.time.Clock() #Permite controlar los cuadros por segundo del juego

###Coordenadas del cubo
cordx = 100
cordy = 200

###Velocidad del cubo

speedx = 2
speedy = 2

###Main Bucle###
while True:
    for event in pygame.event.get(): #este for lo que hace registrar todo lo que está sucediendo en la ventana
        if event.type == pygame.QUIT: #Aqui compara si el evento es igual a cerrar la ventana (pygame.QUIT) 
            sys.exit() #Si es así, con este comando del sistema principal cierra la ventana
    
    if (cordx > 750) or (cordx < 0): #Estos if basicamente invierten la animación del cubo cada que choca con la esquina
        speedx *= -1 

    if (cordy > 450) or (cordy < 0):
        speedy *= -1

    screen.fill(BLACK) #Pintar pantalla (basicamente la cubeta de rellenar en paint kksks)

    cordx += speedx
    cordy += speedy
    ### --Zona de Dibujo(?)--##
    #pygame.draw.line(screen, BLACK, [400,250], [800,500], 5)
    #               lugar donde se va a dibujar, color, coordenada inicial, coordenada final, grosor 
    pygame.draw.rect(screen, RED, (cordx, cordy, 50,50))
    



    #---#
    pygame.display.flip() #Actualizar pantalla
    delay.tick(60)


