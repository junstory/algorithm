import sys
print = sys.stdout.write
n = int(input())


ret = [[' ' for _ in range(n*2)] for _ in range(n)]

def solve(x,y,n):
    if n==3:
        ret[x][y] = '*'
        ret[x+1][y+1] = '*'
        ret[x+1][y-1] = '*'
        for i in range(-2,3):
            ret[x+2][y+i] = '*'
        return
    n = n//2
    solve(x,y,n)
    solve(x+n,y+n,n)
    solve(x+n,y-n,n)



solve(0,n-1,n)

for line in ret:
    for i in line:
        print(i)
    print('\n')


