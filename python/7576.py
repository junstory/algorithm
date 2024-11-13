from collections import deque

def bfs():
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<= ny < m and a[nx][ny] ==0:
                a[nx][ny] = a[x][y] + 1
                queue.append([nx,ny])
        

m, n = map(int, input().split())
a = []
res = 0

queue = deque([])

for i in range(n):
    temp = list(map(int, input().split()))
    a.append(temp)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if a[i][j]==1:
            #print(i,j)
            queue.append([i,j])
bfs()
for i in a:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res-1)