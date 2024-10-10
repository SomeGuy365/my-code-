import pygame
pygame.init()

explosion = pygame.image.load("python/pics/nuke.jpg")
explosion = pygame.transform.scale(explosion,(25,25))

grid_left = 272
grid_right = 507
grid_top = 52

MARGIN = 5
WIDTH = 20
HEIGHT = 20

grid = []
grid2 =[]

colour = (255,255,255)

for row in range(10):
    grid.append([])
    grid2.append([])
    for column in range(10):
        grid[row].append(0)
        grid2[row].append(0)

screen = pygame.display.set_mode([300, 650])
block_size = 25

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if pos[1] < 375:
                row = pos[0]//(WIDTH+MARGIN)
                column = pos[1]//(HEIGHT+MARGIN)
                if row < 10 and column < 10:
                    grid[row][column] = 1
                print(row,column)
            else:
                row = pos[0]//(WIDTH+MARGIN)
                column = (pos[1]-375)//(HEIGHT+MARGIN)
                if row < 10 and column < 10:
                    grid2[row][column] = 1
                print(row,column)
            print(pos)

    for x in range(10):
        for y in range(10):
            if grid[x][y] == 1:
                colour = (0,0,0)
            else:
                colour = (255,255,255)

            pygame.draw.rect(screen,colour,[(MARGIN + WIDTH) * x + MARGIN,
                                                   (MARGIN + HEIGHT) * y + MARGIN,
                                                   WIDTH,
                                                   HEIGHT])

    for x in range(10):
        for y in range(10):
            if grid2[x][y] == 1:
                colour = (0,0,0)
            else:
                colour = (255,255,255)

            pygame.draw.rect(screen,colour,[(MARGIN + WIDTH) * x + MARGIN,
                                                   (MARGIN + HEIGHT) * (y+15) + MARGIN,
                                                   WIDTH,
                                                   HEIGHT])

    pygame.display.update()

pygame.quit()