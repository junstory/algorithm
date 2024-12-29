n = int(input())

a = set()

for i in range(n):
    name, stat = map(str, input().split())
    if stat == 'enter':
        a.add(name)
    else:
        a.remove(name)

ans = list(a)
ans.sort(reverse=True)
for i in ans:
    print(i)