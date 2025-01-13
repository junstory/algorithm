k, n = map(int, input().split())

lines = []

for i in range(k):
    lines.append(int(input()))

start = 1
end = max(lines)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for line in lines:
        count += line // mid
    
    if count >= n:
        start = mid + 1
    else:
        end = mid - 1
    

    

print(end)