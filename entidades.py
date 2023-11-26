import pygame
import math

from view.Guemes import frames_guemes

class Actor(pygame.sprite.Sprite):
    def __init__(self, x, y, tiempo_actualizacion, speed=2,
                 frames_walk_up=None,
                 frames_walk_left_up=None,
                 frames_walk_right_up=None,
                 frames_walk_left=None,
                 frames_walk_right=None,
                 frames_walk_left_down=None,
                 frames_walk_down=None,
                 frames_walk_right_down=None,
                 frames_up=None,
                 frames_down=None,
                 frames_left=None,
                 frames_right=None):
        super().__init__()

        #motion
        self.FRAMES_WALK_UP = frames_walk_up
        self.FRAMES_WALK_LEFT_UP = frames_walk_left_up
        self.FRAMES_WALK_RIGH_UP = frames_walk_right_up
        self.FRAMES_WALK_LEFT = frames_walk_left
        self.FRAMES_WALK_RIGH = frames_walk_right
        self.FRAMES_WALK_LEFT_DOWN = frames_walk_left_down
        self.FRAMES_WALK_DOWN = frames_walk_down
        self.FRAMES_WALK_RIGH_DOWN = frames_walk_right_down

        #still
        self.FRAMES_UP = frames_up
        self.FRAMES_DOWN = frames_down
        self.FRAMES_LEFT = frames_left
        self.FRAMES_RIGHT = frames_right

        self.frames = self.FRAMES_WALK_DOWN
        self.current_frame = 0
        self.tiempo_actualizacion = tiempo_actualizacion
        self.tiempo_anterior = pygame.time.get_ticks()

        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.speed = speed
    
    def actualizar_animacion(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_anterior > self.tiempo_actualizacion:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.tiempo_anterior = tiempo_actual
    
    def mover_arriba(self):
        self.rect.y -= self.speed
        self.frames = self.FRAMES_WALK_UP

    def mover_derecha(self):
        self.rect.x += self.speed
        self.frames = self.FRAMES_WALK_RIGH

    def mover_abajo(self):
        self.rect.y += self.speed
        self.frames = self.FRAMES_WALK_DOWN

    def mover_izquierda(self):
        self.rect.x -= self.speed
        self.frames = self.FRAMES_WALK_LEFT
    
    def mover_arriba_izquierda(self):
        self.rect.x -= self.speed
        self.rect.y -= self.speed
        self.frames = self.FRAMES_WALK_LEFT_UP
    
    def mover_abajo_izquierda(self):
        self.rect.x -= self.speed
        self.rect.y += self.speed
        self.frames = self.FRAMES_WALK_LEFT_DOWN
    
    def mover_arriba_derecha(self):
        self.rect.x += self.speed
        self.rect.y -= self.speed
        self.frames = self.FRAMES_WALK_RIGH_UP
    
    def mover_abajo_derecha(self):
        self.rect.x += self.speed
        self.rect.y += self.speed
        self.frames = self.FRAMES_WALK_RIGH_DOWN
    
    def still_down(self):
        self.frames = self.FRAMES_DOWN
    
    def still_up(self):
        self.frames = self.FRAMES_UP
    
    def still_left(self):
        self.frames = self.FRAMES_LEFT
    
    def still_right(self):
        self.frames = self.FRAMES_RIGHT

class Guemes(Actor):
    def __init__(self, x, y, update_time, speed=2):
        super().__init__(x,y,update_time, speed=speed,
                         frames_walk_down=frames_guemes.FRAMES_WALK_DOWN,
                         frames_walk_left=frames_guemes.FRAMES_WALK_LEFT,
                         frames_walk_right=frames_guemes.FRAMES_WALK_RIGHT,
                         frames_walk_up=frames_guemes.FRAMES_WALK_UP,
                         frames_right=frames_guemes.FRAMES_RIGHT,
                         frames_left=frames_guemes.FRAMES_LEFT,
                         frames_up=frames_guemes.FRAMES_UP,
                         frames_down=frames_guemes.FRAMES_DOWN)

class Realista(Actor):
    def __init__(self, x, y, update_time, speed=1):
        super().__init__(x, y, 300, speed=speed,
                         frames_walk_down=frames_guemes.FRAMES_WALK_DOWN,
                         frames_walk_left=frames_guemes.FRAMES_WALK_LEFT,
                         frames_walk_right=frames_guemes.FRAMES_WALK_RIGHT,
                         frames_walk_up=frames_guemes.FRAMES_WALK_UP,
                         frames_right=frames_guemes.FRAMES_RIGHT,
                         frames_left=frames_guemes.FRAMES_LEFT,
                         frames_up=frames_guemes.FRAMES_UP,
                         frames_down=frames_guemes.FRAMES_DOWN)
    
    def move_to_enemy(self, enemy):
        enemyX, enemyY = enemy.rect.x, enemy.rect.y
        dx = enemyX - self.rect.x
        dy = enemyY - self.rect.y
        print(enemyX)
        print(self.rect.x)
        if enemyX > self.rect.x:
            dx += self.rect.width
        else:
            dx -= enemy.rect.width
        
        distance = math.hypot(dx, dy)
        print(f"distancia:{distance}")

        if distance!=0:
            dx, dy = dx/distance, dy/distance

        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed