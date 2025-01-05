import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    x = int(input())
    if x == 0:
        if heap:
            node = heapq.heappop(heap)
            print(node[0] if node[1] else -node[0])
        else:
            print(0)
    else:
        node = (x, 1) if x >0 else (-x, 0)
        heapq.heappush(heap, node)
