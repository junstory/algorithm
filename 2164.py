# Try 2
from collections import deque
n = int(input())
ret = deque([i for i in range(1,n+1)])
while len(ret) != 1:
    ret.popleft()
    last = ret.popleft()
    ret.append(last)    
    print(ret)

print(ret[0])


# Try 1(Timeout)
# n = int(input())
# ret = [i for i in range(1,n+1)]
# ret.reverse()
# while len(ret) != 1:
#     ret.pop()
#     last = ret.pop()
#     ret.insert(0,last)
#     #print(ret)

# print(ret[0])