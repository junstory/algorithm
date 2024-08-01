t = int(input())
ret = [0]*4
for i in range(t):
    n = int(input())
    ret[0] = n//25
    n = n%25
    ret[1] = n//10
    n = n%10
    ret[2] = n//5
    n = n%5
    ret[3] = n
    for i in ret:
        print(i, end= " ")
    print()
    