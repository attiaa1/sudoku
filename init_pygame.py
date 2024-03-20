import pygame

pygame.init()
pygame.font.init()

# display settings
window = pygame.display.set_mode((window_size,window_size))
window.fill((0, 0, 0))
pygame.display.set_caption("Sudoku")
icon = pygame.image.load("imgs/rubiks_cube.png")
pygame.display.set_icon(icon)
pygame.display.flip()