from pygame import sprite
from pygame.locals import *

import pygame
import ctypes
import sys


def main():

    pygame.init()
    user = ctypes.windll.user
    user.SetProcessDPIAware()
    WIDTH, HEIGTH = user.GetSystemMetrics(0), user.GetSystemMetrics(1)
    window = pygame.display.set_mode((WIDTH, HEIGTH))
    clock = pygame.time.Clock()

    class Fondo(sprite.Sprite):
        def __init__(self):
            sprite.Sprite.__init__(self)
            self.spriteSheet = pygame.image.load('sprite/fondo.png')
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH/2, HEIGTH/2)

            self.frames = 4 
            self.current_frame = 0
            self.frame_width = 64
            self.frame_heigth = 64


        def update(self, dt, window):
            if self.current_frame >= self.frames-1:
                self.current_frame = 0 
            else:
                self.current_frame += 3*dt
    

    wallpaper = Fondo()
    group_sprites = pygame.sprite.GroupSingle()
    group_sprites.add(Fondo)

    while True:

        dt = clock.tick(30) /100

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()   

        window.fill(0, 0, 0)
        group_sprites.update(dt, window)
        group_sprites.draw(window)
        pygame.display.flip() 

     
    

if __name__== '__main__':
    main()
