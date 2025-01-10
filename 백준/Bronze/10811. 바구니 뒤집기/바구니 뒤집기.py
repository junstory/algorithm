n, m = map(int, input().split())

basket = [i for i in range(1, n+1)]

for i in range(m):
    a, b = map(int, input().split())
    temp = basket[a-1:b]
    temp.reverse()
    basket[a-1:b] = temp

for i in basket:
    print(i, end=' ')