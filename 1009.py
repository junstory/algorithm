t = int(input())

#a^b니까 1초에 수행 불가. 시간초과
# for i in range(t):
#     a, b = map(int, input().split())
#     print(a**b%10)

# a^b의 일의 자리수는 a의 일의 자리수와 b의 일의 자리수에 따라 결정된다.
# 즉 1의 자리만 구하고 곱할거 곱하고. 이를 반복해도 된다.
#그치만 이것도 시간초과. 최대 100^1,000,000이니까 1억은 가뿐히 넘음.
# for i in range(t):
#     a, b = map(int, input().split())
#     for j in range(b-1):
#         a *= a
#         a %= 10
#     print(a%10)

# 규칙?
# 결국 1의 자리끼리 곱하는 것.
# 일의 자리가
# 1이면 계속 1, 2면 2,4,,8,6 3이면, 3,9,7,1 4면 4,6
# 5는 5 6은 6, 7은 7,9,3,1 8은 8,4,2,6 9는 9,1
#하나인거는 그냥 예외처리 해주고
# 다른 숫자는 최대 4제곱이면 1의자리가 결정남.
#그래서 b도 4의 나머지로 바꾸기.
#이때 a는 0이면 10, b는 0이면 4라는 점..!
for i in range(t):
    a, b = map(int, input().split())
    a %= 10
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    else:
        b %= 4
        if b == 0:
            b = 4
        print(a**b%10)