import pygame
pygame.init()
gameDisplay = pygame.display.set_mode((800,400))
pygame.display.set_caption("Slither")
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
lead_x = 400
lead_y = 200
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x = lead_x - 25
            if event.key == pygame.K_RIGHT:
                lead_x = lead_x + 25
        
    gameDisplay.fill(blue)
    pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,25,25])
    pygame.display.update()
pygame.quit()

