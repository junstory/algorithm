import heapq
import sys

input = sys.stdin.readline

n = int(input())
max_heap = []
min_heap = []

for i in range(n):
    num = int(input())
    heapq.heappush(max_heap, -num)
    if min_heap and -max_heap[0] > min_heap[0]:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    
    if len(max_heap) >= len(min_heap):
        print(-max_heap[0])
    else:
        print(min_heap[0])