import pygame
import sys
from view.Guemes import frames_guemes

class MiSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = frames_guemes.FRAMES_DOWN[0]
        self.image.fill((255, 0, 0))  # Relleno rojo para el sprite (puedes usar una imagen en su lugar)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Visualizar Rectángulo")

# Crear un sprite
mi_sprite = MiSprite(100, 100, 50, 50)

# Crear un grupo para gestionar sprites
todos_los_sprites = pygame.sprite.Group()
todos_los_sprites.add(mi_sprite)

# Bucle principal
reloj = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpiar la pantalla
    pantalla.fill((255, 255, 255))

    # Dibujar el rectángulo del sprite en la pantalla
    pygame.draw.rect(pantalla, (0, 0, 255), mi_sprite.rect, 2)  # 2 es el grosor del borde

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    reloj.tick(60)
