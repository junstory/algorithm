n = input()
n = list(n)
n.sort()
count = dict()
for i in n:
    if count.get(i) == None:
        count[i] = 1
    else:
        count [i] = count[i] + 1
odd = 0
mid = ""
ret = ""
for alpha, num in count.items():
    if num % 2 == 1:
        odd += 1
        mid = alpha
    if odd > 1:
        print("I'm Sorry Hansoo")
        exit()

for alpha, num in count.items():
    ret += alpha * (num // 2)

print(ret + mid + ret[::-1])
            
    