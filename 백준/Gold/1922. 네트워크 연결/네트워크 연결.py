def findParent(x):
    if parent[x] != x:
        parent[x] = findParent(parent[x])
    return parent[x]

def unionParent(a,b):
    a = findParent(a)
    b = findParent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
edge_num = int(input())
# parent[i] 자신의 부모
parent = [ i for i in range(n+1)]

#비용
value = [ [10001]*(n+1) for i in range(n+1)]

edges = []
total_cost = 0
for i in range(edge_num):
    a, b, cost = map(int,input().split())
    if a > b:
        a, b = b, a
    edges.append((a,b,cost))

edges.sort(key=lambda x: x[2])
#print(edges)
while edges:
    a, b, cost = edges.pop(0)
    if findParent(parent[a]) != findParent(parent[b]):
        value[a][b] = cost
        value[b][a] = cost
        unionParent(a,b)
        #print(a,b,cost)
        total_cost += cost

# for i in value:
#     for j in i:
#         print(str(j).center(2),end=" ")
#     print()

print(total_cost)