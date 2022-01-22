from email.mime import image
from tkinter import image_names
from traceback import print_tb
from pygame import sprite   #Archivo especifico para animar los sprites
from pygame.locals import * #Gestion de eventos

import pygame
import sys


def main():
    '''Todo lo que sea area, ancho o alto o coordenadas, tiene como medida el pixel'''
    WIDTH_SCREEN, HEIGHT_SCREEN = 800, 800 #Ancho y alto de la ventana
    SPRITE_SIZE = 200
    MAX_FPS = 0.35
    draw_point_w, draw_point_h =  0, 0 #Donde empezar a dibujar el sprite
    width_sprite, height_sprite = 256, 64 #Tamaño del png completo
    wallpaper = []  
    c = 0
    group_sprites = pygame.sprite.GroupSingle()
    window = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN)) #Creación de la ventana que mostrara nuestro juego
    clock = pygame.time.Clock() #Definición del reloj interno del juego
    dt = clock.tick(30) /100 #Definición de los FPS del surface
    
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
                self.current_frame += int(3*dt)

         
            self.image = pygame.transform.scale(self.spriteSheet.subsurface((int(self.current_frame)*self.frame_width,0,self.frame_width,self.frame_heigth)),(SPRITE_SIZE,SPRITE_SIZE)) #Escala del sprite en el juego


    while True:
        if draw_point_w < 600 and draw_point_h <= 600:
            draw_point_w += SPRITE_SIZE
        elif draw_point_w == 600 and draw_point_h < 600:
            draw_point_w = 0
            draw_point_h += SPRITE_SIZE
        else:
            draw_point_w = 0
            draw_point_h = 0
        wallpaper.append(Fondo())
        group_sprites.add(wallpaper[c])
        group_sprites.update(dt, window)
        window.fill((0, 0, 0))
        group_sprites.draw(window)
        pygame.display.flip()
        c += 1
        if 15 <= c:
            break


    while True:

        group_sprites.update(dt, window)
        window.fill((0, 0, 0))
        group_sprites.draw(window)
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

                

if __name__== '__main__':
    main()
