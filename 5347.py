# 두 수 a와 b가 주어졌을 때, a와 b의 최소 공배수를 구하는 프로그램을 작성하시오.

def GCD(a, b):
    while b != 0:
        remain = a % b
        a = b
        b = remain
    return a

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(a * b // GCD(a, b))

# 유클리드 호제법으로 쉽게 풀었다.