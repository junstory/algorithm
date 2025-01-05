import heapq
import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    max_heap = []
    min_heap = []
    is_valid = {}

    m = int(input())
    for j in range(m):
        a, b = input().split()
        b = int(b)
        if a == 'I':
            heapq.heappush(min_heap, b)
            heapq.heappush(max_heap, -b)
            is_valid[b] = is_valid.get(b, 0) + 1
        else:
            if not min_heap or not max_heap:
                continue
            if b == 1:
                while max_heap and is_valid[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    value = -heapq.heappop(max_heap)
                    is_valid[value] -= 1
            else:
                while min_heap and is_valid[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    value = heapq.heappop(min_heap)
                    is_valid[value] -= 1

    while max_heap and is_valid[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    while min_heap and is_valid[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    
    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0], min_heap[0])