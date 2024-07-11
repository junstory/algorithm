 
n =40

dp = [0] * (n+1)
dp[0], dp[1] = [1,0], [0,1]
for i in range(2, n+1):
    dp[i] = [x+y for x,y in zip(dp[i-2], dp[i-1])]




n = int(input())
for i in range(n):
    out_zero = 0
    out_one = 0
    x = int(input())
    ret = dp[x]
    print(ret[0], ret[1])