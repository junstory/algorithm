n = int(input())
a = []
count = 0
for i in range(n):
    temp = list(map(int, input().split()))
    #temp.append(temp[1]-temp[0])
    a.append(temp)
a.sort(key = lambda x: (x[1],x[0]))
#print(a)

prev_e = a[0][1]
a.pop(0)
count += 1
for s, e in a:
    if s >= prev_e:
        count += 1
        prev_e = e
print(count)
