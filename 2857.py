ans = []
for i in range(1, 6):
    name = input()
    if 'FBI' in name:
        #print(name)
        ans.append(i)

if ans:
    for i  in ans:
        print(i, end=' ')
else:
    print('HE GOT AWAY!')