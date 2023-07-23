#Cách sử dụng: bấm chạy và dùng 2 nút A D hoặc Left arrow Right arrow
#Code này dùng cho game của Second Meeting 2023 LHPSC
#Bật chế độ output ra màn hình bằng nút V (verbose)

import numpy as np, pygame as pg, time
import os
pg.init()

w, h = 650, 650
screen = pg.display.set_mode([w, h])
run = True
verbose = False

#CREATE MAP
def createMap(times, size, generate_ratio: list):
    gameMapGen = []
    for _ in range(times):
        numpyMap = np.random.multinomial(1, generate_ratio, [size, size]).argmax(axis = 2)
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
def UI(drawMap, w, h, size):
    #GRID LINES
    for i in range(size + 1):
        x = 0 + w/size * i
        y = 0 + h/size * i
        pg.draw.line(screen, (0, 0, 0), (x, 0), (x, h), 5)
        pg.draw.line(screen, (0, 0, 0), (0, y), (w, y), 5)
    
    #DRAW OBSTACLES
    for row in range(size):
        for col in range(size):
            if drawMap[row][col] == 'T':
                pg.draw.circle(screen, (252, 186, 3), (w/size*(col+1/2), h/size*(row+1/2)), w/(size*2)-2)
            elif drawMap[row][col] == 'B':
                pg.draw.circle(screen, (255, 0, 0), (w/size*(col+1/2), h/size*(row+1/2)), w/(size*2)-2)
            elif drawMap[row][col] == ' ':
                continue
            else:
                #print(w/8*(col-1), h/8*(row-1), w/8, h/8)
                pg.draw.rect(screen, (100, 100, 100), pg.Rect(w/size*col+2, h/size*row+2, w/size-3, h/size-3))

def main():
    global run, verbose
    TRASH_RATIO = 0.02
    BLOCK_RATIO = 0.02
    WALL_RATIO = 0.1
    AIR_RATIO = 1 - TRASH_RATIO - BLOCK_RATIO - WALL_RATIO
    mapIndex = 0
    quantity = 30
    size = 21
    gameMapGen = createMap(quantity, size, [TRASH_RATIO, BLOCK_RATIO, AIR_RATIO, WALL_RATIO])
    id = 1
    while run:
        screen.fill((3, 190, 252))
        UI(gameMapGen[mapIndex], w, h, size)
        
        #LOAD IMAGES TO FOLDER
        if id <= quantity:
            pg.image.save(screen, f"generated/{id}.png")
            mapIndex = (mapIndex + 1) % quantity
            id += 1
            
        #EVENT
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    mapIndex = (mapIndex - 1) % quantity
                elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                    mapIndex = (mapIndex + 1) % quantity
                
                if event.key == pg.K_v:
                    verbose = not verbose
                    print(f"Verbose set to {verbose}")
            #OUTPUTS MAP
            if verbose:
                for row in gameMapGen[mapIndex]:
                    print(*row)
                print("--------------")
                
        #time.sleep(2)
            
    pg.quit()

if __name__ == "__main__":
    main()