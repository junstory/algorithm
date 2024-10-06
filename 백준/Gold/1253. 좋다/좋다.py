n = int(input())
nums = list(map(int, input().split()))
count = 0

nums.sort()
for i in range(n):
    goal = nums[i]
    start = 0
    end = n-1
    while start < end:
        if nums[start] + nums[end] == goal:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                count += 1
                break
        elif nums[start] + nums[end] > goal:
            end -= 1
        else:
            start += 1
print(count)