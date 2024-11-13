n = []
for i in range(7):
    a = int(input())
    if a%2 != 0:
        n.append(a)


if not n:
    print(-1)
else:
    print(sum(n))
    print(min(n))