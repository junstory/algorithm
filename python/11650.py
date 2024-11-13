n = int(input())
ret = []
for i in range(n):
    x,y = map(int,input().split())
    ret.append((x,y))

ret.sort()

for x, y in ret:
    print(x,y)