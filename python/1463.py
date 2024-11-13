n = int(input())

ans = [0 for i in range(1000001)]

ans[1] = 0
ans[2] = 1
ans[3] = 1

for i in range(4,n+1):
   ans[i] = min(ans[i-1],ans[i//2]+i%2,ans[i//3]+i%3)+1

print(ans[n])