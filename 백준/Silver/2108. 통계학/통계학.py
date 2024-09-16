import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
ret = []
cnt = [0]*8001
summ = 0
for i in range(n):
    temp = int(input())
    summ += temp
    ret.append(temp)
    cnt[temp+4000] += 1
ret.sort()
#print(ret)
print(round(summ/n))
print (ret[n//2])

# 상위 두 개만 보기
# cnter = Counter(ret)
# if len(cnter) != 1:
#   mode = cnter.most_common(2)
#   if mode[0][1] == mode[1][1]:
#     print(mode[1][0])
#   else:
#     print(mode[0][0])
# else:
#   mode = cnter.most_common(1)
#   print(mode[0][0])

cnt1, max1 = max(cnt), cnt.index(max(cnt))-4000
cnt[max1+4000] = 0
cnt2, max2 = max(cnt), cnt.index(max(cnt))-4000
if cnt1 == cnt2:
    print(max2)
else:
    print(max1)
#print(cnt.index(max(cnt))-4000)
print(ret[-1]-ret[0])