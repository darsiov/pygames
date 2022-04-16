from classes import *

import sys

clock = pygame.time.Clock() #Definición del reloj interno del juego

def main():

    char = Character()#Asignamos la clase Character al grupo individual char
    character.add(char)         
    wall_blocks.add(wallpaper)#Agregado de la lista al grupo de sprite
    asteroid.add(r_asteroid)
    
    while char.alive():#Ciclo de juego 

        clock.tick(FPS)
        
        for event in pygame.event.get():#Ciclo para detectar cualquier evento hecho por el usuario
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:#Si presionas ESC podrás salir del programa, es practico para pruebass
                pygame.quit()

        asteroid.add(r_asteroid)
        char.movement()#Movimiento del personaje
        wall_blocks.update(window)#Invocación de la función del refresco de todos los sprites
        character.update(window)
        asteroid.update(window)
        window.fill((0, 0, 0))#Pantalla en negro
        wall_blocks.draw(window)
        character.draw(window)
        asteroid.draw(window)
        pygame.display.flip()
        for i in r_asteroid:
            collision = pygame.sprite.collide_mask(char,i)
            if collision != None:
                char.kill()

                

if __name__== '__main__':
    main()
