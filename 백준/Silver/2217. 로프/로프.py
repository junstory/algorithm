n = int(input())

ropes = []
for i in range(n):
    ropes.append(int(input()))

ropes.sort(reverse=True)
ans = []
for i in range(n):
    ans.append(ropes[i]*(i+1))

print(max(ans))