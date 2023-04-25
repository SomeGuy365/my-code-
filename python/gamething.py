import pygame
import random
import sys

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

x = SCREEN_WIDTH/2
y = 250

y1 = random.randint(1,SCREEN_HIGHT)
y2 = y1 + 150

xx = SCREEN_WIDTH-50

pressed_up = False
pressed_right = False
pressed_left = False
pressed_down = False

velocity = 0.15


while running:
    screen.fill((255,255,255))
    rect_play = pygame.Rect(x,y,20,20)
    rect_toptube = pygame.Rect(xx,0,60,y1)
    rect_bottomtube = pygame.Rect(xx,y2,60,SCREEN_HIGHT-y2)
    pygame.draw.rect(screen,(0,0,0),rect_play)
    pygame.draw.rect(screen,(10,10,10),rect_toptube)
    pygame.draw.rect(screen,(10,10,10),rect_bottomtube)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                y -= 75
                velocity = 0.0001
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                pressed_up = False

    if xx < -60:
        y1 = random.randint(200,SCREEN_HIGHT-400)
        y2 = y1 + 150
        xx = SCREEN_WIDTH

        rect_toptube = pygame.Rect(xx,0,60,y1)
        rect_bottomtube = pygame.Rect(xx,y2,60,SCREEN_HIGHT-y2)

    if y < -80 or y > SCREEN_HIGHT+20:
        print('ded')
        pygame.time.delay(5)
        running = False
    if rect_play.colliderect(rect_bottomtube) or rect_play.colliderect(rect_toptube):
            print('dedtube')
            pygame.time.delay(5)
            running = False

    y += velocity
    velocity += 0.0005
    xx -= 0.2
    pygame.display.update()