n = int(input())

# 기본 꼴도 시간 초과?
# def sol(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return sol(n-2) + sol(n-1)

# ret = sol(n)
# print(ret)


##Solution
# dp = [0 for i in range(n+1)]

# def sol(n):
#     global dp
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     if dp[n] > 0:
#         return dp[n]
#     dp[n] = sol(n-2) + sol(n-1)
#     return dp[n]

# ret = sol(n)
# print(ret)

a = 0
b = 1
for i in range(2,n+1):
    c = a + b
    a, b = b, c
print(b)