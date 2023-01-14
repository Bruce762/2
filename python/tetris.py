import pygame as pg

class position:
    def __init__(self,y,x):
        self.x = x
        self.y = y
#pygame初始化
pg.init()
#設定視窗
width, height = 12, 22
blockwide =  35
screen = pg.display.set_mode((width*blockwide, height*blockwide)) 
pg.display.set_caption("Tetris")        
#建立畫布bg
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255,255,255))           #白色
#顯示
screen.blit(bg, (0,0))

feild = [[0 for _ in range(width)] for _ in range(height)]
block= [[position(j,i) for i in range(4,8)]for j in range(-3,1)]
graphic1=[
    [0,0,0,0],
    [0,1,0,0],
    [1,1,0,0],
    [1,0,0,0]
]

#方塊設定
## 空白方塊
block0 = pg.Surface((blockwide,blockwide))
block0 = block0.convert()
block0.fill((255,255,255))

## 藍方塊
block1 = pg.image.load("block1.png")
block1.convert()
block1 = pg.transform.scale(block1,(blockwide,blockwide))


#生成灰色邊框
frame = pg.image.load("block0.png")
frame.convert()
frame = pg.transform.scale(frame,(blockwide,blockwide))
for i in range(width):
    screen.blit(frame,(i*blockwide,0))
    screen.blit(frame,(i*blockwide,(height-1)*blockwide))
    feild[0][i]=-1
    feild[height-1][i]=-1
for i in range(1,height-1):
    screen.blit(frame,(0,i*blockwide))
    screen.blit(frame,((width-1)*blockwide,i*blockwide))
    feild[i][0]=-1
    feild[i][width-1]=-1
pg.display.update()
clock = pg.time.Clock()#時間元件
"""
for i in range(height):
    for j in range(width):
        print(f'{feild[i][j]:>2}',end='')
    print('')
"""
running = True
recentX= blockwide * (width/2-1)
recenty= 0 

while running:
    clock.tick(1)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    bump=False
    for i in range(4):
        for j in range(4):
            nowX = block[i][j].x
            nowY = block[i][j].y            
            if nowY==0 and feild[nowX][nowY]!=0 and graphic1[i][j]==1:
                bump=True
    if bump == False:
        for i in range(4):
            for j in range(4):
                nowX = block[i][j].x
                nowY = block[i][j].y            
                if nowX>0 and nowX<11 and nowY>0 and nowY<21 and feild[nowX][nowY]==0 and graphic1[i][j]==1:
                    screen.blit(block0,(nowX*blockwide,nowY*blockwide))
                block[i][j].y+=1
        for i in range(4):
            for j in range(4):
                nowX = block[i][j].x
                nowY = block[i][j].y            
                if nowX>0 and nowX<11 and nowY>0 and nowY<21 and feild[nowX][nowY]==0 and graphic1[i][j]==1:
                    screen.blit(block1,(nowX*blockwide,nowY*blockwide))
    else :
        for i,y in zip(range(4),range(-3,1)):
            for j,x in zip(range(4),range(4,8)):
                block[i][j].x
    pg.display.update()
    
pg.quit() 