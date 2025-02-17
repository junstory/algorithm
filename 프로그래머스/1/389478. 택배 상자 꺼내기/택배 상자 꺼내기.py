def solution(n, w, num):
    answer = 0
    h = n//w + 1
    location = [[0]*w for i in range(h)]
    idx = 1
    for i in range(h):
        for j in range(w):
            if idx > n:
                break
            if i % 2 == 0:
                location[i][j] = idx
            else:
                location[i][w-j-1] = idx
            idx += 1
    x = 0
    y = 0
    for i in range(h):
        #print(location[i])
        for j in range(w):
            if location[i][j] == num:
                x = i
                y = j

    for i in range(x, h):
        if location[i][y] != 0:
            answer += 1
    
    return answer
