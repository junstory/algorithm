import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print((-1)*heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, (-1)*x)
