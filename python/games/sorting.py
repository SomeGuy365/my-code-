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

def endcheck():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_RIGHT:
                return False
            if event.key == pygame.K_LEFT:
                return True

#Grid initiations/drawing to screen
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
            
def tredraw(move,speed):
    if type(move) == int:
        typ = 'int'
    else:
        typ = 'list'
    drawgrid(bars,move,typ)
    pygame.time.delay(speed)
    pygame.display.update()

#Sorting functions#
###################

def bubblesort():
    #if value to left is higher, bars swap and og moves right 
    for i in range(len(bars) - 1):
        for j in range(len(bars) - i - 1):
            if bars[j] > bars[j + 1]:
                t = bars[j]
                bars[j] = bars[j + 1]
                bars[j + 1] = t
            tredraw(j+1,10)

        if endcheck():
            break

def insertsort():
    #compares induvidual elements with all before to find sorted space 
    for i in range(1,len(bars)):
        key_index = bars[i]
        j = i - 1
        while j >= 0 and bars[j] > key_index:
            bars[j + 1] = bars[j]
            j -= 1
            tredraw(j,0)
        bars[j + 1] = key_index
        tredraw(j,10)

        if endcheck():
            break       


#Quicksort
def partition(array,low,high):
    #Function seperates list between low/high
    pivot = array[high]
    i = low-1

    for j in range(low,high):
        if array[j] <= pivot:
            i += 1
            (array[i], array[j]) = (array[j], array[i])
        temp = [i,j]
        tredraw(temp,10)
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i+1

def quicksort(array,low,high):
    #function continously seperates/sorts list until complete
    if low < high:
        pi = partition(array,low,high)

        quicksort(array,low,pi-1)
        tredraw("None",10)
        quicksort(array,pi+1,high)
#-----------------------------------------------#

#Radix sort                      -WIP:End check prob dont work,rework system or build seperate one?
def countingSort(arr, exp1):
    n = len(arr)
    #sets len of output and initalises count array as 0
    output = [0] * (n)
    count = [0] * (10)

    #stores count of occurences
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
    #changes count into useable index
    for i in range(1, 10):
        count[i] += count[i - 1]

    #builds output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    #copys output to og array 
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
        tredraw(i,10)

def radixSort(arr):
    #max:largest num in unsorted array
    max1 = max(arr)
    #exp:digit being sorted
    exp = 1
    while max1 / exp >= 1:
        #sorts current digit
        countingSort(arr, exp)
        #moves the sorting digit up
        exp *= 10
#-----------------------------------------------#

#THE MAIN EVENT#
execute = False
while running:
    drawgrid(bars,"None","Nah")
    

    if execute == False:
        drawgrid(bars,"None","Nah")
        pygame.display.update()
    else:
        #bubblesort()
        #insertsort()
        #quicksort(bars,0,len(bars)-1)
        radixSort(bars)

        execute = False

    for event in pygame.event.get():
        if event.type == QUIT:
                 running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                 running = False
            if event.key == pygame.K_RIGHT:
                execute = True