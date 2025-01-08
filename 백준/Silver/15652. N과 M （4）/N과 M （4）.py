n, m = map(int, input().split())

def backtrack(curr_seq, start):
    if len(curr_seq) == m :
        print(' '.join(map(str, curr_seq)))
        return
    
    for i in range(start, n+1):
        if curr_seq and curr_seq[-1] > i:
            continue
        backtrack(curr_seq + [i], i)

backtrack([], 1)