"""
  W 0 1 2 3
H 0 0 1 1 1
  1 x 1 2 3
  2   x 2 5 ...??

일단 전체를 뽑아야 반쪽이 생긴다.
W,H = (2.2) 인 경우도 그래서 whhw가 불가능 하므로 경우의 수는 2가지.
그러면 왼쪽 + 위쪽의 경우의 수를 더하면 된다.
"""

dp = [[0] * 31 for _ in range(31)]
for i in range(1,31):
    dp[0][i] = 1

for i in range(1,31):
    for j in range(i,31):
        dp[i][j] += dp[i-1][j] + dp[i][j-1]
# for i in dp:
#     print(i)

while True:
    n = int(input())
    if n == 0:
        break
    print(dp[n][n])