L = int(input())
s = input()

r = 31
M = 1234567891
hash = 0
for i in range(L):
    hash += ((ord(s[i]) - 96) * r ** i) 
    


print(hash% M)