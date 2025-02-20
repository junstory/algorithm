import math
def solution(a, b, g, s, w, t):
    answer = (10**9*2) * (10**5*2)
    start = 0
    end = (10**9*2) * (10**5*2)
    while start <= end:
        mid = (start+end)//2
        gold = 0
        silver = 0
        add = 0
        for i in range(len(t)):
            nowGold = g[i]
            nowSilver = s[i]
            nowWeight= w[i]
            nowTime = t[i]
            
            moveCount = mid//(nowTime*2)
            if mid % (nowTime*2) >=t[i]:
                moveCount += 1
            
            gold += min(nowGold, moveCount*nowWeight)
            silver += min(nowSilver, moveCount*nowWeight)
            add += min(nowGold+nowSilver, moveCount * nowWeight)
                
        if(a <= gold and b <= silver and a+b <= add):
            end = mid -1
            answer = min(mid, answer)
        else:
            start = mid + 1
              
    return answer