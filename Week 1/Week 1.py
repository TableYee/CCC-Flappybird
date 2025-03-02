#pip install pygame
import pygame
import random

"""
Initialises all the modules 
-> you have to initialise individual modules if you dont do this
"""
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
FPS = 60

#Constant Variables
BIRD_CIRC = 20 #Bird Radius

#Establish Colors
BACKGROUND = (0,0,255) # Blue
BIRD = (255,0,0)       # Red

screen.fill(BACKGROUND)
text = font.render(f"Score: 1", True, (255, 255, 100))
#gets text as a rectangluar box
text_box = text.get_rect()
#text's center coord = (1100,50)
text_box.center = (1100, 50)

running  = True
while running: 
    BIRD_X, BIRD_Y = world_w/4, world_h/2 
    
    #DRAWING BIRD Explain the position of the birdy
    pygame.draw.circle(screen, BIRD, (BIRD_X, BIRD_Y), BIRD_CIRC) 

    #computer graphics operation = draws the stuff at the position text_box
    screen.blit(text,text_box)

    pygame.display.update()
    clock.tick(FPS)