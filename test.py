import pygame

screen = pygame.display.set_mode((500, 500))
running  = True

while running: 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           running = False

    pygame.draw.circle(screen, (0,255,0), (500/3,500/3), 50) #BIRD
    pygame.display.update()