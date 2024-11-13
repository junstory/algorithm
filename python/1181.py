n = int(input())
li = []
temp = []
ret = []
for i in range(n):
    li.append(input())

for i in range(1,51):
    for v in li:
        if i == len(v):
            if v not in temp:
                temp.append(v)
    temp.sort()
    ret += temp
    temp = []

for elem in ret:
    print(elem)