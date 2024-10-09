n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

for i in m_list:
    start = 0
    end = n-1
    find = False
    while start <= end:
        mid = (start + end) // 2
        if n_list[mid] == i:
            find = True
            break
        elif n_list[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    if find:
        print(1)
    else:
        print(0)