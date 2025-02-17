def solution(sizes):
    answer = 0
    l = []
    s = []
    for a,b in sizes:
        if a > b:
            l.append(a)
            s.append(b)
        else:
            l.append(b)
            s.append(a)
            
    answer = max(l) * max(s)
        
    return answer