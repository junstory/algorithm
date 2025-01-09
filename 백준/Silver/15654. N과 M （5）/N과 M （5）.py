import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

def backtrack(curr_seq, start):
    if len(curr_seq) == m:
        print(' '.join(map(str,curr_seq)))
        return
    
    for i in range(start, n):
        if arr[i] not in curr_seq:
            backtrack(curr_seq + [arr[i]], 0)


backtrack([], 0)