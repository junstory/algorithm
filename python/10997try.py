n = int(input())
# 별 한줄은 4*n-3개
# if n=100 then 397 -> 약 400
stars = [[' ']*400]*400


def star(n,x,y):
    #top
    for i in range(4*n -3):
        stars[x][y+i] = '*'
    
    #left
    for i in range(4*n-1):
        stars[x+i][y] = '*'
    #bottom
    for i in range(4*n -3):
        stars[x+(4*n-2)][y+i] = '*'
    
    #right
    for i in range(2*n + 2):
        stars[x + 4*n-2 - i][y+3*n] = '*'
if n==1:
    print('*')
    exit()


star(n,0,0)

for i in stars:
    for j in i:
        print(j,end="")
    print()

