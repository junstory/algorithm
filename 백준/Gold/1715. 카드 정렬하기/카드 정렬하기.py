import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    num = int(input())
    heap.append(num)

heapq.heapify(heap)
count = 0
while len(heap) > 1:
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    heapq.heappush(heap, num1 + num2)
    count += num1 + num2
    
print(count)