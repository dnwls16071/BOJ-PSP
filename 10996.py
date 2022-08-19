# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

N = int(input())
even = N // 2
odd = N - N // 2

for i in range(N):
    print("* " * odd)
    print(" *" * even)