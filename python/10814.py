n = int(input())
ret = []
for i in range(n):
    age, name = map(str, input().split())
    ret.append((int(age),name))
ret.sort(key= lambda x :x[0])
for age, name in ret:
    print(age, name)