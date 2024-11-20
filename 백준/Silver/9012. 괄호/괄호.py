n = int(input())

def sol(temp):
    l_count = 0
    r_count = 0
    for i in temp:
        if i == '(':
            l_count += 1
        elif i == ')' and l_count > 0:
            l_count -= 1
        elif i==')' and l_count == 0:
            return "NO"
    if l_count == 0:
        return "YES"
    else:
        return "NO"

for i in range(n):
    temp = list(input())
    print(sol(temp))