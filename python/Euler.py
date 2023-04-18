import pygame 
import pygame.freetype
import random
import time

SCREEN_WIDTH = 800
SCREEN_HIGHT = 600

x = 400
y = 300

count = 0

width = 20
height = 20

burgerimg = pygame.image.load("pics/burger.jpg")
smaller_burger = pygame.transform.scale(burgerimg,(30,30))

smollyoshi = pygame.image.load("pics/perry.png")
smollyoshi = pygame.transform.scale(smollyoshi,(width,height))

def destroy():
    pygame.time.delay(5000)
    running = False

    return running

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HIGHT])

running = True 

xx = random.randint(0,SCREEN_WIDTH)
yy = random.randint(0,SCREEN_HIGHT) 

GAME_FONT = pygame.freetype.SysFont('arial',25)
clock = pygame.time.Clock()

transparent = (0,0,0,0)

pressed_up = False
pressed_right = False
pressed_left = False
pressed_down = False

while running:
    screen.fill((104, 235, 52))
    rect_ran = pygame.Rect(xx,yy,20,20)
    rect_play = pygame.Rect(x,y,width,height)
    pygame.draw.rect(screen,(0,0,0),rect_play)
    pygame.draw.rect(screen,(52, 189, 235),rect_ran)
    GAME_FONT.render_to(screen, (20, 20), "Count:"+str(count), (0, 0, 0))
    screen.blit(smaller_burger,(xx,yy))
    screen.blit(smollyoshi,(x,y))
    for event in pygame.event.get():
        if event.type == QUIT:
                 running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                 running = False
            if event.key == pygame.K_UP:
                pressed_up = True
            if event.key == pygame.K_LEFT:
                pressed_left = True 
            if event.key == pygame.K_RIGHT:
                pressed_right = True
            if event.key == pygame.K_DOWN:
                pressed_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                pressed_up = False
            if event.key == pygame.K_RIGHT:
                pressed_right = False
            if event.key == pygame.K_LEFT:
                pressed_left = False
            if event.key == pygame.K_DOWN:
                pressed_down = False
    if pressed_up == True:
        y -= 0.2
    if pressed_down == True:
        y += 0.2
    if pressed_left == True:
        x -= 0.2
    if pressed_right == True:
        x += 0.2
    if rect_play.colliderect( rect_ran ):
        width += 5
        height += 5
        smollyoshi = pygame.transform.scale(smollyoshi,(width,height))
        count += 1
        xx = random.randint(0,SCREEN_WIDTH)
        yy = random.randint(0,SCREEN_HIGHT)

    if count == 25:
        smollyoshi.fill(transparent)
        nuke = pygame.image.load("pics/nuke.jpg")
        nuke = pygame.transform.scale(nuke,(width,height))
        screen.blit(nuke,(x,y))
        pygame.display.update()
        pygame.time.delay(1000)
        running = False



    pygame.display.update()