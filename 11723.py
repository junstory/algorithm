import sys
ret = set()

n = int(input())
for i in range(n):
    x = sys.stdin.readline().strip().split()
    if len(x) == 1:
        if x[0] == "all":
            ret = set([i for i in range(1,21)])
        if x[0] == "empty":
            ret = set()
    else:
        cmd = x[0]
        num = int(x[1])
        if cmd == "add":
            ret.add(num)
        if cmd == "remove":
            ret.discard(num)
        if cmd == "check":
            if num in ret:
                print(1)
            else:
                print(0)
        if cmd == "toggle":
            if num in ret:
                ret.discard(num)
            else:
                ret.add(num)
    