from math import factorial
def a(o,tw,th):
    li = [3]*th + [2]*tw + [1]*o
    
for _ in range(int(input())):
    n = int(input())
    r = 0
    thr = 0
    two = 0
    one = n- thr*3
    while n - thr*3>= 0:
        
        total = one + two + thr
        #print(total)
        ret3 = factorial(total)/(factorial(total-thr)*factorial(thr))
        ret2 = factorial(total-thr)/(factorial(total-thr-two)*factorial(two))
        ret1=factorial(total - thr - two)/(factorial(total - thr - two - one)*factorial(one))
        #print(ret1, ret2, ret3)
        r +=ret1 * ret2* ret3
        
        if n - thr*3 - (two+1)*2>= 0:
            one -= 2
            two += 1
        else:
            thr += 1
            two = 0
            one = n- thr*3
    print(int(r))