n = int(input())

sol = [0]*12
sol[1] = 1
sol[2] = 2
sol[3] = 4
for i in range(4,12):
    sol[i] = sol[i-1] + sol[i-2] + sol[i-3]

for i in range(n):
    num = int(input())
    print(sol[num])