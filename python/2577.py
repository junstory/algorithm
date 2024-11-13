a = int(input())
b = int(input())
c = int(input())
ans = [0]*10
ret = a*b*c
while ret != 0:
    ans[ret%10] += 1
    ret = ret // 10

for i in ans:
    print(i)