n = int(input())

dp = [0 for i in range(n+1)]

def sol(n):
    global dp
    if n == 1:
        return 1
    elif n == 2:
        return 2
    if dp[n] > 0:
        return dp[n]
    dp[n] = (sol(n-2) + sol(n-1))%10007
    return dp[n]

ret = sol(n)
print(ret)

'''
n = int(input())
# memoization을 위함
cache = [0]*1001
# n이 1,2인 경우는 명확하니까 미리 선언해둔다.
cache[1]=1
cache[2]=2
# dynamic programming
for i in range(3,1001):
  cache[i] = (cache[i-1]+cache[i-2])%10007

print(cache[n])
'''