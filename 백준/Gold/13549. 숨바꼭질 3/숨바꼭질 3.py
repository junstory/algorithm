from collections import deque

n, k = map(int, input().split())

def bfs(start, end):

    queue = deque([(start, 0)])
    visited = [-1] * 100001
    visited[start] = 0
    
    best_time = -1
    count = 0

    while queue:
        curr, time = queue.popleft()

        if best_time != -1 and time > best_time:
            break

        if curr == end:
            if best_time == -1:
                best_time = time
                count += 1
            elif time == best_time:
                count += 1
        

        
        for next in (curr + 1, curr -1, curr *2):
            if 0<= next <= 100000 and (visited[next] == -1 or visited[next] == time+1):
                visited[next] = time+1
                if next == curr * 2:
                    queue.appendleft((next, time))
                else:
                    queue.append((next, time+1))
                

    return best_time, count

best_time, count = bfs(n, k)
print(best_time)
