def hanoi(n, start, end, via, route):
    if n == 1:
        route.append([start,end])
        return route
    route = hanoi(n-1, start, via, end, route)
    route.append([start,end])
    route = hanoi(n-1, via, end, start,route)
    return route
    
def solution(n):
    answer = []
    answer = hanoi(n,1,3,2,answer)
    return answer