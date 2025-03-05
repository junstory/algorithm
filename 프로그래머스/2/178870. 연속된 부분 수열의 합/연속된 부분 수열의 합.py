def solution(sequence, k):
    answer = []
    total = 0
    e = 0
    n = len(sequence)
    counter = n
    for s in range(n):
        while total < k and e < n:
            total += sequence[e]
            e += 1
        if total == k and e-s-1 < counter:
            counter = e-s-1
            answer =[s, e-1]
        total -= sequence[s]
    return answer