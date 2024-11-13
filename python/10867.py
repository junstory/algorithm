n = int(input())
ret = set(map(int,input().split()))
ret = list(ret)
ret.sort()
for i in ret:
    print(i, end=' ')