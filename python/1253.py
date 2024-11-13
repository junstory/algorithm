# n = int(input())
# nums = list(map(int, input().split()))
# count = 0

# nums.sort()
# for goal_idx, goal in enumerate(nums):
    
#     for idx, i in enumerate(nums):
#         start = 0
#         end = n-1
#         while start < end:
#             mid = (start + end)//2
#             if (i+nums[mid]) == goal and (goal_idx != mid and goal_idx != idx):
#                 count += 1
#             elif   (i+nums[mid]) > goal:
#                 end = mid-1
#             else:
#                 start = mid +1
# print(count)



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