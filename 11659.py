import sys
input = sys.stdin.readline
n, m = map(int,input().split())
li = list(map(int,input().split()))
ans = [0]
temp = 0
for i in li:
    temp += i
    ans.append(temp)

for i in range(m):
    a, b = map(int,input().split())
    print(ans[b]-ans[a-1])
    