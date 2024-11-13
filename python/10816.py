n = int(input())
counts = [0]*20000001
cards = list(map(int,input().split()))
for i in cards:
    counts[i+10000000] += 1
m = int(input())
finds = list(map(int,input().split()))

for i in finds:
    print(counts[i+10000000],end=" ")