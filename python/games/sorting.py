import random
import pygame
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
SCREEN_HIGHT = 800
running = True
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HIGHT])

#Grid initiations
HEIGHT = 8
WIDTH = 8
MARGIN = 2
colour = (0,0,0)

bars = []
for a in range(100):
    num = random.randint(1,100)
    while num in bars:
        num = random.randint(1,100)
    bars.append(num)

def drawgrid(bars,move,typ):
    screen.fill((0,0,0))
    for x in range(100):
        for y in range(100):
            if y < bars[x]:
                colour = (0,0,0)
            else:
                if move == "None":
                    colour = (255,0,0)

                if typ == 'list':
                    if x == move[0] or x == move[1]:
                        colour = (0,255,0)
                    else:
                        colour = (255,0,0)
                elif typ == 'int':
                    if x == move:
                        colour = (0,255,0)
                    else:
                        colour = (255,0,0)
                else:
                    colour = (255,0,0)
            pygame.draw.rect(screen,colour,[(WIDTH) * x + MARGIN,
                                            (HEIGHT) * y + MARGIN,
                                            WIDTH,
                                            HEIGHT])
            
def redraw():
    drawgrid(bars,"None","uh")
    pygame.time.delay(1)
    pygame.display.update()

def tredraw(move):
    if type(move) == int:
        typ = 'int'
    else:
        typ = 'list'
    drawgrid(bars,move,typ)
    pygame.time.delay(10)
    pygame.display.update()

#Quicksort functions

def partition(array,low,high):
    pivot = array[high]
    i = low-1

    for j in range(low,high):
        if array[j] <= pivot:
            i += 1
            (array[i], array[j]) = (array[j], array[i])
        temp = [i,j]
        tredraw(temp)
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i+1

def quicksort(array,low,high):
    if low < high:
        pi = partition(array,low,high)

        quicksort(array,low,pi-1)
        redraw()
        quicksort(array,pi+1,high)

###############################


execute = False

while running:
    drawgrid(bars,"None","Nah")
    

    if execute == False:
        drawgrid(bars,"None","Nah")
        pygame.display.update()
    else:
        #Bubble sort
        for i in range(len(bars) - 1):
            for j in range(len(bars) - i - 1):
                if bars[j] > bars[j + 1]:
                    t = bars[j]
                    bars[j] = bars[j + 1]
                    bars[j + 1] = t
                tredraw(j+1)
        #Insert sort
        #for i in range(1,len(bars)):
        #    key_index = bars[i]
        #    j = i - 1
        #    while j >= 0 and bars[j] > key_index:
        #        bars[j + 1] = bars[j]
        #        print("ayy")
        #        j -= 1
        #    bars[j + 1] = key_index
        #    redraw()

        #quicksort(bars,0,len(bars)-1)
        #redraw()

        execute = False

    for event in pygame.event.get():
        if event.type == QUIT:
                 running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                 running = False
            if event.key == pygame.K_RIGHT:
                execute = True
            if event.key == pygame.K_LEFT:
                execute = False
