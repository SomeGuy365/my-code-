import pygame
import random
import time
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

x = 400
y = 450

bullets = []
ebullet = []
enemy = []

fps = pygame.time.Clock()

class Bullet:
     def __init__(self,x,y):
          self.x = x
          self.y = y

class Enemy:
     def __init__(self,x,y,direction,speed):
          self.x = x
          self.y = y
          self.direction = direction
          self.speed = speed

pressed = ''
level = 0
time1 = 0

GAME_FONT = pygame.freetype.SysFont('arial',25)
DEAD_FONT = pygame.freetype.SysFont('arial',70)

def bedead():
    DEAD_FONT.render_to(screen, (20, 20,20,20), "UR DEAD!", (255, 255, 255))
    time.sleep(2)
    pygame.quit()
    quit()


while running:
    screen.fill((0,0,0))
    GAME_FONT.render_to(screen, (20, 20,20,20), "Level:"+str(level), (255, 255, 255))
    rect_play = pygame.Rect(x,y,40,40)
    pygame.draw.rect(screen,(200,200,200),rect_play)
    for event in pygame.event.get():
        if event.type == QUIT:
                running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                pressed = 'left'
            elif event.key == pygame.K_RIGHT:
                pressed = 'right'
            elif event.key == pygame.K_UP:
                 bullets.append(Bullet(x+10,y-10))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pressed = ''
            elif event.key == pygame.K_RIGHT:
                pressed = ''
        
    if pressed == 'left':
        x -= 3
    elif pressed == 'right':
        x += 3

    for bullet in bullets:
        pygame.draw.rect(screen,(100,100,100),(bullet.x,bullet.y,20,20))
        bullet.y -= 10

    if not enemy:
        level += 1
        ey = [50]
        for i in range(level):
            if level > 3:
                ey.append(80)
                if level > 7:
                    ey.append(20)
            direc = random.randint(0,1)
            if direc == 0:
                enemy.append(Enemy(SCREEN_WIDTH/2,random.choice(ey),'left',random.randint(8,30)/10))
            else:
                enemy.append(Enemy(SCREEN_WIDTH/2,random.choice(ey),'right',random.randint(8,30)/10))
    else:
        for i in enemy:
            pygame.draw.rect(screen,(219, 7, 7),(i.x,i.y,20,20))
            if i.direction == 'left':
                if i.x < 100:
                    i.direction = 'right'
                else:
                    i.x -= i.speed
            elif i.direction == 'right':
                if i.x > SCREEN_WIDTH-100:
                    i.direction = 'left'
                else:
                    i.x += i.speed


    for i in enemy:
        for b in bullets:
            rect_enemy = pygame.Rect(i.x,i.y,20,20)
            rect_bullet = pygame.Rect(b.x,b.y,20,20)
            if rect_enemy.colliderect(rect_bullet):
                enemy.remove(i)
        
    if time1 == 100:
        shoot = random.choice(enemy)
        ebullet.append(Bullet(shoot.x,shoot.y))
        time1 = 0

    for i in ebullet:
        rect_ebullet = pygame.Rect(i.x,i.y,20,20)
        pygame.draw.rect(screen,(65, 5, 150),(rect_ebullet))
        i.y += 1
        if rect_play.colliderect(rect_ebullet):
            bedead()
            

    time1 += 1


    pygame.display.update()
    fps.tick(100)