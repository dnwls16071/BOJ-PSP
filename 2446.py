# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

N = int(input())

for i in range(N):
    print(" " * i + "*" * ((N-i)*2 - 1))

for j in range(N-2, -1, -1):
    print(" " * j + "*" * ((N-j)*2 - 1))