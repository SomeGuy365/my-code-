import pygame
from pygame.locals import *
import sys
import random

x= 250
y= 250
vel = 5
width = 25
height = 50

pressed_up = False
pressed_right = False
pressed_left = False

SCREEN_WIDTH = 800
SCREEN_HIGHT = 600

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

clock = pygame.time.Clock()
jump_power = 20

def create_fruit(x,y):
    pygame.draw.rect(screen,(0,0,0),(x,y,50,50))
    running = 1
    return running


pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HIGHT])

running = True
runnin = 0

while running:
    clock.tick(60)
    screen.fill((250,250,250))
    rect1 = Rect(x,y,width,height)
    rect2 = Rect(0,550,800,50)
    grav = 5
    pygame.draw.rect(screen,(0,0,0),rect2)
    pygame.draw.rect(screen,(0,0,255),rect1)
    if runnin == 0:
        runnin = create_fruit(random.randint(100,SCREEN_WIDTH),10)
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
        elif event.type == KEYUP:
            if event.key == pygame.K_UP:
                pressed_up = False
            if event.key == pygame.K_RIGHT:
                pressed_right = False
            if event.key == pygame.K_LEFT:
                pressed_left = False

    if pressed_up:
        for i in range(jump_power):
            y+=-5
        pressed_up = False
    if pressed_left:
        x+=-vel
    if pressed_right:
        x+=vel
    y += grav

    if rect1.bottom == rect2.top:
        y-=grav

    pygame.display.update()
    

