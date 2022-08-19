# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

N = int(input())

for i in range(1, N):   # N=5인 경우 1~4까지 
    print(" "*(N-i) + "*"*(2*i-1))

for i in range(N, 0, -1):   # N=5인 경우 5~1까지
    print(" "*(N-i) + "*"*(2*i-1))
