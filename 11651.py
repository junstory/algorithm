n = int(input())
ret = []
for i in range(n):
    x,y = map(int,input().split())
    ret.append((x,y))

ret.sort(key = lambda x : (x[1],x[0]))

for x, y in ret:
    print(x,y)