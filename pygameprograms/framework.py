import pygame
pygame.init()
col = (25,55,55)
red = (255,0,0)
black =(0,0,0)
gameDisplay = pygame.display.set_mode((800,400))
pygame.display.set_caption("Slither")

gameExit = False

while not gameExit :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
          


pygame.quit()

