n, m = map(int,input().split())
ans = [i for i in range(1, n+1)]
count = 0
print('<', end='')
while len(ans) > 1:
    count += m-1
    count %= len(ans)
    print(ans.pop(count), end=', ')
print(ans.pop(), end='>')