# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

#1번 코드
N = int(input())

for i in range(1, N):
    print("*"*i + " "*(N-i))

for i in range(N, 0, -1):
    print("*"*i + " "*(N-i))

#2번 코드
N = int(input())

for i in range(1, N+1):
    print("*"*i)

for i in range(N-1, 0, -1):
    print("*"*i)