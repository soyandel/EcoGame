#Prueba de Drag and Drop

import pygame, random, sys
pygame.init()



###SCREEN###
size = (800,450)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Drag & Drop") #nombre de la ventana

###Bloques###
active_box = None
boxes = []
for i in range(5):
    x = random.randint(50,750)
    y = random.randint(50, 350)
    w = random.randint(35,65)
    h = random.randint(35,65)
    box = pygame.Rect(x, y, w, h)
    boxes.append(box)

run = True
while run:

    screen.fill("white")

    for box in boxes:
        pygame.draw.rect(screen,"black",box)

    for event in pygame.event.get(): 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num,box in enumerate(boxes):
                    if box.collidepoint(event.pos):
                        active_box = num

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_box = None

        if event.type == pygame.MOUSEMOTION:
            if active_box != None:
                boxes[active_box].move_ip(event.rel)

        if event.type == pygame.QUIT: 
            sys.exit() 

    pygame.display.flip()

