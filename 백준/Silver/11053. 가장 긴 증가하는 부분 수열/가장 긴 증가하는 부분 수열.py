
def sol(arr):
    answer = 0
    length = [1]*len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                length[i] = max(1 + length[j], length[i])
    answer  = max(length)
    return answer

n = int(input())
arr = list(map(int, input().split()))
print(sol(arr))