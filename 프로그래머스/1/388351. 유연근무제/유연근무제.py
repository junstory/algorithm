def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        day = startday
        count = 0
        for j in range(7):
            if day > 5:
                count += 1
            else:
                start = schedules[i]
                end = (start + 10) if (start + 10) % 100 < 60 else (start//100 + 1) * 100 + (start%100 + 10)%60
                
                if timelogs[i][j] <= end:
                    count += 1
                #print(i, day, timelogs[i][j], start,end, count)
            day = day % 7 + 1
        if count == 7:
                answer += 1
    return answer