def sol(curr_x,curr_y):
    global counter
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    house[curr_x][curr_y] = 0
    for i in range(4):
        nx = curr_x + dx[i]
        ny = curr_y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if house[nx][ny] == 1:
            counter += 1
            sol(nx,ny)

n = int(input())
house = []

for i in range(n):
    temp = list(map(int, list(input())))
#   print(temp)
    house.append(temp)
#print(house)
total = 0
count = []
for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            total += 1
            counter = 1
            sol(i,j)
            count.append(counter)
print(total)
count.sort()
for i in count:
    print(i)
