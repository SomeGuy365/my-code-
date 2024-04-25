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

SCREEN_WIDTH = 1000
SCREEN_HIGHT = 600

running = True
pygame.init()

fps = pygame.time.Clock()

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HIGHT])

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def bubble():
    random.shuffle(list)
    n = len(list)

    for i in range(n):
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            print(list[0])

def insertaiton_sort(list):
    for i in range(1,len(list)):
        key_index = list[i]
        j = i - 1
        while j >= 0 and list[j] > key_index:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key_index
        print(list)

    return list



#WORK IN PROGRESS(I have no idea whats going on)

def quicksort(array):
    low, same, high = [], [], []

    pivot = list[random.randint(0,len(array)-1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
        print(low+same+high)
        
    return low + same + high

def quicksort2(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[random.randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)



HEIGHT = 8
WIDTH = 8
MARGIN = 4
colour = (0,0,0)

bars = []
for a in range(100):
    num = random.randint(1,100)
    while num in bars:
        num = random.randint(1,100)
    bars.append(num)

while running:
    screen.fill((255,255,255))
    for x in range(100):
        for y in range(100):
            if y == 10:
                colour = (255,0,0)
            pygame.draw.rect(screen,colour,[(MARGIN + WIDTH) * x + MARGIN,
                                            (MARGIN + HEIGHT) * y + MARGIN,
                                            WIDTH,
                                            HEIGHT])
    
    for i in range(1,len(bars)):
        key_index = bars[i]
        j = i - 1
        while j >= 0 and bars[j] > key_index:
            bars[j + 1] = bars[j]
            j -= 1
        bars[j + 1] = key_index

    for event in pygame.event.get():
        if event.type == QUIT:
                 running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                 running = False
            if event.key == pygame.K_RIGHT:
                bars[2] += 1

    pygame.display.update()
    fps.tick(2)
    

#while running:
    #userimp = int(input('what method\n1:bubble\n2:insertation\n'))
    #if userimp == 1:
       # random.shuffle(list)
        #print(list)
        #bubble()
    #elif userimp == 2:
        #random.shuffle(list)
        #print(list)
        #newlist = insertaiton_sort(list)
        #print(newlist)
    #elif userimp == 3:
        #random.shuffle(list)
        #print(list)
        #newlist = quicksort2(list)
        #print(newlist)
