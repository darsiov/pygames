from pygame import sprite   #Archivo especifico para animar los sprites
from pygame.locals import * #Gestion de eventos

import pygame
import sys


def main():
    '''Todo lo que sea area, ancho o alto o coordenadas, tiene como medida el pixel'''
    WIDTH_SCREEN, HEIGHT_SCREEN = 800, 800 #Ancho y alto de la ventana
    WALL_SIZE = 200 #Tamaño del fondo
    MAX_FPS = 0.35 #Maximo del tiempo de espera del clock
    draw_point_w, draw_point_h =  0, 0 #Donde empezar a dibujar el sprite
    width_sprite, height_sprite = 256, 64 #Tamaño del png completo
    wallpaper = []#Lista para acumular las coordenadas de los bloques del fondo  
    c = 0
    wall_blocks = pygame.sprite.Group()#Grupo de sprites del fondo
    window = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN)) #Creación de la ventana que mostrara nuestro juego
    clock = pygame.time.Clock() #Definición del reloj interno del juego
    dt = clock.tick(10) /100 #Definición de los FPS del surface
    
    class Fondo(sprite.Sprite):#Objeto que contendra el fondo
        def __init__(self):#Función que llevará la extracción , carga y conversión del sprite
            sprite.Sprite.__init__(self)
            self.spriteSheet = pygame.image.load('sprites/Fondo.png')#Cargado del sprite

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
            if self.current_frame >= self.frames - 1:
                self.current_frame = 0 
            else:
                self.current_frame += int(3.1*dt)

         
            self.image = pygame.transform.scale(self.spriteSheet.subsurface((int(self.current_frame)*self.frame_width,0,self.frame_width,self.frame_heigth)),(WALL_SIZE,WALL_SIZE)) #Escala del sprite en el juego

    while True:#Ciclo para calcular las coordenadas de cada uno de los bloques del fondo
        if draw_point_w < 600 and draw_point_h <= 600:
            draw_point_w += WALL_SIZE
        elif draw_point_w == 600 and draw_point_h < 600:
            draw_point_w = 0
            draw_point_h += WALL_SIZE
        else:
            draw_point_w = 0
            draw_point_h = 0
        wallpaper.append(Fondo())#Agragado de bloque
        c += 1
        if c > 15:
            break


    while True: 

        wall_blocks.add(wallpaper)#Agregado de la lista al grupo de sprite
        wall_blocks.update(dt, window)#Invocación de la función del refresco de todos los sprites
        window.fill((0, 0, 0))#Pantalla en negro
        wall_blocks.draw(window)#Refresco
        pygame.display.flip()

        for event in pygame.event.get():#Ciclo para detectar el cerrado del juego

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

                

if __name__== '__main__':
    main()
