import pygame

# Inicializa Pygame
pygame.init()

class MiSprite(pygame.sprite.Sprite):
    def __init__(self, imagen):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()

# Crea un objeto de la clase MiSprite
sprite = MiSprite('view/Guemes/down_1.png')

# Crea una ventana
win = pygame.display.set_mode((500, 500))

# Dibuja el sprite y su cuadro de colisión
win.blit(sprite.image, (50, 50))  # Dibuja el sprite
pygame.draw.rect(win, (255, 0, 0), sprite.rect, 2)  # Dibuja el cuadro de colisión

# Actualiza la pantalla
pygame.display.flip()
