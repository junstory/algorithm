n = int(input())

num = 0
count = 0
while True:
    num += 1
    if '666' in str(num):
        #print(num)
        count += 1
    if count == n:
        print(num)
        break