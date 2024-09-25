n = int(input())

# ret = [[' '] * n] * n 
# 얕은 복사로 모든 배열이 같은 객체를 가리키게 된다.
# 따라서 한 배열을 수정하면 다른 배열도 수정된다.

ret = [[' ' for _ in range(n)] for _ in range(n)]

# 3/n * 3/n 크기의 구멍을 내느거라 분할정복 필요해보임.
def solve(x,y,n):
    if n == 1:
        ret[x][y] = '*'
        return
    # if n == 3:
    #     for i in range(3):
    #         for j in range(3):
    #             if i == 1 and j == 1:
    #                 continue
    #             else:
    #                 ret[x+i][y+j] = '*'
    #     return
    n = n//3
    # 이중 for문 이라도 다 돌아봤자 9번.
    # 27인 경우 27 -> 9 , 이게 또 9번이니까 81번,,, 
    # 그디음도 9번... 그러면 284번 엄청 커지진 않는 것으로 보아 걱정X
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            solve(x+n*i, y+n*j, n)
            #print(x+n*i, y+n*j, n)
    return

solve(0,0,n)
for i in range(n):
    for j in range(n):
        print(ret[i][j], end='')
    print()