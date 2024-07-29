n, m = map(int, input().split())
# N^2으로는 풀 수 없음. n,m의 최대는 500,000
# a = []
# b = []
# for i in range(n):
#     a.append(input())

# for i in range(m):
#     b.append(input())

# num = a if len(a) < len(b) else b
# ans = []
# count = 0
# for i in num:
#     try:
#         a.index(i)
#         b.index(i)
#         ans.append(i)
#         count += 1
#     except:
#         pass
            
# print(count)
# ans.sort()
# #print(ans)
# for i in ans:
#     print(i)

dic = {}
for i in range(n):
    name = input()
    dic[name] = 1
for i in range(m):
    name = input()
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1
ans = []
for i in dic:
    if dic[i] == 2:
        ans.append(i)
ans.sort()
print(len(ans))
for i in ans:
    print(i)