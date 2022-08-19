# 정수 n(0 < n < 1000)과 수의 목록이 주어졌을 때, 목록에 들어있는 수가 n의 배수인지 아닌지를 구하는 프로그램을 작성하시오.

n = int(input())

while True:
    number = int(input())    
    if number == 0:
        break

    if number % n == 0:
        print(str(number) + " is a multiple of " + str(n) + ".")
    else:
        print(str(number) + " is NOT a multiple of " + str(n) + ".")