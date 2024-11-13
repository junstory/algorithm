# Try.1 무작정 h를 최대로 두고 1씩줄이면 시간초과
# Try.2 재귀를 이용한 이분탐색은 깊이 초과, 시간초과
# Try.3 반복을 이용해 완료. 
import sys
sys.setrecursionlimit(10**6)
n, m = map(int,input().split())
trees = list(map(int,input().split()))
h = max(trees)
s = 0
e = max(trees)
while s <= e:
    mid = (s+e) // 2
    ret = 0
    for i in trees:
        if i - mid >= 0:
            ret += i-mid
    if ret >= m:
        s = mid + 1
    else:
        e = mid -1
print(e)
# while e_h < m:
#     e_h = 0
#     h -= 1
#     for i in trees:
#         if i - h > 0:
#             e_h += i-h
    
    
#print(sol(0,max(trees),m,trees))
# for i in trees:
#     if i-h >=0:
#         print(i-h, end=" " )
#     else:
#         print(i,end=" ")
