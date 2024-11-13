n = int(input())

#수가 커질 때마다 가로세로 4씩 증가.
#배열은 (4*n) -3 크기
size = (4*n) -3
arr = [[' ']*size for i in range(size)]

def sol(n,x,y):
    global arr
    size = (4*n) -3
    if size == 1:
        arr[x][y] = '*'
        return
    else:
        for i in range(size):
            arr[x][y+i] = '*'
            arr[x+i][y] = '*'
            arr[x+size-1][y+i] = '*'
            arr[x+i][y+size-1] = '*'
        n -= 1
        x += 2
        y += 2
        sol(n,x,y)
        return

sol(n,0,0)
for i in arr:
    for elem in i:
        print(elem,end="")
    print()

