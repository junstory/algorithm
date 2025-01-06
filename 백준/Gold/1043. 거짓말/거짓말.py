
node = [i for i in range(51)]
party = []
def find(v):
    if v == node[v]:
        return v

    return find(node[v])

def union(a,b):
    a = find(a)
    b = find(b)
    if a< b:
        node[b] = a
    else:
        node[a] = b

n, m = map(int, input().split())
k = input().split()
know = int(k[0])
k = k[1:]
knows = set()
for i in range(know):
    union(0, int(k[i]))

for i in range(m):
    tmp = input().split()
    tmp = tmp[1:]
    party.append(tmp)
    root = int(tmp[0])
    for i in range(len(tmp)):
        union(int(tmp[i]), root)


count = 0
for i in party:
    check  = False
    for j in i:
        if find(int(j)) == 0:
            check = True
            break
    if not check:
        count += 1

print(count)


