import sys
input = sys.stdin.readline

n,m = map(int,input().split())
store = {}
for i in range(n):
    site, pw = map(str,input().rstrip().split())
    store[site] = pw

for i in range(m):
    site = input().rstrip()
    print(store[site])