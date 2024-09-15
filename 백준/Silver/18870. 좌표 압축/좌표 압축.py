#너무 당연한 시간초과
# n = int(input())
# coor = list(map(int, input().split()))
# ans = [0 for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if coor[i] < coor[j]:
#             ans[j] += 1

# for i in ans:
#     print(i, end=' ')

n = int(input())
coor = list(map(int, input().split()))
zipped = sorted(set(coor))
ret = {value: idx for idx, value in enumerate(zipped)}
    

for i in coor:
    print(ret[i], end=' ')