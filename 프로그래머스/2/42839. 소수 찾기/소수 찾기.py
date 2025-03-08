from itertools import permutations
import math
def solution(numbers):
    answer = 0
    primceCandidates = set()
    numbers = list(map(str, list(numbers)))
    for i in range(1, len(numbers)+1):
        combi = list(permutations(numbers,i))
        
        for num in combi:
            primceCandidates.add(int("".join((list(num)))))
    #print(primceCandidates)
    for i in primceCandidates:
        if i < 2:
            continue
        if i == 2 or i == 3:
            answer += 1
            #print(i)
            continue
        isPrime = True
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            #print(i)
            answer += 1
                      
        
    return answer