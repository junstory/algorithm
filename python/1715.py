import heapq


def solution(heap, n):
    count = 0
    if n == 1:
       return 0
    while len(heap) > 1:
         a = heapq.heappop(heap)
         b = heapq.heappop(heap)
         #print(a, b)
         count += a + b
         heapq.heappush(heap, a+b)
    return count

heap = []
n = int(input())
for i in range(n):
    heapq.heappush(heap, int(input()))

answer = solution(heap, n)
print(answer)