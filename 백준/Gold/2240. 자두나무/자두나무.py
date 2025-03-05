t, w = map(int, input().split())
tree = [0]
for i in range(t):
    tree.append(int(input()))
#안움직일수도 있으니까 0번 이동도 계산해야 함
dp = [[0]*(w+1) for _ in range(t+1)]

#1번 나무에 있다면 나머지가 1나와서 1 추가, 아니면0,
#움직여서 2번 나무에 있다면 1이면 0, 2면 나눠져서 1
dp[1][0], dp[1][1] = tree[1]%2, tree[1]//2  
for i in range(2, t+1):
    for j in range(w+1):
        # w가 짝수면 1번에 있는 것(갔다가 왔다)이므로 1번에 있다면 나머지를 확인해서 1번에 있는지 확인
        # 홀수면 2번에 있는 것. 2번에 있다면 몫이 1이 나올 것임.
        jadu = tree[i]%2 if j%2 == 0 else tree[i]//2 
        #j번 움직였을 때의 결과니까 j를 더함.
        dp[i][j] = max(dp[i-1][0:j+1]) + jadu

print(max(dp[-1]))

