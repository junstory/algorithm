import sys
input = sys.stdin.readline
n = int(input())
L = []

# def rounder(n):
#     if (n % 100) >=50:
#         n = int(cutter//100) +1
#     else:
#         n = int(cutter//100)
#     return n

def rounder(n):
    if n-int(n) >= 0.5:
        return int(n)+1
    else:
        return int(n)
        
for i in range(n):
    L.append(int(input()))
#round 함수는 이상하다
#cutter = round(n*0.15)
cutter = rounder(n*0.15)

#print(cutter)
#print(n,L)
L.sort()
L = L[cutter:n-cutter]
if len(L) > 0 and n > 0:
    #summ = sum(L)
    #lenn = len(L)
    #print(int(summ//lenn+rounder(summ/lenn*100)))
    print(rounder(sum(L)/len(L)))
    #print(sum(L)/len(L))
    
else:
    print(0)