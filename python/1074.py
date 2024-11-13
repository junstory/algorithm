n, r, c = map(int ,input().split())
count = 0
# 시도 2
# 좌표를 기반으로 이전 값은 계산 끝내버리기~
# 분할 정복
while n != 0 :
    n -= 1
    size  = (2**n)*(2**n)
    if r < 2**n and c < 2**n:
        count += size * 0
    elif r < 2**n and c >= 2**n:
        count += size * 1
        c -= 2**n
    elif r >= 2**n and c < 2**n:
        count += size * 2
        r -= 2**n
    elif r >= 2**n and c >= 2**n:
        count += size * 3
        r -= 2**n
        c -= 2**n
    
    

print(count)

# 시도 1
# 모든 배열의 순서를 결정하는 것은 메모리를 너무 많이 사용함.
# 순서의 규칙을 찾아서 r,c의 순서만 딱 찾자..
# n = 2 ** n
# size = n*n
# li = [[0]*n for i in range(n)]
# count = 0

# def sol(s,e,n):
#     global count
#     size = n*n
#     if size == 1:
#         li[s][e] = count
#         count += 1
#         return
#     sol(s,e,n//2)
#     sol(s,e+n//2,n//2)
#     sol(s+n//2,e,n//2)
#     sol(s+n//2,e+n//2,n//2)

# sol(0,0,n)
# # for elem in li:
# #     print(elem)
# print(li[r][c])

    # li[s][e] = count
    # count += 1
    # li[s][e+1] = count
    # count+= 1
    # li[s+1][e] = count
    # count+=1
    # li[s+1][e+1] = count