
#시도2
t = int(input())
for i in range(t):
    ret = ""
    cmds = list(input())
    n = int(input())
    s = input()
    start, end = 0, n
    direction = 1
    li = []
    if n > 0:
        s = s[1:len(s)-1]
        li = list(map(int, s.split(",")))
    for cmd in cmds:
        if cmd == 'R':
            direction *= -1
        if cmd == 'D':
            if start > end or n == 0:
                ret = 'error'
                break
            if direction == 1:
                start += 1
                n -= 1
            else:
                end -= 1
                n -= 1

    if ret == 'error':
        print (ret)
        continue
    if not li:
        print("[]")
    else:
        ret = '['
        if direction == 1:
            li = str(li[start:end])
            li = li.replace(" ", "")
            print(li)
        else:
            li = li[start:end]
            li.reverse()
            li = str(li)
            li = li.replace(" ", "")
            print(li)

    


# 시도 1
# 직접 배열을 reverse 하는 것은 뒤집는 연산 시간이 오래 걸리므로 시간초과가 될 수 밖에 없다.
# 따라서 배열은 그대로 둔 상태로 바꾸는 방법을 고민해야 한다.
# t = int(input())
# li = []
# for i in range(t):
#     ret = ""
#     cmds = list(input())
#     n = int(input())
#     s = input()
#     if n > 0:
#         s = s[1:len(s)-1]
#         li = list(map(int, s.split(",")))
#     for cmd in cmds:
#         #print(cmd)
#         if cmd == 'R':
#             li.reverse()
#             #print(li)
#         elif cmd == 'D':
#             if n == 0:
#                 ret = 'error'
#                 break
#             li = li[1:]
#             n -= 1
#             #print(li)
#     if ret == 'error':
#         print(ret)
#         continue
#     if not li:
#         print("[]")
#     else:
#         ret = '['
#         for i in range(len(li)-1):
#             ret = ret + str(li[i])  + ','
#         ret = ret + str(li[-1]) + ']'
#         print(ret)
            
        