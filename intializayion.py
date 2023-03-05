import pygame

pygame.init()


SCREEN_SIZE: tuple = 500, 300  # width, height

screen = pygame.display.set_mode(SCREEN_SIZE)

is_window_open = True

while is_window_open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_window_open = False
