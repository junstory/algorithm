def isOutside(storage, x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    outside = False
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if storage[nx][ny] == "0":
            storage[x][y] = "0"
            outside = True
            break
            
    if outside:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if storage[nx][ny] == "1":
                storage[nx][ny] = "0"
                isOutside(storage,nx,ny)

def solution(storage, requests):
    answer = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    idx = []
    storage = [list("0" + i + "0") for i in storage]
    storage.append(["0"]*len(storage[0]))
    storage.insert(0,["0"]*len(storage[0]))
    for want in requests:
        if len(want) == 1:
            for i in range(1,len(storage)-1):
                for j in range(1,len(storage[0])-1):
                    if storage[i][j] == want:
                        for k in range(4):
                            nx, ny = i +dx[k], j + dy[k]
                            if storage[nx][ny] == "0":
                                idx.append((i,j))
                                break
            for i, j in idx:
                storage[i][j] = "0"
                isOutside(storage, i, j)
                                
        else:
            want = want[0]
            for i in range(len(storage)):
                for j in range(len(storage[0])):
                    if storage[i][j] == want:
                        storage[i][j] = "1"
                        isOutside(storage,i,j)
    for i in storage:
        for j in i:
            if j != "0" and j != "1":
                answer += 1
    return answer