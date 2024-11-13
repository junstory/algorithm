# 2579
# 계단 오르기

# 연속으로 세 계단은 불가능.
# dp배열에 그때까지의 최대값을 정함.
# dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])
# 가능한 경우는 1. i-3번째 + 연속으로 이전(i-1), 나(i) i-2는 건너뜀.
# 2. i-2번째 + 나(i) i-2는 연속으로 왔든 띄엄띄엄왔든 모름. 상관없음. 왜? i-2를 계산할 당시에 최댓값을 추구해서 구한거니까.

stairs = [0] * 301
for i in range(1, n + 1):
    stairs[i] = int(input())

dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n])


# n = int(input())
# dp = [0 for i in range(n)]
# arr = [0 for i in range(n)]
# for i in range(n):
#     arr[i] = int(input())



# for i in range(n):
#     if i == 0:
#         dp[0] = arr[0]
#     elif i ==1:
#         dp[1] = arr[0] + arr[1]
#     elif i==2:
#         dp[2] = max(arr[0]+arr[2],arr[1]+arr[2])
#     else:
#         dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])


# print(dp[n-1])

