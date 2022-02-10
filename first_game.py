from pygame import sprite   #Archivo especifico para animar los sprites
from pygame.locals import * #Gestion de eventos

import pygame
import sys
import random

'''Todo lo que sea area, ancho o alto o coordenadas, tiene como medida el pixel'''
WIDTH_SCREEN, HEIGHT_SCREEN = 800, 800 
SPRITE_SIZE = 200 
SPEED_UP = 0.05
SPEED = 0.1#Velocidad de la animación de la nave
MOVE = 10
FPS = 60
draw_point_w, draw_point_h =  0, 0 
x, y = 300, 600
random_limit = random.randint(1,5)
ax, ay = 0, 0
width_sprite, height_sprite = 256, 64 #Tamaño del png completo
wallpaper = []  #Lista para acumular las coordenadas de los bloques del fondo 
r_asteroid = [] #Lista para acumular los  asteroides aleatorios
c = 0
random.seed()
character = pygame.sprite.GroupSingle()#Grupo individual del sprite del personaje
asteroid = pygame.sprite.Group()
wall_blocks = pygame.sprite.Group()#Grupo de sprites del fondo
window = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN)) #Creación de la ventana que mostrara nuestro juego
pygame.display.set_caption(u'first game py')
clock = pygame.time.Clock() #Definición del reloj interno del juego

class Wall(sprite.Sprite):#Objeto que contendra el fondo

    def __init__(self):#Función que llevará la extracción , carga y conversión del sprite

        sprite.Sprite.__init__(self)
        self.spriteSheet = pygame.image.load('sprites/Fondo.png').convert_alpha()#Cargado del sprite
        self.image = pygame.transform.scale(self.spriteSheet.subsurface((0,0 ,width_sprite, height_sprite)),(0, 0)) #Transformación del png y definición de las medidas del sprite y del punto de coordenadas para dibujar el sprite
        self.rect = self.image.get_rect()#Necesario para mostrar la imagen
        self.rect.center = (draw_point_w, draw_point_h)#Definición de las coordenadas del sprite
        self.frames = 4 #Limite de frames del refresco del sprite
        self.current_frame = 0 #Frame actual0
        self.frame_width = 64   #Ancho del frame
        self.frame_heigth = 64  #Alto del frame

    def update(self, window):#Funcion del refresco del sprite

        if self.current_frame >= self.frames - 0.1:
            self.current_frame = 0 
        else:
            self.current_frame += 0.09
 
        self.image = pygame.transform.scale(self.spriteSheet.subsurface((int(self.current_frame)*self.frame_width,0,self.frame_width,self.frame_heigth)),(SPRITE_SIZE,SPRITE_SIZE)) #Escala del sprite en el juego


while True:#Ciclo para calcular las coordenadas de cada uno de los bloques del fondo

    if draw_point_w < 600 and draw_point_h <= 600:
        draw_point_w += SPRITE_SIZE
    elif draw_point_w == 600 and draw_point_h < 600:
        draw_point_w = 0
        draw_point_h += SPRITE_SIZE
    else:
        draw_point_w = 0
        draw_point_h = 0
    wallpaper.append(Wall())#Agragado de bloque
    c += 1
    if c > 15:
        break


class Character(sprite.Sprite):#Objeto que contendra el personaje

    def __init__(self):#Función que llevará la extracción , carga y conversión del sprite

        sprite.Sprite.__init__(self)
        self.spriteSheet = pygame.image.load('sprites/nave.png').convert_alpha()#Cargado del sprite transparente
        self.image = pygame.transform.scale(self.spriteSheet.subsurface((0,0 ,width_sprite, height_sprite)),(0, 0)) #Transformación del png y definición de las medidas del sprite y del punto de coordenadas para dibujar el sprite
        self.rect = self.image.get_rect()#Necesario para mostrar la imagen
        self.rect.center = (x, y)#Definición de las coordenadas del sprite
        self.frames = 4 #Limite de frames del refresco del sprite
        self.current_frame = 0 #Frame actual
        self.frame_width = 64   #Ancho del frame
        self.frame_heigth = 64  #Alto del frame

    def update(self, window):#Funcion del refresco del sprite
    
        if self.current_frame >= self.frames - 0.1:
            self.current_frame = 2 
        elif self.current_frame < 2:
            self.current_frame +=  SPEED_UP
        elif self.current_frame >= 2:
            self.current_frame +=  SPEED
        else:
            pass

        self.image = pygame.transform.scale(self.spriteSheet.subsurface((int(self.current_frame)*self.frame_width,0,self.frame_width,self.frame_heigth)),(SPRITE_SIZE,SPRITE_SIZE)) #Escala del sprite en el juego

    def movement(self):#Función de movimiento del personaje, d es el indicador de la dirección

        keys = pygame.key.get_pressed()
            
        if keys[K_a] and self.rect.centerx > -25:#↤ con respectivo limite

            self.rect.centerx -= MOVE
            
            if keys[K_s]:#↙

                if self.rect.centerx > -25 and self.rect.centery < 600:#Limite para ↙ 

                    self.rect.centery += MOVE/2
                    self.rect.centerx -= MOVE/2
            
        if keys[K_d] and self.rect.centerx < 625:#↦ con respectivo limite

            self.rect.centerx += MOVE
            
            if keys[K_s]:#↙
                if self.rect.centerx < 625 and self.rect.centery < 600:#Limite para ↘

                    self.rect.centery += MOVE/2
                    self.rect.centerx += MOVE/2
                
        if keys[K_w] and self.rect.centery > -25:#↥ con respectivo limite

            self.rect.centery -= MOVE

            if keys[K_d]:#↗
                if self.rect.centerx < 625 and self.rect.centery > -25:#Limite para ↗
                    self.rect.centerx += MOVE/2
                    self.rect.centery -= MOVE/2
            if keys[K_a]:#↖
                if self.rect.centerx > -25 and self.rect.centery > -25:#Limite para ↖
                    self.rect.centery -= MOVE/2
                    self.rect.centerx -= MOVE/2
    
        if keys[K_s] and self.rect.centery < 600:#↧ con respectivo limite
            self.rect.centery += MOVE   

        else:#Evita errores en la conosola
            pass


class Asteroide(sprite.Sprite):#Objeto que contendra el personaje

    def __init__(self):#Función que llevará la extracción , carga y conversión del sprite
        sprite.Sprite.__init__(self)
        self.spriteSheet = pygame.image.load('sprites/Asteroide.png').convert_alpha()#Cargado del sprite transparente
        self.image = pygame.transform.scale(self.spriteSheet.subsurface((0,0 ,width_sprite, height_sprite)),(0, 0)) #Transformación del png y definición de las medidas del sprite y del punto de coordenadas para dibujar el sprite
        self.rect = self.image.get_rect()#Necesario para mostrar la imagen
        self.rect.center = (ax, ay)#Definición de las coordenadas del sprite
        self.frames = 4 #Limite de frames del refresco del sprite
        self.current_frame = 0 #Frame actual
        self.frame_width = 64   #Ancho del frame
        self.frame_heigth = 64  #Alto del frame

    def update(self, window):#Funcion del refresco del sprite
    
        if self.current_frame >= self.frames - 0.1:
            self.current_frame = 2 
        elif self.current_frame < 2:
            self.current_frame +=  SPEED_UP
        elif self.current_frame >= 2:
            self.current_frame +=  SPEED
        else:
            pass
        
        self.image = pygame.transform.scale(self.spriteSheet.subsurface((int(self.current_frame)*self.frame_width,0,self.frame_width,self.frame_heigth)),(SPRITE_SIZE,SPRITE_SIZE)) #Escala del sprite en el juego


c = 0
while True:
    random_point = random.randint(-SPRITE_SIZE + 50, WIDTH_SCREEN - SPRITE_SIZE)
    if c >= random_limit:
        ax = -SPRITE_SIZE + 50
        ay = random_point
        r_asteroid.append(Asteroide())
        c += 1
    elif c < random_limit:
        ax = random_point
        ay = -SPRITE_SIZE + 50
        r_asteroid.append(Asteroide())
        c += 1
    if c >= random_limit*2:
        break

   
def main():

    char = Character()#Asignamos la clase Character al grupo individual char
    character.add(char)         
    wall_blocks.add(wallpaper)#Agregado de la lista al grupo de sprite
    asteroid.add(r_asteroid)
    while True:#Ciclo temporal de juego 

        clock.tick(FPS)

        for event in pygame.event.get():#Ciclo para detectar cualquier evento hecho por el usuario
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:#Si presionas ESC podrás salir del programa, es practico para pruebass
                pygame.quit()
                sys.exit()

        char.movement()#Movimiento del personaje
        wall_blocks.update(window)#Invocación de la función del refresco de todos los sprites
        character.update(window)
        asteroid.update(window)
        window.fill((0, 0, 0))#Pantalla en negro
        wall_blocks.draw(window)
        character.draw(window)
        asteroid.draw(window)
        pygame.display.flip()

                

if __name__== '__main__':
    main()
