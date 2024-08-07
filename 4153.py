a,b,c = map(int,input().split())

while a != 0 and b != 0 and c!=0:
    a *= a
    b *= b
    c *= c
    if (a == b+c) or (b ==a+c) or (c ==a+b):
        print("right")
    else:
        print("wrong")
    a,b,c = map(int,input().split())

#입력을 리스트로 받고 정렬하면 제일 큰 값을 통해 
# a^2 = b^2 + c^2 공식을 사용할 수 있음
# 정렬하는 시간과 a,b,c각각에 대한 조건문 중 무엇이 더 시간 걸릴까?