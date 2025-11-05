def solution(n, s, a, b, fares):
    min_total_cost = 100000 * 15 * 3
    dist = [[min_total_cost  for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):
        dist[i][i] = 0
    for _a,_b,_f in fares:
        dist[_a][_b] = _f
        dist[_b][_a] = _f
        
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
    answer = 0
        
    for k in range(1,n+1):
        curr_cost = dist[s][k] + dist[k][a] + dist[k][b]
        min_total_cost = min(min_total_cost, curr_cost)
    answer = min_total_cost
    return answer