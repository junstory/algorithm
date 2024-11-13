n = int(input())
a = list(map(int, input().split()))
t, p = map(int, input().split())

count = 0
for i in a:
    if i > 0:
        count += i//t + 1
    if i>=t and i%t == 0:
        count -= 1
print(count)
print(n//p, n%p)