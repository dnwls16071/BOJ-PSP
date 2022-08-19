# 자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

A, B, C = map(int, input().split())

def power(a, b):
    if b == 1:
        return a % C
    else:
        temp = power(a, b // 2)
        if b % 2 == 0:
            return (temp * temp) % C
        else:
            return (temp * temp * a) % C
print(power(A, B))

# 수학적 배경지식이 있어야 해결할 수 있는 간단한 문제였다.
# 일일이 매번 거듭제곱을 하게 된다면 시간초과가 발생할 수 밖에 없는 문제였다.
# 이 문제의 알고리즘은 '거듭제곱 알고리즘'이었다.

