# 해밍 거리란 두 숫자의 서로 다른 자리수의 개수이다. 두 이진수가 주어졌을 때, 해밍 거리를 계산하는 프로그램을 작성하시오.


T = int(input())
for _ in range(T):
    A = input()
    B = input()
    distance = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            distance += 1
    print("Hamming distance is " + str(distance) + ".")