def solution(picks, minerals):
    answer = 0
    total = sum(picks) * 5
    mine = [[0,0,0] for i in range(total//5+1)]
    
    for i in range(min(total, len(minerals))):
        if minerals[i] == "diamond":
            mine[i//5][0] +=1
        elif minerals[i] == "iron":
            mine[i//5][1] +=1
        elif minerals[i] == "stone":
            mine[i//5][2] +=1
    
    mine.sort(reverse = True)
    for i in mine:
        a,b,c = i
        if picks[0] > 0:
            answer += (a+b+c)
            picks[0] -= 1
        elif picks[1] > 0:
            answer += (5*a+b+c)
            picks[1] -= 1
        elif picks[2] > 0:
            answer += (25*a+5*b+c)
            picks[2] -= 1
    return answer