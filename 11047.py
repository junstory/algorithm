#동전0
n, k = map(int, input().split())
coin = [0]*1000001
for i in range(n):
    cash = int(input())
    coin[cash] += 1
count = 0
while k > 0:
    for i in range(len(coin)-1,0,-1):
        if coin[i] > 0 and k - i > 0:
            coin[i] -= 1
            k -= i
            count += 1
            break

print(count)