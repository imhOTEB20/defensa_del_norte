import pygame
import sys

import random

from entidades import Guemes
from entidades import Realista
from view.Guemes import frames_guemes
# Inicializar Pygame
pygame.init()

# Definir colores
blanco = (255, 255, 255)

# Configuración de la pantalla
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Animación de Sprites")

# Crear un grupo para gestionar sprites
todos_los_sprites = pygame.sprite.Group()

# Crear varios sprites con animaciones y tiempos de actualización distintos

player = Guemes(300, 100, 100)
enemy1 = Realista(100, 100, 200)

todos_los_sprites.add(player)
todos_los_sprites.add(enemy1)

# Bucle principal
reloj = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYUP and evento.type != pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                player.still_down()
            elif evento.key == pygame.K_UP:
                player.still_up()
            elif evento.key == pygame.K_LEFT:
                player.still_left()
            elif evento.key == pygame.K_RIGHT:
                player.still_right()
    
    keys = pygame.key.get_pressed()
    enemy1.move_to_enemy(player)
    if keys[pygame.K_LEFT]:
        player.mover_izquierda()
    if keys[pygame.K_RIGHT]:
        player.mover_derecha()
    if keys[pygame.K_UP]:
        player.mover_arriba()
    if keys[pygame.K_DOWN]:
        player.mover_abajo()

    # Actualizar animaciones y mover sprites
    for sprite in todos_los_sprites:
        sprite.actualizar_animacion()

    # Limpiar la pantalla
    pantalla.fill(blanco)

    # Dibujar todos los sprites en la pantalla
    todos_los_sprites.draw(pantalla)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    reloj.tick(60)  # Establecer el límite de FPS en 60