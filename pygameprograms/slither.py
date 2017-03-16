import pygame
pygame.init()
gameDisplay = pygame.display.set_mode((800,400))
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        print(event)

