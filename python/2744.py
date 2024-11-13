n = input()
ret =''
for i in n:
    if "A"<=i and i <="Z":
        ret += i.lower()
    else:
        ret += i.upper()
print(ret)