from pygame import sprite   #Archivo especifico para animar los sprites
from pygame.locals import * #Gestion de eventos

import pygame
import sys


def main():
    '''Todo lo que sea area, ancho o alto o coordenadas, tiene como medida el pixel'''
    WIDTH_SCREEN, HEIGHT_SCREEN = 800, 800 #Ancho y alto de la ventana
    SPRITE_SIZE = 200
    CENTER = 600
    MAX_FPS = 35
    draw_point_w, draw_point_h =  1200, 1200 #Donde empezar a dibujar el sprite
    width_sprite, height_sprite = 256, 64 #Tamaño del png completo
    window = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN)) #Creación de la ventana que mostrara nuestro juego
    clock = pygame.time.Clock() #Definición del reloj interno del juego

    class Fondo(sprite.Sprite):#Objeto que contendra el fondo
        def __init__(self):#Función que llevará la extracción , carga y conversión del sprite
            sprite.Sprite.__init__(self)
            self.spriteSheet = pygame.image.load('sprites/Fondo.png')#Cargado del sprite

            self.image = pygame.transform.scale(self.spriteSheet.subsurface((0,0 ,width_sprite, height_sprite)),(draw_point_w, draw_point_h)) #Transformación del png y definición de las medidas del sprite y del punto de coordenadas para dibujar el sprite

            self.rect = self.image.get_rect()#Necesario para mostrar la imagen
            self.rect.center = (CENTER, CENTER)#Definición del centro de las coordenadas
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

        wallpaper = Fondo()
        group_sprites = pygame.sprite.GroupSingle()
        group_sprites.add(wallpaper)

        dt = clock.tick(30) /100 #Definición de los FPS del surface
        window.fill((0, 0, 0))
        group_sprites.update(dt, window)
        group_sprites.draw(window)
        pygame.display.flip()

        # if draw_point_w > 0 and draw_point_h >= 0:
        #     draw_point_w -= SPRITE_SIZE

        # elif draw_point_w == 0 and draw_point_h > 0:
        #     draw_point_w = 1200
        #     draw_point_h -= SPRITE_SIZE

        # else:
        #     draw_point_w = 1200
        #     draw_point_h = 1200
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()   
                

if __name__== '__main__':
    main()
