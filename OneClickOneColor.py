import pygame
import random

#Screen
pygame.init()

ScreenWidth = 1280
ScreenHeight = 720

screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))
pygame.display.set_caption("Flappy")

#Colors

background_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
screen.fill(background_colour)
pygame.display.flip()

#Font

font = pygame.font.SysFont("MicrosoftTaiLe.ttf", 72)
img1 = font.render('Click for more colors', True, (255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONUP:
            background_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            screen.fill(background_colour)
    
        if event.type == pygame.K_SPACE:
            background_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            screen.fill(background_colour)

    screen.blit(img1, (400, 300))
    pygame.display.update()
