import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def backtrack(curr_seq, start):
    if len(curr_seq) == m:
        print(' '.join(map(str,curr_seq)))
        return
    
    for i in range(start, n+1):
        backtrack(curr_seq + [i], start)


backtrack([], 1)