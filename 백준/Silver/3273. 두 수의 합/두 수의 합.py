n = int(input())
nums = list(map(int, input().split()))
target = int(input())
count = 0

nums.sort()
# 이중for문 == O(n^2)
# 너무나 시간 초과,,
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             count += 1
#         elif nums[i] + nums[j] > target:
#             break

for i in range(len(nums)):
    start = i + 1
    end = len(nums) - 1
    while start <= end:
        mid = (start + end)//2
        if nums[i] + nums[mid] == target:
            count += 1
            break
        elif nums[i] + nums[mid] < target:
            start = mid +1
        else:
            end = mid-1
#print(nums)
print(count)