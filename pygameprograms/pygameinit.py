import pygame
import random
WIDTH = 360
HEIGHT = 400
FPS = 30
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLUE)
    pygame.display.flip()
pygame.quit()
