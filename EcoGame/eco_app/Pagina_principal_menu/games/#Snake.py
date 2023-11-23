#Snake#

import re
import pygame, random, sys, time, os
from pygame.math import Vector2

pygame.init()

###Screen###
size = (720,480)
screen = pygame.display.set_mode(size)

###Score###
score_text = pygame.font.SysFont("Russo One",15)


class Snake:
    #Se define como inicia la serpiente
    def __init__(self):
        self.body = [Vector2(10,100), Vector2(10,110), Vector2(10,120)]
        self.direction = Vector2(0,-10)
        self.add = False

    #Dibuja los cuerpos antes definidos
    def draw(self):
        for bloque in self.body:
            pygame.draw.rect(screen,"green",(bloque.x,bloque.y, 10,10))
    
    #Movimento de los cuerpos
    def move(self):
        if self.add == True:    
            body_copy = self.body
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]
            self.add = False
        else: 
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]

    #Movimiento con el teclado
    def move_up(self):
        self.direction = Vector2(0,-10)

    def move_down(self):
        self.direction = Vector2(0,10)

    def move_right(self):
        self.direction = Vector2(10,0)

    def move_left(self):
        self.direction = Vector2(-10,0)  

    #Si se le ocurre morir
    def die(self):
        if (self.body[0].x >= size[0]+1) or (self.body[0].y >= size[1]+1) or (self.body[0].x <= -1) or (self.body[0].y <= -1):
            return True
        
        #Colision con su propio cuerpo

        for i in self.body[1:]:
            if self.body[0] == i:
                return True
    


class Manzana:
    def __init__(self) -> None:
        self.generate() 

    def draw(self):
        pygame.draw.rect(screen, "red", (self.pos.x, self.pos.y, 10,10))

    def generate(self):
        self.x = random.randrange(0,size[0]/10)
        self.y = random.randrange(0,size[1]/10)
        self.pos = Vector2(self.x*10, self.y*10)

    def check_collision (self, snake):
        if snake.body[0] == self.pos:

            self.generate()
            snake.add = True

            return True
        
        for bloque in snake.body[1:]:
            if self.pos == bloque:
                self.generate()
        
        return False

def main():

    #Se le otorga la clase Snake a la variable snake
    snake = Snake()
    apple = Manzana()

    score = 0
    high_score = 0
    fps = clock = pygame.time.Clock()

    while True:

        fps.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            if event.type == pygame.KEYDOWN and snake.direction.y != 10:
                if event.key == pygame.K_UP:
                    snake.move_up()

            if event.type == pygame.KEYDOWN and snake.direction.y != -10:
                if event.key == pygame.K_DOWN:
                    snake.move_down()
            
            if event.type == pygame.KEYDOWN and snake.direction.x != -10:
                if event.key == pygame.K_RIGHT:
                    snake.move_right()
            
            if event.type == pygame.KEYDOWN and snake.direction.x != 10:
                if event.key == pygame.K_LEFT:
                    snake.move_left()




        screen.fill("black")
        snake.draw()
        apple.draw()

        snake.move()


        if snake.die():
            quit()

        if apple.check_collision(snake): 
            score =+ 1

        if score >= high_score:
            high_score = score
        
        text = score_text.render("Score: {}         High Score: {}".format(score, high_score),1,"white")
        screen.blit(text,(size[0]-text.get_width()-20,15))

        pygame.display.update()


main()