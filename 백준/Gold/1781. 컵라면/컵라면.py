import heapq
n = int(input())
prob = []

for i in range(n):
    prob.append(list(map(int,input().split())))


#prob.sort(key=lambda x: (x[0],-x[1]))
prob.sort()
#print(prob)

ans = []
for i in prob:
    heapq.heappush(ans,i[1])
    #print("ADD: ", ans)
    if len(ans) > i[0]:
        heapq.heappop(ans)
    #print("Ret: ",ans)
print(sum(ans))


# ans = []
# heapq.heappush(ans,prob[0][1])
# for i in range(1,n):
#     heapq.heappush(ans,prob[i][1])
#     if len(ans) > prob[i][0]:
#         continue

# 보상이 큰 것부터
# 데드라인이 작은 것부터

# lastN = prob[0][0]
# ret = prob[0][1]
# for i in range(1,n):
#     if prob[i][0] == lastN:
#         continue
#     else:
#         lastN = prob[i][0]
#         ret += prob[i][1]
# print(ret)
        
