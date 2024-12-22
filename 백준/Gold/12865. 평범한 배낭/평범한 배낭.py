n, k = map(int, input().split())
items= []

for i in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

items.sort()

dp = [0] * (k+1)
for i in range(n):
    for j in range(k, items[i][0]-1, -1):
        dp[j] = max(dp[j], dp[j-items[i][0]] + items[i][1])
print(dp[k])
