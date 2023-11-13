#Snake#

###Librerias###
import turtle #Importa basicamente un eje de coordenadas x e y
import time
import random

###Constantes###
delay = 0.1

###Pantalla###
screen = turtle.Screen() #Define la pantalla
screen.setup(width = 600, height = 600) #Tamaño de la pantalla
#A su vez, 500 es la distacia total de la ventana, es decir, desde el punto (0,0), 
#se extiene -250 y 250 en el eje X
screen.tracer #idk est xd
screen.bgcolor("black") #Color del fondo


###Serpiente###
snake = turtle.Turtle() #define el objeto como algo movible(?)
snake.speed(0)
snake.shape("square") #forma
snake.color("green4") #color
snake.penup() #No deja rastro a medida q se mueve 
snake.goto(0,0) #parte del punto 0,0
snake.direction = "stop" #direccion en la que apunta la serpiente

###Segmentos / Cuerpo de la serpiente###
segmentos = [] #Para este caso, la mejor estructura de datos son las listas

###Marcador de puntos###
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle() #Para esconder la punta de la fleca (los objetos turtle son como flechas tipo vectores)
texto.goto(0,260)
texto.write("Score: 0       High Score: 0", align="center", font=("Courier", 24, "normal"))

linea = turtle.Turtle()
linea.speed(0)
linea.color("white")
linea.penup()
linea.hideturtle()
linea.goto(-300,240)
linea.write("_________________________________________________", align="left",font=("Courier",24,"normal"))

score = 0
high_score = 0

###Comida###
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


###Funciones###
def arriba(): #Cuando se usa la funcion, cambia la direccion de la serpiente
    snake.direction = "up"
def abajo():
    snake.direction = "down"
def derecha():
    snake.direction = "right"
def izquierda():
    snake.direction = "left"

def mov(): #Funcion Condicional que revisa el valor de snake.direction
    if snake.direction == "up": 
        y = snake.ycor() #Obtiene el valor de la coordenadas en Y y lo guarda en la variable y
        snake.sety(y + 20) #Reeposiciona a objeto snake en y+10 pixles
        #OJO que el .sety configura el valor en el eje Y

    if snake.direction == "down": 
        y = snake.ycor() 
        snake.sety(y - 20)

    if snake.direction == "right": 
        x = snake.xcor() 
        snake.setx(x + 20)
        #El .setx configura el valor en el eje X 

    if snake.direction == "left": 
        x = snake.xcor() 
        snake.setx(x - 20)

###Teclado###
screen.listen() #Le digo al programa que este atento a objeto externos
screen.onkeypress(arriba,"Up") #Le digo este atento al teclado
#En este caso le digo que ejecute la función arriba si presiono la tecla "Up" (Flecha arriba)
screen.onkeypress(abajo,"Down")
screen.onkeypress(derecha,"Right")
screen.onkeypress(izquierda,"Left")

###Bucle de esperar ordenes###
while True: #Bucle infinito hasta que reciba intrucciones
    ##Actualización de la pantalla##
    screen.update() 

    ##Colsiones con el borde##
    if (snake.xcor() > 280) or (snake.xcor() < -280) or (snake.ycor() > 220) or  (snake.ycor() < -280):
        time.sleep(1) 
        snake.goto(0,0)
        snake.direction = "stop"

        #Esconder los segmentos porque no sé como borrarlos XD#
        for segmento in segmentos:
            segmento.goto(2000,2000) #manda los segmentos fuera de la pantalla visible

        #Limpiar lista de segmentos#
        segmentos.clear() #limpia la lista

        #Resetea el marcador#
        score = 0
        texto.clear()#Limpia el texto
        texto.write("Score: {}       High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    ##Colisiones de la comida##
    if snake.distance(food) < 20: # el .distance(objeto) mide la distancia entre el objeto en el parentesis
        x = random.randint(-280,280) #Se otroga valores random enteros a variables x e y que posteriormente son asigandas al objeto comida
        y = random.randint(-280,220)
        food.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("green3")
        nuevo_segmento.penup()
        nuevo_segmento.goto(1000,1000)
        segmentos.append(nuevo_segmento)

        #aumentar marcador
        score += 1
        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Score: {}       High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
    
    ##Movimiento de los segmento tras la cabeza de snake##
    totalSeg = len(segmentos)
    for seg in range(totalSeg-1, 0, -1): #Se excluye el 0
        x = segmentos[seg-1].xcor() #Se extraen las coordenadas de la valor anterior en la lista, y se las agregan al siguiente, y así consecutivamente
        y = segmentos[seg-1].ycor() #Agregar que este ciclo for sigue las coordenadas del caso exclusivo
        segmentos[seg].goto(x,y)
    
    if totalSeg > 0: #Este es el caso exclusivo para cuando exista un valor en lista, el anterior ciclo for puede fallar si no existe un valor
        x = snake.xcor() #Se toman las coordenadas de la cabeza 
        y = snake.ycor()
        segmentos[0].goto(x,y)

    mov()

    ##Colisiones con el cuerpo##
    for segmento in segmentos:
        if segmento.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"

            #Esconder los segmentos#
            for segmento in segmentos:
                segmento.goto(2000,2000)

            #Limpiar lista de segmentos#
            segmentos.clear()

            score = 0
            texto.clear()
            texto.write("Score: {}       High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)