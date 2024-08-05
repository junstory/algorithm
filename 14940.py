from collections import deque

def bfs(start_x,start_y,graph):
    global ans
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque([(start_x,start_y,0)])
    visited = set([(start_x,start_y)])
    ans[(0,0)] = 0
    while queue:
        x, y, dist = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(graph) and 0<=ny <len(graph[0]):
                if (nx,ny) not in visited:
                    if graph[nx][ny] == 1:
                        visited.add((nx,ny))
                        queue.append((nx,ny,dist+1))
                        ans[(nx,ny)] = dist+1
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if (i,j) not in visited and graph[i][j] == 1:
                ans[(i,j)] = -1
                    

n, m = map(int,input().split())
ans = {}
for i in range(n):
    for j in range(m):
        ans[(i,j)] = 0

graph = []
start_x, start_y = 0, 0
for i in range(n):
    temp = list(map(int,input().split()))
    if 2 in temp:
        start_x = i
        start_y = temp.index(2)
    graph.append(temp)

bfs(start_x,start_y,graph)
ans[(start_x,start_y)] = 0
#print(ans)
for i in range(n):
    for j in range(m):
        print(ans[(i,j)], end=" ")
    print()