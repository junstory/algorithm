n = int(input())
nums = list(map(int, input().split()))
count = 0

nums.sort()
for goal_idx, goal in enumerate(nums):
    
    for idx, i in enumerate(nums):
        start = 0
        end = n-1
        while start < end:
            mid = (start + end)//2
            if (i+nums[mid]) == goal and goal_idx != mid and goal_idx != idx:
                count += 1
            elif   (i+nums[mid]) > goal:
                end = mid-1
            else:
                start = mid +1
print(count)