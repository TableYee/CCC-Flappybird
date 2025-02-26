import pygame
import random

class pipes():
    def __init__(self, height, width, is_top):
        self._width = width
        
        self._leftx = world_w
        self._rightx = world_w + width

        if is_top:
            self._topy = 0
            self._boty = height
        else:
            self._topy = height
            self._boty = world_h + 100

        self._height = self._boty - self._topy

    def shift(self, speed):
        self._leftx -= speed
        self._rightx -= speed

    def leftx(self):
        return self._leftx
    def rightx(self):
        return self._rightx

    def topy(self):
        return self._topy
    def boty(self):
        return self._boty

    def width(self):
        return self._width
    def height(self):
        return self._height

def spawn_pipe(pipe_gap):
    top_variable = random.randint(20, 235)  
    bot_variable = top_variable + pipe_gap
    pipe1 = pipes(top_variable, 60, True)
    pipe2 = pipes(bot_variable, 60, False)
    return pipe1, pipe2

def dies():
    dead = True
    while dead:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT):
                dead = False
                return True
            elif event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                return False

pygame.init()
running = True
paused = False

#Set up display
world_w, world_h = 1200, 400
screen = pygame.display.set_mode((world_w, world_h))
pygame.display.set_caption("Flappy Bird")

#Set up score counter
font = pygame.font.SysFont("Comic Sans", 32, True)

#Set up clock
clock = pygame.time.Clock()
FPS = 90

#State constant variables
SAFETY_ZONE = 6
GRAVITY = 10 #9.81
BIRD_F = 1.03  #Flap Strength
BIRD_CIRC = 17 #Bird Radius
FLOOR_HEIGHT = 20
BIRD_A = 0.04
pipe_gap = 125

#Establish Colors
BACKGROUND = (0,0,255) # Blue
FLOOR = (0,0,0)        # Black
BIRD = (255,0,0)       # Red
PIPE = (0,255,0)       # Green

while running:
    #State changing variables
    BIRD_V = 1    #Vertical Velocity
    BIRD_H = 2.25    #Horizontal Velocity

    BIRD_X, BIRD_Y = world_w/3 - BIRD_CIRC, world_h/2 - BIRD_CIRC

    PIPE_DIST = 0 #How far apart pipes are
    PIPES = []    #List of pipes

    #State conditionals
    score = 0
    score_prevent = 0
    alive = True

    # Handle events
    while alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                running = False
                alive = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                BIRD_V = BIRD_F
            
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT):
                paused = True

        #Draw Background before handling pipes
        screen.fill(BACKGROUND)

        #Apply gravity and accelerate bird
        BIRD_V -= GRAVITY / 300

        BIRD_Y -= BIRD_V * 4

        if BIRD_Y + BIRD_CIRC - SAFETY_ZONE >= world_h - FLOOR_HEIGHT + 0.1: #0.1 delays the collision by 1 fram
            alive = False
            running = dies()
        elif BIRD_Y + BIRD_CIRC + SAFETY_ZONE <= 10:
            alive = False
            running = dies()

        if PIPE_DIST <= 0:
            pipe1, pipe2 = spawn_pipe(pipe_gap)
            PIPES.append(pipe1)
            PIPES.append(pipe2)
            PIPE_DIST = 200 - 22*BIRD_H ####Original: 100 - 1.5 * BIRD_H

        #Collision detection
        for pipe in PIPES:
            pipe.shift(BIRD_H)
        
        for pipe in PIPES: #For some reason when the loop runs once (Which makes complete sense) the first and every other pipe shifts to the right by one frame after the bird flies through it (Which makes no sense). I don't know.
            # if bird_x is in pipe
            if (pipe.leftx() <= BIRD_X + BIRD_CIRC - SAFETY_ZONE <= pipe.rightx() ) or ( pipe.leftx() <= BIRD_X - BIRD_CIRC + SAFETY_ZONE <= pipe.rightx() ):
                # if bird_y is in pipe 
                if (pipe.topy() <= BIRD_Y - BIRD_CIRC + SAFETY_ZONE <= pipe.boty() ) or ( pipe.topy() <= BIRD_Y + BIRD_CIRC - SAFETY_ZONE <= pipe.boty() ):
                    alive = False
                    running = dies()
                elif score_prevent <= 0:
                    score_prevent = 40
                    score += 1
                    BIRD_H += BIRD_A

            # if pipe is off screen
            if pipe.rightx() <= 0:
                PIPES.remove(pipe)
            
            pygame.draw.rect(screen, PIPE, (pipe.leftx(), pipe.topy(), pipe.width(), pipe.height()))

        text = font.render(f"Score: {score}", True, (255, 255, 100))
        text_box = text.get_rect()
        text_box.center = (1100, 50)
        
        # Draw objects
        pygame.draw.circle(screen, BIRD, (BIRD_X, BIRD_Y), BIRD_CIRC) #BIRD
        pygame.draw.rect(screen, FLOOR, (0, world_h - FLOOR_HEIGHT, world_w, FLOOR_HEIGHT))
        screen.blit(text,text_box)

        PIPE_DIST -= 1
        score_prevent -= 1
        pygame.display.update()
        clock.tick(FPS)

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    alive = False
                    running = False
                elif event.type == pygame.KEYDOWN and (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT or event.key == pygame.K_SPACE):
                    paused = False