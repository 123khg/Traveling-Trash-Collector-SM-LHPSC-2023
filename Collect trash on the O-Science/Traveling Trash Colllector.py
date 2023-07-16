#Cách sử dụng: bấm chạy và dùng 2 nút A D hoặc Left arrow Right arrow
#Code này dùng cho game của Second Meeting 2023 LHPSC

import numpy as np, pygame as pg, time
pg.init()

w, h = 650, 650
screen = pg.display.set_mode([w, h])
run = True

#CREATE MAP
def createMap(times):
    gameMapGen = []
    for _ in range(times):
        numpyMap = np.random.multinomial(1, [0.1, 0.15, 0.6, 0.15], [8, 8]).argmax(axis = 2)
        #                                   Trash Block Air  Wall
        gameMap = []
        for row in numpyMap:
            gameMap.append([])
            for col in row:
                if col == 0:
                    obj = 'T'
                elif col == 1:
                    obj = 'B'
                elif col == 2:
                    obj = ' '
                else:
                    obj = 'W'
                gameMap[-1].append(obj)
                #print(obj + " ", end = "")
            #print("")
        #print("----------------")
        gameMapGen.append(gameMap)
    
    return gameMapGen

#DRAW UI
def UI(drawMap, quantity, w, h):
    #GRID LINES
    for i in range(9):
        x = 0 + w/8 * i
        y = 0 + h/8 * i
        pg.draw.line(screen, (0, 0, 0), (x, 0), (x, h), 5)
        pg.draw.line(screen, (0, 0, 0), (0, y), (w, y), 5)
    
    #DRAW OBSTACLES
    for row in range(8):
        for col in range(8):
            if drawMap[row][col] == 'T':
                pg.draw.circle(screen, (0, 200, 0), (w/8*(col+1/2), h/8*(row+1/2)), w/16)
            elif drawMap[row][col] == 'B':
                pg.draw.circle(screen, (0, 0, 200), (w/8*(col+1/2), h/8*(row+1/2)), w/16)
            elif drawMap[row][col] == ' ':
                continue
            else:
                #print(w/8*(col-1), h/8*(row-1), w/8, h/8)
                pg.draw.rect(screen, (100, 100, 100), pg.Rect(w/8*col, h/8*row, w/8, h/8))
                
mapIndex = 0
quantity = 50
gameMapGen = createMap(quantity)
while run:
    screen.fill((255, 255, 255))
    UI(gameMapGen[mapIndex], quantity, w, h)
    
    #EVENT
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
                 
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                mapIndex -= 1
            elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                mapIndex += 1
            
            #LIMITS
            if mapIndex < 0:
                mapIndex = quantity - 1
            elif mapIndex >= quantity:
                mapIndex = 0
            
            #OUTPUTS MAP
            for row in gameMapGen[mapIndex]:
                print(*row)
            print("--------------")
            
    #time.sleep(2)
        
pg.quit()