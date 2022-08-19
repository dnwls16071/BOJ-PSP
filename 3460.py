# 양의 정수 n이 주어졌을 때, 이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램을 작성하시오. 최하위 비트(least significant bit, lsb)의 위치는 0이다.

T = int(input())

for i in range(T):
    n = int(input())
    num = bin(n)[2:]
    for i in range(len(num)):
        if num[::-1][i] == "1":
            print(i, end = " ")