n, m  = map(int, input().split())

ans = [i for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    ans[a],ans[b] = ans[b], ans[a]

for i in range(1, n+1):
    print(ans[i],end=" ")