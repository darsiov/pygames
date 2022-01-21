from pygame import sprite
from pygame.locals import *

import pygame
import ctypes
import sys


def main():

    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    WIDTH, HEIGTH = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    window = pygame.display.set_mode((WIDTH, HEIGTH))
    clock = pygame.time.Clock()

    class Fondo(sprite.Sprite):
        def __init__(self):
            sprite.Sprite.__init__(self)
            self.spriteSheet = pygame.image.load('sprites/Fondo.png').convert_alpha()
            self.image = pygame.transform.scale(self.spriteSheet.subsurface((0,0,256,64)),(WIDTH-1, HEIGTH-1))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH/2, HEIGTH/2)

            self.frames = 4 #Limite de frames
            self.current_frame = 0 #Frame actual
            self.frame_width = 64   #Ancho del frame
            self.frame_heigth = 64  #Alto del frame


        def update(self, dt, window):
            if dt >= 0.35:
                dt = 0.33
            if self.current_frame >= self.frames - 1:
                self.current_frame = 0 
            else:
                self.current_frame += int(3*dt)
                print(str(self.current_frame)+' Frame actual del sprite')

            self.image = pygame.transform.scale(self.spriteSheet.subsurface((int(self.current_frame)*self.frame_width,0,64,64)),(400,400))
    

    wallpaper = Fondo()
    group_sprites = pygame.sprite.GroupSingle()
    group_sprites.add(wallpaper)

    while True:

        dt = clock.tick(30) /100 #Hz
        window.fill((0, 0, 0))
        group_sprites.update(dt, window)
        group_sprites.draw(window)
        print(str(dt) + ' Frames' )
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()   
                

        

     
    

if __name__== '__main__':
    main()
