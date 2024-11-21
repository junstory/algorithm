from collections import deque
import sys
sys.setrecursionlimit(10000)
n = int(input())

colors = []
for i in range(n):
    colors.append(list(input()))

def dfs(x,y,colors):
    queue.append((x,y))
    visited.add((x,y))

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if (nx, ny) not in visited:
                    if colors[nx][ny] == colors[x][y]:
                        visited.add((nx, ny))
                        queue.append((nx, ny))


queue = deque()
visited = set()
cnt1 = 0
for i in range(n):
    for j in range(n):
        if (i, j) not in visited:
            dfs(i, j, colors)
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if colors[i][j] == 'G':
            colors[i][j] = 'R'

visited = set()
cnt2 = 0
for i in range(n):
    for j in range(n):
        if (i, j) not in visited:
            dfs(i, j, colors)
            cnt2 += 1

print(cnt1, cnt2)