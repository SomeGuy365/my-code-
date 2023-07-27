import pygame
import random
import pygame.freetype
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HIGHT = 600
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HIGHT])
running = True

left = False
right = True
up = False
down = False

GAME_FONT = pygame.freetype.SysFont('arial',25)
fps = pygame.time.Clock()

fruit = [(random.randint(10,SCREEN_WIDTH-10)//10)*10,(random.randint(10,SCREEN_HIGHT-10)//10)*10]
pos = [400,300]
body = [[400,300],
        [350,300],
        [300,300]]

score = 0

while running:
    screen.fill((0,0,0))
    GAME_FONT.render_to(screen, (20, 20,20,20), "Score:"+str(score), (255, 255, 255))
    pygame.draw.rect(screen,(230, 12, 5),(fruit[0],fruit[1],10,10))
    for event in pygame.event.get():
        if event.type == QUIT:
                 running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                 running = False
            elif event.key == pygame.K_DOWN and up != True:
                 down = True
                 left = False
                 right = False
            if event.key == pygame.K_LEFT and right != True:
                 left = True
                 up = False
                 down = False
            if event.key == pygame.K_UP and down != True:
                 up = True
                 left = False
                 right = False
            if event.key == pygame.K_RIGHT and left != True:
                 right = True
                 up = False
                 down = False

    if up == True:
        pos[1] -= 10
    if down == True:
        pos[1] += 10
    if left == True:
        pos[0] -= 10
    if right == True:
        pos[0] += 10


    body.insert(0,list(pos))
    if pos[0] == fruit[0] and pos[1] == fruit[1]:
        fruit[0] = (random.randint(10,SCREEN_WIDTH-10)//10)*10
        fruit[1] = (random.randint(10,SCREEN_HIGHT-10)//10)*10
        score += 1
    else:
         body.pop()

    
    for i in body:
         pygame.draw.rect(screen,(200,200,200),(i[0],i[1],10,10))
         

    for block in body[1:]:
        if block[0] == pos[0] and block[1] == pos[1]:
              running = False

    if pos[0] < 0 or pos[0] > SCREEN_WIDTH:
         running = False
    elif pos[1] < 0 or pos[1] > SCREEN_HIGHT:
         running = False
    
    pygame.display.update()
    fps.tick(15)