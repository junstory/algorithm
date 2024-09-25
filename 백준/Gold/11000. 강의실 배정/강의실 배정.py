import heapq
import sys
input = sys.stdin.readline

# 우선순위 큐 활용하기
n = int(input())
table = []
for i in range(n):
    temp = list(map(int, input().split()))
    table.append(temp)

table.sort()
rooms = []
heapq.heappush(rooms, table[0][1])

for i in range(1, n):
    if rooms[0] <= table[i][0]:
        heapq.heappop(rooms)
        heapq.heappush(rooms, table[i][1])
    else:
        heapq.heappush(rooms, table[i][1])
print(len(rooms))


# 먼저 시작하는대로 강의실을 배정하고
# 겹치면 새로운 강의실을 배정한다.
# 아래는 시간초과.
# while과 for문에 의한 것으로 생각 됨.. 
# table : n
# rooms : 점차 n 만큼 커짐
# 결국 O(n^2) 이 되어버림.

# n = int(input())
# table = []
# for i in range(n):
#     temp = list(map(int, input().split()))
#     table.append(temp)

# table.sort(key=lambda x: x[0])
# rooms = []

# rooms.append([table[0]])
# #print(rooms)
# table.pop(0)
# while table:
#     #print(table)
#     lecture = table.pop(0)
#     assigned = False
#     for i in range(len(rooms)):
#         if rooms[i][-1][1] <= lecture[0]:
#             rooms[i].append(lecture)
#             assigned = True
#             break
#     if not assigned:
#         rooms.append([lecture])
        
# print(len(rooms))