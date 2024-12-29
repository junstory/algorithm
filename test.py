from collections import deque

n = int(input())
ret = []
for i in range(n):
    ret.append(int(input()))

ans = []
q = deque([])
for i in range(1, n+1):
    q.appendleft(i)
    temp = q.popleft()
    if temp == ret[0]:
        while len(ret) != 0 and temp == ret[0]:
            ans.append('-')
            ret.pop(0)
            if len(q) != 0:
                temp = q.popleft()
        q.appendleft(temp)
    else:
        q.appendleft(temp)
        ans.append('+')
print(ret)
print(ans)
print(q)
    
