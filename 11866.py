n, k = map(int, input().split())
a = list(i for i in range(1,n+1))
ret = []
i = 1
while a:
    #print(a)
    if(i>=k and i%k == 0):
        ret.append(a.pop(0))
    else:
        a.insert(len(a), a.pop(0))
    i += 1
print('<', end='')
for i in range(len(ret)-1):
    print(ret[i], end=', ')
print(str(ret[-1])+'>')
    