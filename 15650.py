from itertools import combinations
n, m = map(int, input().split())

li = [i for i in range(1,n+1)]
ans = list(map(list, list(combinations(li, m))))
for items in ans:
    for item in items:
        print(item, end = ' ')
    print()