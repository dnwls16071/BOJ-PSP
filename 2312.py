# 양의 정수 N이 주어졌을 때, 이 수를 소인수분해 한 결과를 출력하는 프로그램을 작성하시오.

T = int(input())

for _ in range(T):
    a = int(input())
    for i in range(2, a+1):
        count = 0
        if a % i == 0:
            while a % i == 0:
                a = a // i
                count += 1
            print(i, count)
        elif a == 1:
            break