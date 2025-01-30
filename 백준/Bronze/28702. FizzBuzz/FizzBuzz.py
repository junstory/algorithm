inputs = []

for i in range(3):
    tmp = input()
    if tmp != 'FizzBuzz' and tmp != 'Fizz' and tmp != 'Buzz':
        num = int(tmp) +(3-i)

if num % 3 == 0 and num % 5 ==0:
    print('FizzBuzz')
elif num % 3 == 0:
    print('Fizz')
elif num % 5 == 0:
    print('Buzz')
else:
    print(num)
        

