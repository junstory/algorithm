from itertools import combinations
def solution(n, q, ans):
    answer = 0
    combi = list(combinations(range(1,n+1),5))
    
    for code in combi:
        canMake = True
        for i in range(len(q)):
            if len(set(q[i])&set(code)) != ans[i]:
                canMake = False
                break
        if canMake:
            answer += 1
        
    return answer