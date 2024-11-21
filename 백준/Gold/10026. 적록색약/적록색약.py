# from collections import deque
# import sys
# sys.setrecursionlimit(10000)
# n = int(input())

# colors = []
# for i in range(n):
#     colors.append(list(input()))

# def dfs(x,y):
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]

#     #queue = deque([(x,y)])
#     #visited = set([(x,y)])

#     while queue:
#         x, y, count = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < n and 0 <= ny < n:
#                 if (nx, ny) not in visited:
#                     if colors[nx][ny] == colors[x][y]:
#                         print(colors[nx][ny], colors[x][y])
#                         visited.add((nx, ny))
#                         queue.append((nx, ny,count))
#                         dfs(nx, ny)
#                     else:
#                         print("\n\nanother",colors[nx][ny], colors[x][y])
#                         visited.add((nx, ny))
#                         queue.append((nx, ny,count+1))
#                         dfs(nx, ny)

#     return count

# queue = deque([(0,0,1)])
# visited = set([(0,0)])
# print(dfs(0,0))
    
from collections import deque
import sys
sys.setrecursionlimit(10000)
n = int(input())

colors = []
colors2 = []
for i in range(n):
    tmp = input()
    colors.append(list(tmp))
    colors2.append(list(tmp))



def dfs(x,y, color, colors):
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if colors[x][y] == 0:
        return

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    if colors[x][y] in color:
        colors[x][y] = 0
    else:
        return
    #queue = deque([(x,y)])
    #visited = set([(x,y)])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx, ny, color, colors)

red_count = 0
green_count = 0
blue_count = 0

first_count = 0
for i in range(n):
    for j in range(n):
        if colors[i][j] == 'R':
            dfs(i,j,["R"], colors)
            first_count += 1
        elif colors[i][j] == 'G':
            dfs(i,j,["G"], colors)
            first_count += 1
        elif colors[i][j] == 'B':
            dfs(i,j,["B"], colors)
            first_count += 1

second_count = 0
for i in range(n):
    for j in range(n):
        if colors2[i][j] == 'R' or colors2[i][j] == 'G':
            dfs(i,j,["R", "G"], colors2)
            second_count += 1
        elif colors2[i][j] == 'B':
            dfs(i,j,"B", colors2)
            second_count += 1

print(first_count, second_count)