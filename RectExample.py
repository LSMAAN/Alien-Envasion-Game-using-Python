import pygame, sys
from pygame.locals import *
import time

pygame.init()
FPS = 10 # frames per second setting
fpsClock = pygame.time.Clock()

# Set up the window
DISPLAYSURF = pygame.display.set_mode((600, 400), 0, 32)
pygame.display.set_caption('Test program for get_rect()')

WHITE = (255, 255, 255)

# Load two images
baseImg = pygame.image.load('images/ship.bmp')
spaceshipImg = pygame.image.load('images/Capture.bmp')

DISPLAYSURF.fill(WHITE)

# Place one image at the bottom of the screen
DISPLAYSURF.blit(baseImg, (300, 300))
pygame.display.update()

# Place the second image at the top of the screen
DISPLAYSURF.blit(spaceshipImg, (300, 0))
pygame.display.update()

# Wait for one second
time.sleep(1)

# Obtain the rectangle for each image
baseRect = baseImg.get_rect()
spaceshipRect = spaceshipImg.get_rect()

# This is where I believe I'm going wrong
# I understand this to obtain the x,y of the spaceship image
# Set the xy coordinates for the top image to the xy of the bottom image
spaceshipRect.x = baseRect.x
spaceshipRect.y = baseRect.y

# Move the top image to new xy position
# However this doesn't work
DISPLAYSURF.blit(spaceshipImg, (spaceshipRect.x, spaceshipRect.y))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
