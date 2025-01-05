import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
jewel = []
bag = []
ans =0
for i in range(n):
    weight, value = map(int, input().split())
    jewel.append((weight, value))

for i in range(k):
    capacity = int(input())
    bag.append(capacity)

jewel.sort()
bag.sort()

max_heap = []
j = 0
for capacity in bag:
    while j < n and jewel[j][0] <= capacity:
        heapq.heappush(max_heap, -jewel[j][1])
        j += 1
    if max_heap:
        ans += -heapq.heappop(max_heap)
print(ans)