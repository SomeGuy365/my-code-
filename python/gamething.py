import pygame
import random
import sys
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

x = SCREEN_WIDTH/2
y = 250

y1 = random.randint(1,SCREEN_HIGHT-80)
y2 = y1 + 250

xx = SCREEN_WIDTH-50

pressed_up = False
pressed_right = False
pressed_left = False
pressed_down = False

velocity = 0.15
score = 0

GAME_FONT = pygame.freetype.SysFont('arial',25)

spriteplay = pygame.image.load('C:\\Users\\ethan\\.vscode\\cool\\python\\flappy-bird-1.png.png')
spriteplay = pygame.transform.scale(spriteplay,(100,100))

bg_img = pygame.image.load('C:\\Users\\ethan\\.vscode\\cool\\python\\flappy-backdrop4.png') 
bg_img = pygame.transform.scale(bg_img,(SCREEN_WIDTH,SCREEN_HIGHT))

while running:
    screen.blit(bg_img,(0,0))
    GAME_FONT.render_to(screen, (20, 20,20,20), "Score:"+str(score), (0, 0, 0))
    rect_play = pygame.Rect(x,y,20,20)
    rect_toptube = pygame.Rect(xx,0,60,y1)
    rect_bottomtube = pygame.Rect(xx,y2,60,SCREEN_HIGHT-y2)
    rect_tubepart = pygame.Rect(xx-10,y1,80,30)
    rect_tubepart2 = pygame.Rect(xx-10,y2,80,30)
    rect_ground = pygame.Rect(0,SCREEN_HIGHT-40,SCREEN_WIDTH,80)
    #pygame.draw.rect(screen,(0,0,0),rect_play)
    screen.blit(spriteplay,(x,y))
    pygame.draw.rect(screen,(50,168,82),rect_toptube)
    pygame.draw.rect(screen,(50,168,82),rect_bottomtube)
    pygame.draw.rect(screen,(50,168,82),rect_tubepart)
    pygame.draw.rect(screen,(50,168,82),rect_tubepart2)
    pygame.draw.rect(screen,(252,165,3),rect_ground)
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
        y1 = random.randint(1,SCREEN_HIGHT-160)
        y2 = y1 + 250
        while y2 < SCREEN_HIGHT-200:
            y1 = random.randint(1,SCREEN_HIGHT-160)
            y2 = y1 + 250
        xx = SCREEN_WIDTH
        score += 1

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