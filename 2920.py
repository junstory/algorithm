li = list(map(int,input().split()))
ret = []
for i in range(len(li)-1):
    if li[i] < li[i+1]:
        ret.append(0)
    elif li[i] > li[i+1]:
        ret.append(1)

if 0 not in ret:
    print("descending")
elif 1 not in ret:
    print("ascending")
else:
    print("mixed")