def solution(answers):
    answer = []
    ans1 = [1,2,3,4,5]
    ans2 = [2,1,2,3,2,4,2,5]
    ans3 = [3,3,1,1,2,2,4,4,5,5]
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(len(answers)):
        if ans1[i%len(ans1)] == answers[i]:
            count1 += 1
        if ans2[i%len(ans2)] == answers[i]:
            count2 += 1
        if ans3[i%len(ans3)] == answers[i]:
            count3 += 1
    max_count = max(count1, count2, count3)
    if count1 == max_count:
        answer.append(1)
    if count2 == max_count:
        answer.append(2)
    if count3 == max_count:
        answer.append(3)
    return answer
