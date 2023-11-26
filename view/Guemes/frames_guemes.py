import pygame

#motion:

FRAMES_WALK_UP = [pygame.image.load(f"view/Guemes/walk_up_{i}.png") for i in range(1,9)]
#FRAMES_WALK_LEFT_UP = [pygame.image.load(f"view/Guemes/walk_left_up_{i}.png") for i in range(1,8)]
FRAMES_WALK_LEFT = [pygame.image.load(f"view/Guemes/walk_left_{i}.png") for i in range(1,9)]
#FRAME_WALK_LEFT_DOWN = [pygame.image.load(f"view/Guemes/walk_left_down_{i}.png") for i in range(1,8)]
FRAMES_WALK_DOWN = [pygame.image.load(f"view/Guemes/walk_down_{i}.png") for i in range(1,9)]
#FRAMES_WALK_DOWN_RIGHT = [pygame.image.load(f"view/Guemes/walk_down_right_{i}.png") for i in range(1,8)]
FRAMES_WALK_RIGHT = [pygame.image.load(f"view/Guemes/walk_right_{i}.png") for i in range(1,9)]
#FRAMES_WALK_RIGHT_UP = [pygame.image.load(f"view/Guemes/walk_right_up_{i}.png") for i in range(1,8)]

#still:
FRAMES_UP = [pygame.image.load(f"view/Guemes/up_{i}.png") for i in range(1,4)]
FRAMES_DOWN = [pygame.image.load(f"view/Guemes/down_{i}.png") for i in range(1,4)]
FRAMES_LEFT = [pygame.image.load(f"view/Guemes/left_{i}.png") for i in range(1,4)]
FRAMES_RIGHT = [pygame.image.load(f"view/Guemes/right_{i}.png") for i in range(1,4)]