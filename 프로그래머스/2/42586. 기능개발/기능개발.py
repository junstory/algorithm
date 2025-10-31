def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        #print(progresses, len(progresses))
        
        temp = 0
        for i in range(len(progresses)):
            if progresses[i] >= 100 and temp == i:
                temp += 1
        if temp != 0:
            answer.append(temp)
        for i in range(temp):
            progresses.pop(0)
            speeds.pop(0)
    return answer