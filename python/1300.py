n = int(input())
k = int(input())

arr = [ [ 0 for i in range(n)] for i in range(n)]

# n은 최대 10만이라서 애초에 값을 계산할 생각을 하면 안되겠다.
# 커지는 규칙... 지그재그?
for i in range(1,n+1):
    for j in range(1,n+1):
        arr[i-1][j-1] = i*j

for i in arr:
    for j in i:
        print(str(j).center(2),end=" ")
    print()

ret = []
for i in arr:
    for j in i:
        ret.append(j)
ret.sort()

print(ret[k-1])

