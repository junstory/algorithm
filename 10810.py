n, m = map(int,input().split())

ans = [0 for i in range(n)]

for i in range(m):
    a,b,c = map(int, input().split())
    for j in range(a-1,b):
        ans[j] = c

for i in ans:
    print(i,end = " ")
    