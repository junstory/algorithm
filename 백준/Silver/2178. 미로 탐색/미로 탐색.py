from collections import deque

def bfs(start_x, start_y, end_x, end_y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(start_x, start_y,1)])
    visited = set([(start_x, start_y)])

    while queue:
        x, y, dist = queue.popleft()

        if x==end_x and y == end_y:
            return dist
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if (nx, ny) not in visited:
                    if graph[nx][ny] == 1:
                        visited.add((nx, ny))
                        #print(graph[nx][ny])
                        queue.append((nx, ny, dist+1))
    return -1

n, m = map(int,input().split())
graph = []
for i in range(n):
    temp = list(map(int,list(input())))
    graph.append(temp)
print(bfs(0,0,n-1,m-1,graph))