def solution(n):
    answer_temp = [[0]*n for i in range(n)]
    answer = []
    num = 1
    x = -1
    y = 0
    time = n
    times = sum([i for i in range(n,0,-1)])
    while num <= times:
        for i in range(time):
            if num > times: 
                break
            x += 1
            answer_temp[x][y] = num
            num += 1
            
        time -= 1
        for i in range(time):
            if num > times: 
                break
            y += 1
            answer_temp[x][y] = num
            num += 1
            
        time -= 1
        for i in range(time):
            if num > times: 
                break
            x -= 1
            y -= 1
            answer_temp[x][y] = num
            num += 1
        time -= 1
        
    for line in answer_temp:
        for i in line:
            if i == 0:
                continue
            answer.append(i)

    return answer