n, k = map(int,input().split())
ret = 1
for i in range(n,n-k,-1):
    ret *= i
for i in range(1,k+1):
    ret/=i
print(int(ret))