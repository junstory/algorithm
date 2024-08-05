n = list(map(int,list(input())))
#print(n)
ret = [0]*10
for i in n:
    if i == 6 or i==9:
        if ret[6] > ret[9]:
            ret[9] +=1
        else:
            ret[6] += 1
    else:
        ret[i] += 1
#print(ret)
print(max(ret))