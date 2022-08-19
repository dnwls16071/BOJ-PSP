# 두 개의 이진수를 입력받아 이를 더하는 프로그램을 작성하시오.

A, B = map(str, input().split())

# 이진수를 표사하기위해 사용할 수 있는 int함수의 다른 방법
# int(숫자, 2)를 한다면 이진수로 변환가능
A = int(A, 2)
B = int(B, 2)
C = A + B

print(bin(C)[2:])