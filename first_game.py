import pygame
import ctypes
import sys

def main():
    user = ctypes.windll.user32
    user.SetProcessDPIAware()
    HEIGTH, HIGH = user32.GetSystemMetrics(0), user.GetSystemMetrics(1)
    window = pygame.display.set_mode((HEIGTH, HIGH))
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
     
    

if __name__== '__main__':
    main()
