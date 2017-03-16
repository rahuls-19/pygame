import pygame
pygame.init()
gameDisplay = pygame.display.set_mode((800,400))
pygame.display.set_caption("Slither")
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    gameDisplay.fill(blue)
    pygame.draw.rect(gameDisplay,black,[400,200,25,25])
    pygame.display.update()
pygame.quit()

