#Snake en pygame

import pygame, random, sys, time
from math import sqrt
pygame.init()

###Screen###
size = (600,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")

fuente = pygame.font.Font(None, 50)
text = "Score: {}       High Score: {}"
limite = "_________________________________________________"

#fondo = pygame.image.load("Desktop\piso_feo.png")


###CONSTANTES###
delay = pygame.time.Clock()
i = 0 #Contador de pausas

###SERPIENTE###
##coordenadas##
cordx = 300
cordy = 300

###CUERPO SERPIENTE###
segmentos = []

###COMIDA###
#coordenadas
centerx = random.randint(10,570)
centery = random.randint(58,570)
radio = 10

###SCORE & HIGH SCORE###
score = 0
high_score = 0 

##Velocidad  de inicio
speedx = 0
speedy = 0

###MAIN WHILE###
run = True
while run:

    for event in pygame.event.get():
        print(event)        
        if event.type == pygame.QUIT:
            sys.exit()
        
        #Movimiento de la serpiente 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: #OJO que el movimiento de las teclas está invertido
                speedy = -5
                speedx = 0
            elif event.key == pygame.K_DOWN:
                speedy = 5
                speedx = 0 

            if event.key == pygame.K_LEFT:
                speedx = -5
                speedy = 0 
            elif event.key == pygame.K_RIGHT:
                speedx = 5
                speedy = 0
            
            if event.key == pygame.K_SPACE:
                i += 1
                speedx = 0
                speedx = 0
                if i == 2:
                    (cordx,cordy) = (300,300)
                    (speedx, speedy) = (0,0)
                    i = 0

            
    screen.fill("black")

    #screen.blit(fondo,(150,150))

        

    cordx += speedx
    cordy += speedy
    vector = (centerx-cordx+10, centery-cordy-10)
    magnitud = pygame.math.Vector2.distance_to(pygame.math.Vector2(centerx,centery), pygame.math.Vector2(cordx+10,cordy+10))
    totalseg = len(segmentos)
    #Colision con las paredes
    if (cordx > 580) or (cordx < 0) or (cordy > 580) or (cordy < 48):
        time.sleep(1)
        (cordx, cordy) = (300,300)
        speedx = 0
        speedy = 0
        score = 0 

    #Colisiones con la comida
    if (magnitud < 15):
        #Reposicion de la comida
        centerx = random.randint(10,570)
        centery = random.randint(58,570)

        #Cuerpo
        new_seg = (cordx, cordy)
        segmentos.append(new_seg)

        #Puntaje
        score += 1
        if score > high_score:
            high_score = score

    #Prueba de colisiones 
    pygame.draw.line(screen, "yellow",(cordx+10,cordy+10),(centerx,centery))

    #Dibujo de la serpiente qlia#
    pygame.draw.rect(screen, "green", (cordx, cordy, 20,20))

    for seg in range(totalseg-1, 0, -1):
        x,y = segmentos[seg-1]
        pygame.draw.rect(screen, "green3", (x, y, 20,20))

    if totalseg > 0:
        x,y = segmentos[0]
        pygame.draw.rect(screen, "green3", (x, y, 20,20))
        

    #Dibujo de la comida qlia#
    pygame.draw.circle(screen, "red", (centerx, centery), radio)
    
    mensaje = fuente.render(text.format(score, high_score), 1, "white")
    screen.blit(mensaje, (15, 10))
    limit = fuente.render(limite,1,"white")
    screen.blit(limit, (0, 15))
    
    #------#
    pygame.display.flip()
    delay.tick(30)