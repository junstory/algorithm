n, m = map(int, input().split())
max_num = n if m > n else m
min_num = m if m > n else n
ans = 0
while min_num != 0:
    ans = max_num%min_num
    max_num = min_num
    min_num = ans
ans = max_num
    
print(ans)

# n*m을 최대 공약수로 나눈 값이 최소 공배수
print(n*m//ans)