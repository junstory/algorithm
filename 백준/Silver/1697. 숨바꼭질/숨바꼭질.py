from collections import deque

def bfs(start, end):
    
    queue = deque([(start, 0)])
    visited = set([(start)])

    while queue:
        curr, time = queue.popleft()

        if curr== end:
            return time
        
        for next in (curr +1, curr -1, curr*2):
            if 0 <= next <= 100000 and next not in visited:
                queue.append((next, time+1))
                visited.add(next)
    return -1

n, m = map(int,input().split())
print(bfs(n,m))