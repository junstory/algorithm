n = input()

n = n.split("-")
total = 0
if n[0] == "":
    total = 0
else:
    total = sum(map(int, n[0].split("+")))

for i in n[1:]:
    total -= sum(map(int, i.split("+")))

print(total)