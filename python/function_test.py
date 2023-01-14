class position:
    def __init__(self,y,x):
        self.x = x
        self.y = y

arr= [[position(j,i) for i in range(4,8)]for j in range(-2,2)]
for i in range(4):
    for j in range(4):
        print(f'({arr[i][j].x} {arr[i][j].y}) ',end='')
    print('')