#동전0
n, k = map(int, input().split())
coin = []
for i in range(n):
    cash = int(input())
    coin.append(cash)
coin.sort(reverse=True)
count = 0
for i in coin:
    if k//i > 0:
        count += k//i
        k %= i
        if k<= 0:
            break

print(count)