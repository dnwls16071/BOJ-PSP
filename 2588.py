# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

A = str(input())
B = str(input())

C = int(A) * int(B[-1])
D = int(A) * int(B[-2])
E = int(A) * int(B[-3])
F = int(A) * int(B)

print(C)
print(D)
print(E)
print(F)
