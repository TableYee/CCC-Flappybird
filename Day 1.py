#pip install pygame
import pygame
import random

pygame.init()

#setting screen size
world_w, world_h = 1200, 400
screen = pygame.display.set_mode((world_w, world_h))

#setting caption / title of the program
pygame.display.set_caption("Flappy Bird")

#Set up score counter
font = pygame.font.SysFont("Comic Sans", 32, True)

#Set up clock
clock = pygame.time.Clock()
FPS = 90

#Establish Colors
BACKGROUND = (0,0,255) # Blue
FLOOR = (0,0,0)        # Black
BIRD = (255,0,0)       # Red
PIPE = (0,255,0)       # Green

#
screen.fill(BACKGROUND)
text = font.render(f"Score: 1", True, (255, 255, 100))
text_box = text.get_rect()
text_box.center = (1100, 50)

#updating screen
#pygame.display.update()

#waiting for
clock.tick(FPS)

running  = True

while running: 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           running = False