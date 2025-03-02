import pygame

"""
Initialises all the modules 
-> you have to initialise individual modules if you dont do this
"""
pygame.init()

screen = pygame.display.set_mode((500, 500))
running  = True

font = pygame.font.SysFont("Comic Sans", 32, True)
text = font.render(f"Score: 1", True, (255, 255, 100))
text_box = text.get_rect()
text_box.center = (50, 50)

while running: 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           running = False

    pygame.draw.circle(screen, (0,255,0), (500/3,500/3), 50) #BIRD
    pygame.display.update()

    screen.blit(text,text_box)