# 두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다. 예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다. 자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다. x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.
#
# 자연수 N이 주어졌을 때, g(N)을 구해보자.

# Code1 => 시간초과
def f(A):
    total = 0
    for i in range(1, A+1):
        if A % i == 0:
            total += i
    return total

def g(x):
    total = 0
    while x != 0:
        if x > 0:
            total += f(x)
            x -= 1
    return total

T = int(input())
for _ in range(T):
    N = int(input())
    print(g(N))

# Code2
import sys
input = sys.stdin.readline

MAX = 1000000
dp = [0] * (MAX + 1)    # dp테이블
dp_sum = [0] * (MAX + 1)    # dp테이블 누적합

for i in range(1, MAX+1):
    j = 1
    while i * j <= MAX:
        dp[i * j] += i
        j += 1
    dp_sum[i] = dp_sum[i-1] + dp[i]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp_sum[N])

# Code1은 일반적인 함수로 작성한 코드인데 시간초과가 발생했다.

# Code2 설명
# dp[i] = i의 약수의 합
# dp_sum[i] = 1 ~ i까지의 약수의 합(dp테이블의 누적 배열)
