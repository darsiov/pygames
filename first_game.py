from pygame import sprite   #Archivo especifico para animar los sprites
from pygame.locals import * #Gestion de eventos

import pygame
import sys

'''Todo lo que sea area, ancho o alto o coordenadas, tiene como medida el pixel'''
WIDTH_SCREEN, HEIGHT_SCREEN = 800, 800 
SPRITE_SIZE = 200 
MAX_FPS = 0.36 #Maximo del tiempo de espera del clock
SPEED_UP = 0.003
SPEED = 0.015
MOVE = 25
draw_point_w, draw_point_h =  0, 0 
x, y = 300, 600
width_sprite, height_sprite = 256, 64 #Tamaño del png completo
wallpaper = []  #Lista para acumular las coordenadas de los bloques del fondo  
c = 0
character = pygame.sprite.GroupSingle()#Grupo individual del sprite del personaje
wall_blocks = pygame.sprite.Group()#Grupo de sprites del fondo
window = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN)) #Creación de la ventana que mostrara nuestro juego
clock = pygame.time.Clock() #Definición del reloj interno del juego
dt = clock.tick(30) /100 #Definición de los FPS del surface

class Wall(sprite.Sprite):#Objeto que contendra el fondo

    def __init__(self):#Función que llevará la extracción , carga y conversión del sprite

        sprite.Sprite.__init__(self)
        self.spriteSheet = pygame.image.load('sprites/Fondo.png').convert_alpha()#Cargado del sprite
        self.image = pygame.transform.scale(self.spriteSheet.subsurface((0,0 ,width_sprite, height_sprite)),(0, 0)) #Transformación del png y definición de las medidas del sprite y del punto de coordenadas para dibujar el sprite
        self.rect = self.image.get_rect()#Necesario para mostrar la imagen
        self.rect.center = (draw_point_w, draw_point_h)#Definición de las coordenadas del sprite
        self.frames = 4 #Limite de frames
        self.current_frame = 0 #Frame actual
        self.frame_width = 64   #Ancho del frame
        self.frame_heigth = 64  #Alto del frame

    def update(self, dt, window):#Funcion del refresco del sprite

        if dt >= MAX_FPS:#Definición de maximo de fps
            dt = 0.33
        if self.current_frame >= self.frames - 0.1:
            self.current_frame = 0 
        else:
            self.current_frame += 0.01
 
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
        self.frames = 4 #Limite de frames
        self.current_frame = 0 #Frame actual
        self.frame_width = 64   #Ancho del frame
        self.frame_heigth = 64  #Alto del frame

    def update(self, dt, window):#Funcion del refresco del sprite

        if dt > MAX_FPS:#Definición de maximo de fps
            dt = 0.33
            
        if self.current_frame >= self.frames - 0.1:
            self.current_frame = 2 
        elif self.current_frame < 2:
            self.current_frame +=  SPEED_UP
        elif self.current_frame >= 2:
            self.current_frame +=  SPEED
        else:
            pass

        self.image = pygame.transform.scale(self.spriteSheet.subsurface((int(self.current_frame)*self.frame_width,0,self.frame_width,self.frame_heigth)),(SPRITE_SIZE,SPRITE_SIZE)) #Escala del sprite en el juego

    def movement(self, d):#Función de movimiento del personaje, d es el indicador de la dirección

        direction = d
            
        if direction == 2 and self.rect.centerx > -25:#↤ con respectivo limite
            self.rect.centerx -= MOVE

        if direction == 1 and self.rect.centerx < 625:#↦ con respectivo limite
            self.rect.centerx += MOVE

        if direction == 0 and self.rect.centery > -25:#↥ con respectivo limite
            self.rect.centery -= MOVE
    
        if direction == 3 and self.rect.centery < 600:#↧ con respectivo limite
            self.rect.centery += MOVE   

        if self.rect.centerx < 625 and self.rect.centery > -25:#Limite para ↗

            if direction == 0.5:#↗
                self.rect.centerx += MOVE
                self.rect.centery -= MOVE 

        if self.rect.centerx > -25 and self.rect.centery > -25:#Limite para ↖

            if direction == 1.5:#↖
                self.rect.centery -= MOVE
                self.rect.centerx -= MOVE

        if self.rect.centerx > -25 and self.rect.centery < 600: 

            if direction == 2.5:#↙
                self.rect.centery += MOVE
                self.rect.centerx -= MOVE
        if self.rect.centerx < 625 and self.rect.centery < 600:

            if direction == 3.5:#↘
                self.rect.centery += MOVE
                self.rect.centerx += MOVE

        else:#Evita errores en la conosola
            pass



def main():

    char = Character()#Asignamos la clase Character al grupo individual char
    
    while True: 
        
        for event in pygame.event.get():#Ciclo para detectar cualquier evento hecho por el usuario
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()#funcion que detecta cuando una tecla es pulsada o se mantiene pulsada

            if keys[K_w]:#↥
                d = 0
                if keys[K_d]:#↗
                    d = 0.5
                if keys[K_a]:#↖
                    d = 1.5
            elif keys[K_d]:#↦
                d = 1
                if keys[K_s]:#↙
                    d = 3.5
            elif keys[K_a]:#↤
                d = 2
                if keys[K_s]:#↙
                    d = 2.5
            elif keys[K_s]:#↧   
                d = 3
            elif keys[K_ESCAPE]:#Si presionas ESC podrás salir del programa, es practico para pruebass
                pygame.quit()
                sys.exit()
            else:#Asignamos d a cualquier número que no este anteriormente para evitar cualquier error en consola
                    d = -1

            char.movement(d)

        character.add(char)           
        wall_blocks.add(wallpaper)#Agregado de la lista al grupo de sprite
        wall_blocks.update(dt, window)#Invocación de la función del refresco de todos los sprites
        character.update(dt, window)
        window.fill((0, 0, 0))#Pantalla en negro
        wall_blocks.draw(window)
        character.draw(window)
        pygame.display.flip()


                

if __name__== '__main__':
    main()
