# 최소 힙
#
import sys
input = sys.stdin.readline
def heapify(heap):
    last = len(heap)//2
    for curr in range(last-1 ,-1, -1):
        heap = shiftDown(heap,curr,len(heap))
    return heap

def heappop(heap):
    if not heap:
        print(0)
        return heap
    elif len(heap) == 1:
        print(heap.pop())
        return heap

    pop_data, heap[0] = heap[0], heap.pop()
    shiftDown(heap,0,len(heap))
    print(pop_data)
    return heap

def heappush(heap,data):
    heap.append(data)
    idx = len(heap) -1
    while idx >0:
        parent = (idx-1)//2
        if heap[parent] > data:
            heap[parent], heap[idx] = heap[idx], heap[parent] 
            idx = parent
        else:
            break
    return heap

def shiftDown(heap, parent, last):
    while parent < last:
        child = parent * 2 + 1
        sibling = child + 1
        if sibling < last and heap[child] > heap[sibling]:
            child = sibling
        if child < last and heap[parent] > heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent] 
            parent = child
        else:
            break
    return heap

n = int(input())
heap = list()
length = 0
while n != 0:
    n -= 1
    data = int(input())
    if data == 0 :
        heap = heappop(heap)
    else:
        heap = heappush(heap, data)
    #print(heap)
