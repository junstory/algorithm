n = int(input())
nums =[]
have = list(map(int, input().split()))
for i in have:
    nums.append(i)
nums.sort()

m = int(input())
check = list(map(int, input().split()))

for number in check:
    start = 0
    end = n-1
    bool = False
    while start <= end:
        mid = (start + end) // 2
        value = nums[mid]
        if value == number:
            bool = True
            break
        elif value < number:
            start = mid + 1
        else:
            end = mid - 1
    if bool:
        print(1, end = " ")
    else:
        print(0, end=" ")